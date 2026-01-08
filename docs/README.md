# PARTE 1C - OpenCV C++ CPU vs GPU

## Estado Actual

✅ **Compilación local (sin GPU) funcionando correctamente**

## Compilar y Ejecutar

### Opción 1: Makefile (Recomendado)

```bash
make clean
make
./vision_app
```

### Opción 2: CMake

```bash
mkdir -p build
cd build
cmake ..
make
./vision_app
```

## Configuración para el Laboratorio

### Cuando estés en la PC con GPU NVIDIA:

1. **Abrir [main.cpp](main.cpp#L12) y descomentar la línea 12:**
   ```cpp
   #define ENABLE_CUDA  // Quitar el // del inicio
   ```

2. **Actualizar el CMakeLists.txt** para incluir módulos CUDA:
   - Después de `find_package(OpenCV REQUIRED)`, verificar que OpenCV tenga soporte CUDA
   - O usar el Makefile agregando las librerías CUDA manualmente

3. **Verificar instalación CUDA:**
   ```bash
   nvidia-smi  # Debe mostrar la GPU
   nvcc --version  # Verificar versión de CUDA
   ```

4. **Recompilar:**
   ```bash
   make clean && make
   ```

## Estructura del Código

### Pipeline GPU-Only (Eficiente)

```
CPU: cap.read(frame)
  ↓
GPU: d_frame.upload(frame)          # Única transferencia CPU→GPU
  ↓
GPU: cvtColor → Gaussian → Equalize → Erode → Canny  # Todo en VRAM
  ↓
GPU: d_edges.download(result)        # Única transferencia GPU→CPU
  ↓
CPU: imshow(result)
```

### Operaciones Implementadas

1. ✅ **Conversión a escala de grises** (`cvtColor`)
2. ✅ **Filtro Gaussiano** (5x5, σ=1.5)
3. ✅ **Ecualización de histograma** (`equalizeHist`)
4. ✅ **Erosión morfológica** (kernel 3x3)
5. ✅ **Detección de bordes Canny** (50, 150)

## Métricas a Capturar en el Laboratorio

### Durante ejecución en CPU:

- [ ] Captura de pantalla con FPS
- [ ] Tiempo de procesamiento promedio
- [ ] Uso de RAM (con `htop` o `top`)

### Durante ejecución en GPU:

- [ ] Captura de pantalla con FPS
- [ ] Salida de `nvidia-smi` mostrando uso de VRAM
- [ ] Tiempo de procesamiento promedio
- [ ] Comparación visual de resultados

## Comandos Útiles en el Laboratorio

```bash
# Ver información de la GPU
nvidia-smi

# Ver en tiempo real (actualiza cada 1 segundo)
watch -n 1 nvidia-smi

# Ver uso de CPU y RAM
htop

# Registrar Mac Address
ip link show | grep ether
```

## Notas Importantes

- **En tu PC local**: El código funciona solo con CPU (modo simulación)
- **En el laboratorio**: Descomentar `#define ENABLE_CUDA` para activar GPU
- El código está diseñado para minimizar transferencias CPU↔GPU
- Todos los filtros se inicializan **una sola vez** fuera del bucle

## Respuestas para el Informe

### ¿Diferencia entre pipeline CPU↔GPU y GPU-only?

**Pipeline CPU↔GPU** (Ineficiente):
```
CPU → GPU → CPU → GPU → CPU  // Múltiples transferencias
```

**Pipeline GPU-only** (Eficiente):
```
CPU → GPU → [operaciones] → CPU  // Solo 2 transferencias
```

### ¿Cuándo vale la pena usar GPU?

1. ✅ Videos en alta resolución (HD, 4K)
2. ✅ Procesamiento en tiempo real (>30 FPS requeridos)
3. ✅ Múltiples operaciones encadenadas
4. ✅ Batch processing de muchas imágenes
5. ❌ Imágenes pequeñas individuales (overhead de transferencia)
6. ❌ Una sola operación simple
