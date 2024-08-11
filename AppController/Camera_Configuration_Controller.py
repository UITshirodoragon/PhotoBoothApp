class CameraConfigurationController:
    def __init__(self, resolution, framerate, brightness=0.5, contrast=0.5, saturation=0.5, sharpness=0.5,
                 expose_mode="auto", awb_mode="auto", zoom=1.0, image_effect="none", ISO=100, shutter_speed=1/125, drc_strength=0):
        self.resolution = resolution
        self.framerate = framerate
        self.brightness = brightness
        self.contrast = contrast
        self.saturation = saturation
        self.sharpness = sharpness
        self.expose_mode = expose_mode
        self.awb_mode = awb_mode
        self.zoom = zoom
        self.image_effect = image_effect
        self.ISO = ISO
        self.shutter_speed = shutter_speed
        self.drc_strength = drc_strength

class ImageCaptureController:
    def __init__(self, camera_config):
        self.camera_config = camera_config
        self.flash_led = False
        self.capture_mode = "single"

    def take_picture(self):
        # Logic để chụp ảnh dựa trên các thông số cấu hình
        print(f"Chụp ảnh với độ phân giải: {self.camera_config.resolution}, khẩu độ: {self.camera_config.aperture}...")
        # ... thêm các lệnh để thực hiện việc chụp ảnh ...
