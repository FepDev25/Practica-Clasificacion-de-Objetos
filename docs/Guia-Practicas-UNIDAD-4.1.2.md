# GUÍA DE PRÁCTICAS UNIDAD 4.1.2: CLASIFICACIÓN Y DETECCIÓN DE OBJETOS MEDIANTE REDES NEURONALES PROFUNDAS (YOLOv11/YOLOv12 Y SUPER RESOLUTION)

## PARTE 1A (individual o en parejas)

- Emplear una red YOLOv11 o YOLOv12 (como se ha visto en classe) o similar a la que se haya realizado un proceso de transfer learning para segmentar objetivos de imagenes capturadas a temas de una webcam. Deberá realizar pruebas de rendimiento usingo GPUs vs CPU (para eligo puedaemployar las computadoras del laboratorio de Cofmu 8). El entregamente y validacion de resultados de la red puede hacerlo en Google Colab o enequalquier entorno de su preferencia. Por example, podrfa realizar una tarea similar a la segmentacion de personas como se describe en el cuaderno de Kaggle ("Human Segmentation Dataset - TikTok Dances", ver Ilustracion 1). Se sugiere employar imagenes que se pueda encontrar en repositories para realizar la tarea. No pode haber ningnun grupo que tengla las mismas imagenes ni usear un numero previamente desarrollado en Kaggle u other plataforma similar.

![](images/b134b8a61a3c88376e69ea1e4b61f6a3ba3f3b69557659a5f74ab2dae5fb4875.jpg)

KUCEV ROMAN · UPDATED 3 YEARS AGO

![](images/82e78f989dc8cc0018a803b98da819b1afbd940efe0571f5f82fc67d79a98d05.jpg)

![](images/404a227146b42c42212477ff9f64ec9127bee413caebb67729898e1773f54d8f.jpg)

![](images/a4fc658062cd12427300b93cf0d3c18db8d5ad19db7305827dd6383044373c40.jpg)

![](images/3cf2bd8a988a7540662097fd86678a2c8b6b8d14c66e12b664bc5211ecf0c35b.jpg)

### Human Segmentation Dataset - TikTok Dances

2615 images of a segmented dancing people

![](images/ae163e36e07fd5faa2a967191d6869c8e016ece8190e8fffa3c3dc9150b51ace.jpg)

Data Card

Code (9)

Discussion (0)

Suggestions (0)

### About Dataset

### Segmentation Full Body TikTok Dancing

Dataset includes 2615 images of a segmented dancing people.

Video of people dancing from TikTok were dowloaded and cut into frames. On each frame, all the dancing people were selected in Photoshop.

Usability ①

10.00

License

Attribution-NonCommercial-No...

Expected update frequency

Never

Ilustracion 1. Ejemplo de un dataset para segmentar personas a partir de videos de bailes en TikTok.

- Por另一边 parte, como PODemosajsir en la Ilustracion 2, se ha realizado un proceso de detectacion de objetos usingla red neuronal YOLOv8I (version large) en differedes imagenes:

![](images/1f54aa17156c4c10fb432161751513451d962336e9e31a3de79f2fe26f01603d.jpg)

(a)  
(c)  
![](images/456f3ef99d3e140272ec8751bbc732435822da39bc352c9e8a32749996ea8e1c.jpg)  
llustracion 2. Ejemplos de reconocimiento de objetos usingo YOLO8I en una imagen de una niña (a), en imagenes de escritorios (b) y (d) y en un aula en Biblian (c).

![](images/4eb12aa8705a3dcdca98ec6b3ce811aeb4951f02704f2c83124a5561e1edbe03.jpg)

![](images/3778ef3c7b14c17e88d5122b86a01da99a6c6945c6864f729ee8022139190f7a.jpg)  
(b)  
(d)

## PARTE 1B (individual)

- Realizar pruebas de rendimiento con dos redes neuronales: (a) YOLOv11 o YOLOv12 (como se ha visto en clase) y (b) una red para aplicar superResolution en video (actualizada de no más de 1 año de existencia), comparando GPUs vs CPU (paraarlodebeemployarlascomputadoras dellaboratorio de CómuTo8).Paraello,deberávisualizarlacantidaddeFramesporSegundoque tiene enCPUfrenteag GPU (ver Ilustracion2)，como se explicap en elejemplo visto en clase(video y@cdojo adjunto):

(a)  
![](images/572720124d303c3eda50ad4c83cad50f5026aaf0ca2ecc404151ed31a6ed91cd.jpg)  
Ilustracion 3. Ejemplos de detec tion de objetos usingla red neuronal YOLOv12 en CPU (a) y en GPU (b) de un video de recorrodo por las calles de Moscu.

![](images/0c153fddd9c808c278cdb4ea8c92492f9363949da712cb6b1b5997c58d4bc69e.jpg)  
(b)

- Cada estudante deben usar un computadordistincto (con una Mac Address Única)  
- Ningún esthududiente puede  
- Deberá registrar un video del Ergebnis que se obtiene tanto en CPU como en GPU y做不到 lasuma de información:

- Uso de la memoria con el commando nvidia-smi  
-Numero de FPS (frames per second) en GPU vs CPU  
- Uso de memoria RAM en GPU vs CPU  
Mac Address del Computador

## PARTE 1C (individual)

- Debe realizar un número en OpenCV C++ para preprocesamiento de imágenes en CPU vs GPU. Paraarlo, deben realizar las siguientes operaciones de cualquier exemple que dese (aplicación de imágenes Médicas, detectión de cordes, etc.):

Suavizio (Filtro Gaussiano)  

- Operaciones morfológicas (Erosión / Dilatación)  
$\mathrm{O}$  Detec tion de cordes (Canny)  
$\circ$  Eualización del historograma

- Por exemple, para executar estas operaciones (como se indica en类产品), OpenCV implementa una libreria para que el número corra sobre GPU (Tabla 1):

Table 1: Aplicación del filtró Gaussiano en CPU vs GPU.  

<table><tr><td>CPU:
cv::Mat blurred_cpu;
cv::GaussianBlur(frame, blurred_cpu, cv::Size(5, 5), 1.5);</td><td>GPU:
cv::CUDA::GpuMat d_frame, d_blurred;
d_frame.upload(frame);
auto gaussian = cv::CUDA::createGaussianFilter(d_frame.type(), d_frame.type(), cv::Size(5, 5), 1.5);
gaussian-&gt;apply(d_frame, d_blurred);</td></tr></table>

- Deberá realizar un análisis de resultados, considerando loCEE:

- Comparación qualitativa de los resultados visuales.  
- Comparación cuantitativa (tiempo de procesamiento por frame).  
$\circ$  Reflexión: ¿cual es la diferencia entre pipeline CPU  $\leftrightarrow$  GPU y Pipeline GPU-only? y ¿cuando vale la pena usar la GPU?

- Considerar que deben usar Pipeline GPU-only para realizar estaarea y deben incluir en el informe capturas de pantalla.

Tabla 2: Ejemplo de uso de pipeline GPU-only (eficiente)  

```txt
cv::cuda::GpuMat d_frame, d(gray, d_blur, d_edge;
```

```txt
cap.read(frame); // CPU
d_frame.upload(frame); // CPU  $\rightarrow$  GPU
```

```cpp
cv::cuda::cvtColor(d_frame, d(gray, cv::COLOR_BGR2GRAY); // GPU  
auto gauss = cv::cuda::createGaussianFilter(d(gray.type(), d(gray.type(), cv::Size(5,5), 1.5);  
gauss->apply(d(gray, d_blur); // GPU
```

```cpp
auto canny = cv::CUDA::createCannyEdgeDetector(50, 150);  
canny->detect(d_blur, d_edge); // GPU
```

Documentación de Soporte:  

```rust
cv::Mat result;  
d_edge download(result); // Solo al final  
cv::imshow("GPU Result", result);
```

```txt
- El enlace donde se encuesta el número de ejempo para create aplicaciones que usesan YOLOv5 y YOLOv8 es el que se detalla a continua:  
    - https://github.com/vlarobbky/yolov5-and-yolov8-object-detection-OpenCV-C-
```

```txt
- Tutorial "Object Detection using YOLOv5 OpenCV DNN in C++ and Python" de LearnOpenCV: https://learnopencv.com/object-detection-using-yolov5-and-opencv-dnn-in-c-and-python/
```

```txt
- Artístico Científico "A fine-tuned YOLOv5 deep learning approach for real-time house number detection": https://www.ncbi.nlm.nih.gov/PMC/articles/PMC10403189/
```

```html
- Tutorial “Intersection over Union (IoU) for object detection”: https://pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/
```

$\mathbf{R}$  ESULTADO(S) OBTENIDO(S):  

```txt
- Video tutorial (YouTube) "Train Yolov8 object detection on a custom dataset": https://www.youtube.com/watch?v=m9fH9OWn8YM
```

CONCLUSIONES:  

```txt
Al finalizar esta practica, los estudiantes lograron aplicar de forma efectiva Tecnicas avanzadas de detectacion de objetos mediante redes neuronales profundas, tales como YOLOv11 y MobileNetv3, asi como redes para super resolution y preprocesamento de imagenes con aceleracion GPU utilizingo CUDA y OpenCV. Fueron capaces de realizar un proceso de fine-tuning sobre datasets personalizados, implementaron mecanismos para evaluar el rendimiento entre CPU y GPU (FPS, uso de memoria y eficiencia), y desarrollaron tanto scripts en Python (Colab) como modulo's nativos en  $\mathrm{C} + +$  para pruebas comparativas. Asimismo, se evidencio una adeuada comprension de los conceptos de pipeline GPU-only, optimacion computational y diseño de flujos deficientes en tiempo real, aplicados en tareas reales como clasificacion de alfabetos extranjeros y procesamento de video en alta resolution.
```

```txt
Esta practica permite consolidar los conocimientos teoricos y practicos adquiridos durante el camino de
```

Visión por Computador, integrando componentes esencias de aprendizaje profundo, visión artificial y procesamento accelerado en GPU. Se pueda comprar que el uso de GPUs modernas (con soporte CUDA) permitte mejor significativamente el rendimiento en tareas de detectación y preprocesamento de imágenes, logrado hasta 5x-10x más velocidad comparado con executions en CPU. Además, es factible demostrar la importancia del uso de pipelines GPU-only paraatar los cuellos de botella causados por transferencias innecasarias entre memoria CPU y GPU. El desarrollo de solutions personalizadas con redes como YOLOv11 permitted a los estudiantes adaptar modelos deULTima generación acontextosspecificos, promoviendo el pensamento crítico, la experimentación responsable y la innovación Tecnológica en enternos educativos reales.

## RECOMENDACIONES

- Revisar previamente el entorno técnico: Asegurar de tener las dependencies necessarias configuradas (CUDA, OpenCV con soporte GPU, versiones correctas de Python o C++) paraatar contratiempo durante la practica.  
- Realizar pruebas profundas: Comenzar con datasetsPICYs y realizar pruebas incrementales para evaluar el comportamento de la red antes de escalar a conjuntos más complejos.  
- Fomentar la documentación del número y del processo experimental: Anotar resultados, Cambios en los hiperparámedos y observaciones para facilitar el análisis comparativo y la elaboración de informes.  
- Aprovechar las herramrientas de visualizacion como nvidia-smi y monitors de recursos paraDSLentender mayor el uso de la GPU y tomar decisiones informadas sobre la arquitectura de los modelos y la distribución de la energia computing.  
- Profundizar en métricas de evaluación como mAP, IoU, recall y precision para una evaluación más completa del rendimiento de los modeloshtubados.  
- Fomentar la ética académica y la originalidad en la elección de datasets y scripts, evitando el uso de SOLUTIONES ya desarrolladas en plataformas Públas sin un análisis propio o mejora significativa.

Docente / Técnico Docente: Ing. Vladimir Robles, Bykbaev

Firma:
