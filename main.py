import cv2
from roboflow import Roboflow

print("Loading Roboflow workspace...")
rf = Roboflow(api_key="rsNruwjIJiOeOz5v6Kvu")
project = rf.workspace("apalahnamanya-ahgjp").project("bisindo-tugas-besar-psi")
model = project.version(3).model

def predict_frame_with_roboflow(frame):
    resized = cv2.resize(frame, (640, 640))
    response = model.predict(resized, confidence=15, overlap=30).json()
    
    predictions = response["predictions"]
    
    for pred in predictions:
        x, y = int(pred["x"]), int(pred["y"])
        w, h = int(pred["width"]), int(pred["height"])
        label = pred["class"]
        conf = pred["confidence"]

        scale_x = frame.shape[1] / 640
        scale_y = frame.shape[0] / 640

        x = int(x * scale_x)
        y = int(y * scale_y)
        w = int(w * scale_x)
        h = int(h * scale_y)

        cv2.rectangle(frame, (x - w//2, y - h//2), (x + w//2, y + h//2), (0, 255, 0), 2)
        cv2.putText(frame, f"{label} ({conf:.2f})", (x - w//2, y - h//2 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (94, 98, 245), 2)

    return frame

cap = cv2.VideoCapture(0)
print("Tekan 'q' untuk keluar...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = predict_frame_with_roboflow(frame)
    cv2.imshow("Isyarat Tangan - Roboflow", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()