import cv2

class CameraNode:
    def __init__(self):
        # Kamera yerine bir video dosyasından akış alıyoruz
        self.cap = cv2.VideoCapture('/path/to/test/video.mp4')  # Gerçek kameraya bağlı değilseniz bu şekilde simüle edebilirsiniz.

    def capture_frame(self):
        ret, frame = self.cap.read()
        if ret:
            # Video kaynağını işler
            print("Kamera akışı alınmaya devam ediyor.")
        else:
            print("Kamera akışı hatası")

