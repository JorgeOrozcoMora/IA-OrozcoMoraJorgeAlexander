import cv2
import os

video_path = "YTDown.com_YouTube_Whale-Paradise-4K-1HR-Underwater-Ambient_Media_UWETFUNy_iI_002_720p.mp4"
output_folder = "dataset/ballenas"
os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)

paused = False
frame_actual = None
frame_count = 0

def guardar_frame(event, x, y, flags, param):
    global frame_actual, frame_count
    
    if event == cv2.EVENT_LBUTTONDOWN:
        if frame_actual is not None:
            filename = f"{output_folder}/ballenas_{frame_count}.jpg"
            cv2.imwrite(filename, frame_actual)
            print(f"Frame guardado: {filename}")

cv2.namedWindow("Video")
cv2.setMouseCallback("Video", guardar_frame)

while True:
    if not paused:
        ret, frame = cap.read()
        if not ret:
            break
        frame_actual = frame.copy()
        frame_count = int(cap.get(cv2.CAP_PROP_POS_FRAMES))

    cv2.imshow("Video", frame_actual)

    key = cv2.waitKey(30) & 0xFF

    if key == 27:  # ESC
        break
    elif key == 32:  # ESPACIO
        paused = not paused

cap.release()
cv2.destroyAllWindows()