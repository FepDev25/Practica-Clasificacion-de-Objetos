import cv2
import time
import torch
import psutil
import platform
import uuid
from ultralytics import YOLO

# --- CONFIGURACIÓN ---
# En el lab, esto cambiará automáticamente a 'cuda:0'
DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'

def get_mac_address():
    mac = uuid.getnode()
    return ':'.join(('%012X' % mac)[i:i+2] for i in range(0, 12, 2))

# 1. CARGAR MODELO YOLO (Detección)
# Usamos 'yolov8n.pt' o 'yolo11n.pt' si ya salió. El 'n' es nano (rápido).
print(f"Cargando YOLO en {DEVICE}...")
model_yolo = YOLO('yolov8n.pt') 

# 2. CARGAR SUPER RESOLUCIÓN (Simulado o Real)
# Opción A (Fácil): Usar OpenCV DNN con un modelo EDSR/FSRCNN (descargar .pb aparte)
# Opción B (Pro): Usar RealESRGAN vía Torch (requiere instalar: pip install realesrgan)
# Para este script base, haremos una simulación de carga si no tienes la librería, 
# pero preparo el código para OpenCV DNN que es lo que pide la guía (C++ style logic).
sr = cv2.dnn_superres.DnnSuperResImpl_create()

# NOTA: Debes descargar el modelo "EDSR_x4.pb" o similar y ponerlo en la carpeta
# path_model = "EDSR_x4.pb"
# sr.readModel(path_model)
# sr.setModel("edsr", 4) 

cap = cv2.VideoCapture(0) # Webcam

# Variables para métricas
prev_frame_time = 0
new_frame_time = 0

print(f"Iniciando Benchmark en: {platform.node()}")
print(f"Mac Address: {get_mac_address()}")

while True:
    ret, frame = cap.read()
    if not ret: break

    # --- TAREA 1: DETECCIÓN (YOLO) ---
    # verbose=False para no llenar la terminal
    results = model_yolo(frame, device=DEVICE, verbose=False) 
    
    # Dibujar cajas
    annotated_frame = results[0].plot()

    # --- TAREA 2: SUPER RESOLUCIÓN ---
    # La guía pide comparar CPU vs GPU.
    # Si tienes el modelo cargado:
    # upscale_frame = sr.upsample(annotated_frame)
    
    # [TRUCO PARA TU CASA]
    # Si no tienes el modelo SR descargado aun, simularemos la carga computacional
    # redimensionando con bicúbica (gasta CPU) para probar el script.
    upscale_frame = cv2.resize(annotated_frame, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    # --- MÉTRICAS ---
    new_frame_time = time.time()
    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
    
    # Obtener uso de RAM
    ram_usage = psutil.virtual_memory().percent

    # [cite_start]Info en pantalla (Requisito [cite: 96, 98, 99])
    cv2.putText(annotated_frame, f"FPS: {int(fps)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(annotated_frame, f"Device: {DEVICE.upper()}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.putText(annotated_frame, f"RAM: {ram_usage}%", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.putText(annotated_frame, f"MAC: {get_mac_address()}", (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    cv2.imshow('Benchmark YOLO + SR', annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()