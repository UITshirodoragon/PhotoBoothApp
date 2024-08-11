import cv2
from picamera2 import Picamera2
import tkinter as tk
from PIL import Image, ImageTk

camera = Picamera2()
camera.preview_configuration.main.size = (1024, 600)
camera.preview_configuration.main.format = "RGB888"
camera.preview_configuration.align()
camera.configure("preview")
camera.start()

root = tk.Tk()
label = tk.Label(root)
label.pack()

def update_frame():
    frame = camera.capture_array("main")
    image = Image.fromarray(frame)
    image_tk = ImageTk.PhotoImage(image)
    label.imgtk = image_tk
    label.configure(image=image_tk)
    root.after(1, update_frame)

update_frame()
root.mainloop()

camera.stop()





# back-end cv2