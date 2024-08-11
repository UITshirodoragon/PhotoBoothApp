import picamera

class ImageCaptureController:
    def __init__(self):
        self.camera = picamera.PiCamera()
        self.flash_led = False
        self.capture_mode = False

    def __del__(self):
        self.camera.close()

    def startPreview(self):
        self.camera.start_preview()

    def stopPreview(self):
        self.camera.stop_preview()

    def captureImage(self, filename="image.jpg"):
        self.camera.capture(filename)

# Ví dụ sử dụng:
controller = ImageCaptureController()
controller.startPreview()  # Bắt đầu xem trước
controller.captureImage("my_image.jpg")  # Chụp ảnh và lưu vào file
controller.stopPreview()  # Dừng xem trước
