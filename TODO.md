# TODO - Práctica Clasificación y Detección de Objetos

## PARTE 1A: YOLOv11/YOLOv12 con Transfer Learning (Individual o Parejas)

### Preparación

- [ ] Seleccionar dataset único (diferente a otros grupos)
  - No usar datasets previamente desarrollados en Kaggle
  - Buscar repositorios con imágenes apropiadas
  - Alternativa: Dataset similar a "Human Segmentation Dataset - TikTok Dances"

### Implementación

- [ ] Configurar entorno (Google Colab o local)
- [ ] Implementar red YOLOv11 o YOLOv12
- [ ] Realizar transfer learning sobre el dataset seleccionado
- [ ] Configurar captura desde webcam
- [ ] Implementar segmentación de objetivos en tiempo real

### Pruebas de Rendimiento

- [ ] Configurar pruebas en GPU (Laboratorio Cómpu 8)
- [ ] Ejecutar pruebas en CPU
- [ ] Registrar métricas de rendimiento:
  - Tiempo de inferencia
  - FPS (Frames Per Second)
  - Uso de memoria
  
### Validación

- [ ] Validar resultados de la red
- [ ] Documentar resultados con capturas/screenshots
- [ ] Preparar comparativa GPU vs CPU

---

## PARTE 1B: Pruebas de Rendimiento (Individual)

### Requisitos Previos

- [ ] Acceso al Laboratorio Cómpu 8
- [ ] Identificar Mac Address única del computador asignado
- [ ] Verificar que ningún otro estudiante use el mismo computador

### Red Neuronal YOLOv11/YOLOv12

- [ ] Implementar YOLOv11 o YOLOv12 para video
- [ ] Configurar procesamiento en CPU
- [ ] Configurar procesamiento en GPU
- [ ] Medir FPS en ambos casos

### Red de Super Resolution

- [ ] Seleccionar red de Super Resolution (máximo 1 año de antigüedad)
- [ ] Implementar procesamiento de video
- [ ] Configurar ejecución en CPU
- [ ] Configurar ejecución en GPU
- [ ] Medir rendimiento en ambos casos

### Registro de Métricas

- [ ] Grabar video de resultados en CPU
- [ ] Grabar video de resultados en GPU
- [ ] Ejecutar `nvidia-smi` y capturar uso de memoria GPU
- [ ] Registrar FPS en GPU vs CPU
- [ ] Registrar uso de memoria RAM en GPU vs CPU
- [ ] Documentar Mac Address del computador

### Documentación parte 1B

- [ ] Crear tabla comparativa de resultados
- [ ] Incluir capturas de `nvidia-smi`
- [ ] Adjuntar videos de demostración
- [ ] Análisis de diferencias de rendimiento

---

## PARTE 1C: OpenCV C++ CPU vs GPU (Individual)

### Configuración del Entorno

- [x] ✅ Instalar OpenCV con soporte CUDA (rutas configuradas)
- [ ] Verificar drivers de GPU (en laboratorio)
- [x] ✅ Configurar proyecto C++ (Makefile + CMakeLists.txt)

### Selección de Aplicación

- [x] ✅ Elegir dominio de aplicación:
  - Detección de bordes en video en tiempo real (webcam)

### Implementación de Operaciones

Implementar las siguientes operaciones en CPU y GPU:

#### 1. Suavizado (Filtro Gaussiano)

- [x] ✅ Implementar versión CPU: `cv::GaussianBlur()`
- [x] ✅ Implementar versión GPU: `cv::cuda::createGaussianFilter()`
- [ ] Comparar resultados (en laboratorio)

#### 2. Operaciones Morfológicas

- [x] ✅ Implementar Erosión en CPU
- [x] ✅ Implementar Erosión en GPU
- [ ] Implementar Dilatación en CPU (opcional, ya tienes erosión)
- [ ] Implementar Dilatación en GPU (opcional, ya tienes erosión)
- [ ] Comparar resultados (en laboratorio)

#### 3. Detección de Bordes (Canny)

- [x] ✅ Implementar Canny en CPU
- [x] ✅ Implementar Canny en GPU: `cv::cuda::createCannyEdgeDetector()`
- [ ] Comparar resultados (en laboratorio)

#### 4. Ecualización del Histograma

- [x] ✅ Implementar ecualización en CPU
- [x] ✅ Implementar ecualización en GPU
- [ ] Comparar resultados (en laboratorio)

### Pipeline GPU-Only

- [x] ✅ Diseñar pipeline eficiente GPU-only
- [x] ✅ Minimizar transferencias CPU ↔ GPU
- [x] ✅ Implementar flujo completo:

  ```cpp
  cap.read(frame);              // CPU
  d_frame.upload(frame);        // CPU → GPU
  // Todas las operaciones en GPU
  d_edge.download(result);      // GPU → CPU (solo al final)
  ```

### Análisis de Resultados

- [ ] Comparación cualitativa (resultados visuales) - EN LABORATORIO
- [ ] Comparación cuantitativa (tiempo por frame) - EN LABORATORIO
- [ ] Crear tabla de tiempos de procesamiento - EN LABORATORIO
- [x] ✅ Responder: ¿Diferencia entre pipeline CPU↔GPU y GPU-only? (ver README.md)
- [x] ✅ Responder: ¿Cuándo vale la pena usar GPU? (ver README.md)
- [ ] Incluir capturas de pantalla - EN LABORATORIO

### Documentación

- [x] ✅ Screenshots del código (preparado para capturar)
- [ ] Capturas de ejecución
- [ ] Gráficas de rendimiento
- [ ] Tabla comparativa de tiempos

---

## Recursos y Referencias

### Documentación parte 1c

- [ ] Revisar: YOLOv5 y YOLOv8 en OpenCV C++
  - <https://github.com/vlarobbky/yolov5-and-yolov8-object-detection-OpenCV-C->
  
- [ ] Tutorial LearnOpenCV: Object Detection usando YOLOv5
  - <https://learnopencv.com/object-detection-using-yolov5-and-opencv-dnn-in-c-and-python/>

- [ ] Paper: "A fine-tuned YOLOv5 deep learning approach"
  - <https://www.ncbi.nlm.nih.gov/PMC/articles/PMC10403189/>

- [ ] Tutorial: Intersection over Union (IoU)
  - <https://pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/>

- [ ] Video: Train YOLOv8 on custom dataset
  - <https://www.youtube.com/watch?v=m9fH9OWn8YM>

---

## Informe Final

### Estructura del Informe

- [ ] Introducción y objetivos
- [ ] Metodología (por cada parte)
- [ ] Resultados experimentales
- [ ] Análisis y discusión
- [ ] Conclusiones
- [ ] Recomendaciones
- [ ] Referencias bibliográficas

### Contenido Requerido

- [ ] Capturas de pantalla
- [ ] Videos de demostración
- [ ] Tablas comparativas
- [ ] Gráficas de rendimiento
- [ ] Código fuente comentado
- [ ] Análisis crítico de resultados

### Métricas de Evaluación

- [ ] mAP (mean Average Precision)
- [ ] IoU (Intersection over Union)
- [ ] Recall
- [ ] Precision
- [ ] FPS
- [ ] Uso de memoria
- [ ] Tiempo de procesamiento

---

## Notas Importantes

⚠️ **Requisitos de Originalidad**

- Cada grupo debe usar dataset único
- No copiar notebooks de Kaggle sin análisis propio
- Documentar todo el proceso experimental

⚠️ **Configuración Técnica**

- Verificar CUDA instalado correctamente
- OpenCV compilado con soporte GPU
- Drivers NVIDIA actualizados
- Python/C++ versiones compatibles

⚠️ **Entrega**

- Respetar fechas límite
- Incluir todos los archivos solicitados
- Videos y capturas de pantalla claras
- Código ejecutable y documentado
