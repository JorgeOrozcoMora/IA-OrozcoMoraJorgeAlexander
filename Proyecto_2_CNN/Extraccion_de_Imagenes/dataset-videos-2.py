import cv2
import os

video_path = "C:/Users/jo296/Documents/IA/Proyecto2/videos/Impressive close-ups of Gorillas in a forest and Zoo - 8k [Ultra HD].mp4"
cap = cv2.VideoCapture(video_path)

# 📁 Carpeta de salida
output_folder = "C:/Users/jo296/Documents/IA/Proyecto2/dataset2/dataset"
os.makedirs(output_folder, exist_ok=True)

fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration = total_frames / fps

delay = int(1000 / fps)

speed = 1
frame_id = 0
paused = False

# ROI
drawing = False
ix, iy, fx, fy = -1, -1, -1, -1
roi_selected = False

def draw_rectangle(event, x, y, flags, param):
    global ix, iy, fx, fy, drawing, roi_selected

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            fx, fy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        fx, fy = x, y
        roi_selected = True
        print(f"ROI: ({ix},{iy}) → ({fx},{fy})")

# Slider tipo barra de progreso
def set_frame(pos):
    cap.set(cv2.CAP_PROP_POS_FRAMES, pos)

cv2.namedWindow("Video")
cv2.setMouseCallback("Video", draw_rectangle)
cv2.createTrackbar("Progreso", "Video", 0, total_frames, set_frame)

while cap.isOpened():

    if not paused:
        ret, frame = cap.read()
        if not ret:
            break
    else:
        ret, frame = True, frame  # mantener frame actual

    display_frame = frame.copy()

    # Dibujar ROI
    if drawing or roi_selected:
        cv2.rectangle(display_frame, (ix, iy), (fx, fy), (0, 255, 0), 2)

    # 📊 Tiempo tipo YouTube
    current_frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
    current_time = current_frame / fps

    text = f"{int(current_time)//60:02d}:{int(current_time)%60:02d} / {int(duration)//60:02d}:{int(duration)%60:02d} | x{speed}"
    cv2.putText(display_frame, text, (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # Actualizar barra
    cv2.setTrackbarPos("Progreso", "Video", current_frame)

    cv2.imshow("Video", display_frame)

    key = cv2.waitKey(int(delay / speed)) & 0xFF

    if key == ord('q'):
        break

    # ▶️ / ⏸️
    elif key == ord(' '):
        paused = not paused

    # ⏩ / ⏪ tipo YouTube (flechas)
    elif key == 83:  # derecha
        cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame + fps * 5)
    elif key == 81:  # izquierda
        cap.set(cv2.CAP_PROP_POS_FRAMES, max(0, current_frame - fps * 5))

    # ⚡ Velocidad
    elif key == ord('2'):
        speed = 2
    elif key == ord('4'):
        speed = 4
    elif key == ord('1'):
        speed = 1

    # 💾 Guardar ROI
    elif key == ord('s') and roi_selected:
        x1, x2 = sorted([ix, fx])
        y1, y2 = sorted([iy, fy])
        roi = frame[y1:y2, x1:x2]

        roi_resized = cv2.resize(roi, (28, 28))

        filename = os.path.join(output_folder, f"changos_7_{frame_id:05d}.jpg")
        cv2.imwrite(filename, roi_resized)

        print(f"Guardado: {filename}")
        frame_id += 1

cap.release()
cv2.destroyAllWindows()