import os

carpeta = "C:/Users/jo296/Documents/IA/Proyecto2/dataset2/ranas"

archivos = sorted(os.listdir(carpeta))

for i, nombre in enumerate(archivos, start=1):
    if nombre.lower().endswith((".jpg", ".png", ".jpeg")):
        extension = os.path.splitext(nombre)[1]
        
        nuevo_nombre = f"ranas_{i}{extension}"
        
        os.rename(
            os.path.join(carpeta, nombre),
            os.path.join(carpeta, nuevo_nombre)
        )