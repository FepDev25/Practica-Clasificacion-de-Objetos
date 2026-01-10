import os
import shutil
import random

# --- CONFIGURACIÓN ---
ORIGEN = "data" # Carpeta donde tienes train, valid, test originales
DESTINO_ROOT = "dataset_colab"

# Límites de imágenes por clase (Ajustado a lo que pediste)
LIMITES = {
    "train": 400,  # 400 por clase
    "valid": 50,   # 50 por clase
    "test": 50     # 50 por clase
}

# Palabras clave para detectar el archivo (basado en tus iniciales y nombres)
# Ajusta el "keyword" si el nombre del archivo es distinto (ej: 'c_01.jpg')
CLASES_KEYWORD = {
    "bitter": "bitter_melon", 
    "cucumber": "cucumber",
    "fig": "fig",
    "jujube": "jujube",
    "boyang": "melon_boyang", 
    "musk": "muskmelon"       
}

def preparar_dataset():
    if os.path.exists(DESTINO_ROOT):
        shutil.rmtree(DESTINO_ROOT)
    
    for split, limite in LIMITES.items():
        print(f"\nProcesando {split.upper()}...")
        
        # Rutas de origen para este split
        img_orig = os.path.join(ORIGEN, split, "images")
        lbl_orig = os.path.join(ORIGEN, split, "labels")
        
        if not os.path.exists(img_orig):
            print(f"saltando {split}, no existe la carpeta {img_orig}")
            continue

        # Crear carpetas de destino
        img_dest = os.path.join(DESTINO_ROOT, split, "images")
        lbl_dest = os.path.join(DESTINO_ROOT, split, "labels")
        os.makedirs(img_dest, exist_ok=True)
        os.makedirs(lbl_dest, exist_ok=True)

        todos_los_archivos = [f for f in os.listdir(img_orig) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]

        for key, nombre_clase in CLASES_KEYWORD.items():
            # Filtramos archivos que contengan el keyword (ej: 'fig' o 'f_')
            archivos_clase = [f for f in todos_los_archivos if key in f.lower()]
            
            # Si el nombre empieza con inicial, ej: 'f_01.jpg', esto también sirve
            if not archivos_clase:
                archivos_clase = [f for f in todos_los_archivos if f.lower().startswith(key[0])]

            # Selección aleatoria
            seleccionados = random.sample(archivos_clase, min(len(archivos_clase), limite))
            print(f"{nombre_clase}: {len(seleccionados)} imágenes copiadas.")

            for img_name in seleccionados:
                # Copiar Imagen
                shutil.copy(os.path.join(img_orig, img_name), os.path.join(img_dest, img_name))
                
                # Copiar Label (.txt)
                lbl_name = os.path.splitext(img_name)[0] + ".txt"
                if os.path.exists(os.path.join(lbl_orig, lbl_name)):
                    shutil.copy(os.path.join(lbl_orig, lbl_name), os.path.join(lbl_dest, lbl_name))

    # Crear el data.yaml para COLAB
    yaml_content = f"""
path: /content/dataset_colab
train: train/images
val: valid/images
test: test/images

nc: 6
names: ['bitter_melon', 'cucumber', 'fig', 'jujube', 'melon_boyang', 'muskmelon']
"""
    with open(os.path.join(DESTINO_ROOT, "data.yaml"), "w") as f:
        f.write(yaml_content.strip())
    print(f"\nProceso completado. Carpeta '{DESTINO_ROOT}' lista para comprimir.")

if __name__ == "__main__":
    preparar_dataset()