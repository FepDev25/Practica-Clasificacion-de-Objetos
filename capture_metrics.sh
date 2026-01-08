#!/bin/bash

# Script para capturar métricas en el laboratorio
# Uso: ./capture_metrics.sh [cpu|gpu]

MODE=$1

if [ -z "$MODE" ]; then
    echo "Uso: ./capture_metrics.sh [cpu|gpu]"
    exit 1
fi

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
OUTPUT_DIR="metrics_${MODE}_${TIMESTAMP}"
mkdir -p "$OUTPUT_DIR"

echo "==================================="
echo "CAPTURANDO MÉTRICAS - MODO: $MODE"
echo "==================================="

# Capturar información del sistema
echo "📊 Información del sistema..."
{
    echo "=== FECHA Y HORA ==="
    date
    echo ""
    echo "=== INFORMACIÓN CPU ==="
    lscpu | grep -E "Model name|CPU\(s\)|Thread|Core|Socket"
    echo ""
    echo "=== MEMORIA RAM ==="
    free -h
    echo ""
} > "$OUTPUT_DIR/system_info.txt"

# Capturar Mac Address
echo "🔍 Mac Address..."
ip link show | grep -A 1 "state UP" | grep ether > "$OUTPUT_DIR/mac_address.txt"

# Si es modo GPU, capturar info de NVIDIA
if [ "$MODE" == "gpu" ]; then
    echo "🎮 Información GPU..."
    {
        echo "=== NVIDIA SMI ==="
        nvidia-smi
        echo ""
        echo "=== CUDA VERSION ==="
        nvcc --version 2>/dev/null || echo "nvcc no disponible"
    } > "$OUTPUT_DIR/gpu_info.txt"
    
    # Iniciar monitoreo continuo de GPU en segundo plano
    echo "🔄 Iniciando monitoreo continuo de GPU..."
    nvidia-smi dmon -s u -c 100 -d 1 > "$OUTPUT_DIR/gpu_monitor.txt" 2>&1 &
    MONITOR_PID=$!
    echo "Monitor PID: $MONITOR_PID"
fi

# Instrucciones
echo ""
echo "✅ Sistema preparado para captura"
echo "📁 Directorio: $OUTPUT_DIR"
echo ""
echo "🎬 AHORA:"
echo "   1. Ejecuta: ./vision_app"
echo "   2. Deja correr por ~30 segundos"
echo "   3. Presiona ESC para salir"
echo "   4. Presiona Enter aquí cuando termines"
echo ""
read -p "Presiona Enter cuando hayas terminado la prueba..."

# Detener monitor si estaba corriendo
if [ "$MODE" == "gpu" ]; then
    kill $MONITOR_PID 2>/dev/null
fi

# Capturar estado final
echo "📸 Capturando estado final del sistema..."
{
    echo "=== ESTADO FINAL ==="
    date
    echo ""
    if [ "$MODE" == "gpu" ]; then
        nvidia-smi
    else
        free -h
    fi
} >> "$OUTPUT_DIR/system_info.txt"

echo ""
echo "✅ Captura completa!"
echo "📂 Resultados guardados en: $OUTPUT_DIR/"
echo ""
echo "📋 Archivos generados:"
ls -lh "$OUTPUT_DIR/"
