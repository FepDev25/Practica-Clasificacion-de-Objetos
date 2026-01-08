# CHECKLIST PARA EL LABORATORIO

## ANTES DE IR
- [ ] Llevar pendrive o tener acceso a GitHub para copiar el proyecto
- [ ] Anotar el horario disponible del laboratorio
- [ ] Verificar que llevas el [README.md](README.md) impreso o en digital

## AL LLEGAR AL LABORATORIO

### 1. Verificación Inicial (5 min)
```bash
# Verificar GPU
nvidia-smi

# Verificar CUDA
nvcc --version

# Anotar especificaciones
lscpu | grep "Model name"
nvidia-smi --query-gpu=name --format=csv
```

### 2. Capturar Mac Address
```bash
ip link show | grep ether
# ANOTAR AQUÍ: _________________________
```

### 3. Preparar el Proyecto (5 min)
```bash
# Copiar carpeta 1C al sistema
cd ~/
cp -r /ruta/a/tu/pendrive/1C ./practica_1C
cd practica_1C
```

### 4. Verificar OpenCV con CUDA (10 min)
```bash
# Verificar que OpenCV esté compilado con CUDA
python3 -c "import cv2; print(cv2.getBuildInformation())" | grep -A 20 "CUDA"

# Si no tiene CUDA, pregunta al técnico/profesor
```

### 5. Probar PRIMERO en CPU (10 min)

```bash
# Asegurarte que ENABLE_CUDA esté comentado
grep "#define ENABLE_CUDA" main.cpp
# Debe mostrar: // #define ENABLE_CUDA

# Compilar
make clean && make

# Capturar métricas en CPU
./capture_metrics.sh cpu

# EN OTRA TERMINAL, mientras corre:
watch -n 1 htop  # Observar uso CPU
```

**ANOTAR RESULTADOS CPU:**
- FPS Promedio: ________
- Uso CPU: ________%
- RAM usada: ________

### 6. Probar en GPU (10 min)

```bash
# Descomentar ENABLE_CUDA en main.cpp (línea 12)
sed -i 's|// #define ENABLE_CUDA|#define ENABLE_CUDA|' main.cpp

# Verificar cambio
grep "#define ENABLE_CUDA" main.cpp
# Debe mostrar: #define ENABLE_CUDA (sin //)

# Recompilar
make clean && make

# Capturar métricas en GPU
./capture_metrics.sh gpu

# EN OTRA TERMINAL, mientras corre:
watch -n 1 nvidia-smi  # Observar uso GPU
```

**ANOTAR RESULTADOS GPU:**
- FPS Promedio: ________
- Uso GPU: ________%
- VRAM usada: ________ MB
- Temperatura GPU: ________ °C

### 7. Capturas de Pantalla Requeridas

- [ ] Screenshot: Programa corriendo en CPU con FPS visible
- [ ] Screenshot: `htop` mostrando uso de CPU
- [ ] Screenshot: Programa corriendo en GPU con FPS visible
- [ ] Screenshot: `nvidia-smi` mostrando uso de GPU
- [ ] Screenshot: Comparación visual lado a lado (opcional)

### 8. Grabar Videos (si es requerido)

```bash
# Usar OBS Studio, SimpleScreenRecorder, o Kazam
# - Video corto (30 segundos) en CPU
# - Video corto (30 segundos) en GPU
# - Mostrar FPS y métricas en pantalla
```

### 9. Copiar Resultados

```bash
# Comprimir todo
tar -czf resultados_1C_$(date +%Y%m%d).tar.gz metrics_* *.png *.mp4

# Copiar a pendrive o subir a Drive/GitHub
```

## PREGUNTAS PARA EL INFORME

### Análisis Cualitativo
- ¿Los resultados visuales son idénticos entre CPU y GPU?
- ¿Se observan diferencias en la calidad de detección de bordes?

### Análisis Cuantitativo
- Speedup GPU vs CPU: ________ x más rápido
- Tiempo promedio por frame:
  - CPU: ________ ms
  - GPU: ________ ms

### Reflexión
**¿Diferencia entre pipeline CPU↔GPU y GPU-only?**

*(Ver README.md para respuesta completa)*

**¿Cuándo vale la pena usar GPU?**

*(Ver README.md para respuesta completa)*

## PROBLEMAS COMUNES

### Error: "cannot open shared object file"
```bash
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
```

### Error: "CUDA not found"
```bash
# Verificar que OpenCV tenga CUDA
python3 -c "import cv2; print(cv2.cuda.getCudaEnabledDeviceCount())"
# Debe devolver > 0
```

### Error: Cámara no disponible
```bash
# Cambiar en main.cpp línea 34:
VideoCapture cap("ruta/a/video.mp4");  // En lugar de cap(0)
```

## TIEMPO ESTIMADO TOTAL
- Verificación: 5 min
- Setup: 10 min
- Pruebas CPU: 10 min
- Pruebas GPU: 10 min
- Capturas: 10 min
- Contingencia: 10 min
**TOTAL: ~55 minutos**

---

**Última revisión:** 8 de enero de 2026
