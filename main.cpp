#include <iostream>
#include <string>
#include <vector>
#include <chrono>
#include <iomanip>
#include <opencv2/opencv.hpp>
#include <opencv2/core/utils/logger.hpp>

// --- CONFIGURACIÓN MAESTRA ---
// Descomenta la siguiente línea SOLO cuando estés en la PC del laboratorio con NVIDIA
// #define ENABLE_CUDA 

#ifdef ENABLE_CUDA
#include <opencv2/cudaimgproc.hpp>
#include <opencv2/cudafilters.hpp>
#include <opencv2/cudaarithm.hpp>
#endif

using namespace std;
using namespace cv;

// Función auxiliar para obtener FPS
double getFPS(chrono::time_point<chrono::high_resolution_clock> start) {
    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> diff = end - start;
    return 1.0 / diff.count();
}

int main() {
    cv::utils::logging::setLogLevel(cv::utils::logging::LOG_LEVEL_ERROR);

    VideoCapture cap(0); // Cambia a "ruta/video.mp4" si prefieres
    if (!cap.isOpened()) {
        cerr << "Error: No se puede abrir la cámara/video." << endl;
        return -1;
    }

    // Configurar resolución para estresar un poco la máquina (HD)
    cap.set(CAP_PROP_FRAME_WIDTH, 1280);
    cap.set(CAP_PROP_FRAME_HEIGHT, 720);

    Mat frame, result_frame;
    
    // --- INICIALIZACIÓN DE FILTROS (Se hace FUERA del bucle) ---
#ifdef ENABLE_CUDA
    cout << ">>> MODO: GPU (CUDA) ACTIVADO <<<" << endl;
    
    // 1. Crear objetos GpuMat (Memoria VRAM)
    cuda::GpuMat d_frame, d_gray, d_blur, d_hist, d_eroded, d_edges;

    // 2. Crear los filtros (Esto es costoso, se hace una sola vez)
    // Filtro Gaussiano (Kernel 5x5)
    Ptr<cuda::Filter> gaussFilter = cuda::createGaussianFilter(CV_8UC1, CV_8UC1, Size(5, 5), 1.5);
    // Filtro Morfológico (Erosión)
    Mat element = getStructuringElement(MORPH_RECT, Size(3, 3));
    Ptr<cuda::Filter> erodeFilter = cuda::createMorphologyFilter(MORPH_ERODE, CV_8UC1, element);
    // Detector Canny
    Ptr<cuda::CannyEdgeDetector> cannyFilter = cuda::createCannyEdgeDetector(50, 150);

#else
    cout << ">>> MODO: CPU (SIMULACION LOCAL) <<<" << endl;
    Mat gray, blur, hist, eroded;
#endif

    while (true) {
        auto start_time = chrono::high_resolution_clock::now();
        
        cap >> frame;
        if (frame.empty()) break;

#ifdef ENABLE_CUDA
        // ================= PIPELINE GPU-ONLY =================
        [cite_start]// [cite: 111, 120] La guía exige no bajar a CPU entre pasos
        
        // 1. UPLOAD (El único paso lento de subida)
        d_frame.upload(frame);

        // 2. Preprocesamiento (Todo ocurre en VRAM)
        cuda::cvtColor(d_frame, d_gray, COLOR_BGR2GRAY);
        
        // 3. Suavizado
        gaussFilter->apply(d_gray, d_blur);

        // 4. Ecualización de Histograma
        cuda::equalizeHist(d_blur, d_hist);

        // 5. Erosión
        erodeFilter->apply(d_hist, d_eroded);

        // 6. Detección de Bordes (Canny)
        cannyFilter->detect(d_eroded, d_edges);

        // 7. DOWNLOAD (Bajamos solo el resultado final)
        d_edges.download(result_frame);

#else
        // ================= PIPELINE CPU (TU CASA) =================
        // Lógica espejo para verificar que los filtros funcionan
        
        cvtColor(frame, gray, COLOR_BGR2GRAY);
        GaussianBlur(gray, blur, Size(5, 5), 1.5);
        equalizeHist(blur, hist);
        erode(hist, eroded, getStructuringElement(MORPH_RECT, Size(3, 3)));
        Canny(eroded, result_frame, 50, 150);
#endif

        // --- MÉTRICAS Y VISUALIZACIÓN ---
        double fps = getFPS(start_time);
        
        string device_tag =
#ifdef ENABLE_CUDA 
        "GPU (CUDA)"; 
#else 
        "CPU (i9-13900H)"; 
#endif
        
        // Dibujar datos en pantalla (Requisito visual)
        putText(result_frame, "Dispositivo: " + device_tag, Point(10, 30), FONT_HERSHEY_SIMPLEX, 0.7, Scalar(255), 2);
        putText(result_frame, "FPS: " + to_string((int)fps), Point(10, 60), FONT_HERSHEY_SIMPLEX, 0.7, Scalar(255), 2);

        imshow("Laboratorio Vision - Pipeline", result_frame);

        if (waitKey(1) == 27) break; // ESC para salir
    }

    return 0;
}