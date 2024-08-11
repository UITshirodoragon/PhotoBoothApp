


# import cv2
# from picamera2 import Picamera2, Preview
# import time


# camera = Picamera2()
# camera.preview_configuration.main.size = (640,480)
# camera.preview_configuration.main.format = "RGB888"
# camera.preview_configuration.align()
# camera.configure("preview")

# camera.start_preview(Preview.QT)

# camera.start()

# time.sleep(60)

# camera.stop_preview()
# camera.stop()


# while True:
#     frame = camera.capture_array()
#     cv2.imshow("camera",frame)
#     if cv2.waitKey(1) == ord("q"):
#         break

# camera.stop()
# cv2.destroyAllWindows()
        


import cv2
from picamera2 import Picamera2
import tkinter as tk
from PIL import Image, ImageTk

camera = Picamera2()
camera.preview_configuration.main.size = (1024, 600)
camera.preview_configuration.main.format = "XRGB8888"
camera.preview_configuration.align()
camera.configure("preview")
camera.start()

root = tk.Tk()
label = tk.Label(root)
label.pack()

def update_frame():
    frame = camera.capture_array("main")
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(frame_rgb)
    image_tk = ImageTk.PhotoImage(image)
    label.imgtk = image_tk
    label.configure(image=image_tk)
    root.after(1, update_frame)

update_frame()
root.mainloop()

camera.stop()