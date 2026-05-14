import os
import random

dataset_path = 'C:/Users/jo296/Documents/IA/Proyecto2/dataset'
target = 9000

classes = [c for c in os.listdir(dataset_path) if os.path.isdir(os.path.join(dataset_path, c))]

for clase in classes:
    class_path = os.path.join(dataset_path, clase)

    # 🔥 Acepta más extensiones
    images = [
        img for img in os.listdir(class_path)
        if img.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.bmp'))
    ]

    current = len(images)
    print(f'\nClase: {clase}')
    print(f'Imágenes encontradas: {current}')

    if current > target:
        to_delete = current - target
        print(f'Eliminando {to_delete} imágenes...')

        delete_images = random.sample(images, to_delete)

        for img in delete_images:
            try:
                os.remove(os.path.join(class_path, img))
            except Exception as e:
                print(f'Error eliminando {img}: {e}')

        print('✔ Eliminación terminada')

    elif current < target:
        print(f'⚠ Solo hay {current}, faltan {target - current}')

    else:
        print('✔ Ya está en 9000')

print('\n🔥 Proceso terminado')