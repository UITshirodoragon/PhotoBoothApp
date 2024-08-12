import platform
import cv2
from picamera2 import Picamera2
import libcamera
from PIL import Image, ImageTk
import time
import numpy


# This class is responsible for controlling image capture
class Image_Capture_Controller:
    # constuctor for init the controller in each interface
    def __init__(self):
        # images are named and identified by numbers
        self.Captured_numbers = 1
        self.camera_ready_state = True
        try:
            # camera state is ready or not
            self.camera_ready_state = True
            # detect right platform 
            if platform.system() == 'Windows':
                # Choose and init camera from CV
                self.CVcamera = cv2.VideoCapture(0) 
                
            elif platform.system() == 'Linux': 
                
                # init camera from Picamera2
                self.Picamera = Picamera2()
                # preview_config = self.Picamera.create_preview_configuration()
                # capture_config = self.Picamera.create_preview_configuration(lores= {"size" : (1024, 600), "format" : "RGB888"}, main= {"size" : (2592,1944), "format" : "RGB888"}, display="lores")
                
                # self.Picamera.preview_configuration.sensor.output_size = (2560, 1500)
                # self.Picamera.preview_configuration.sensor.bit_depth = 10
                # self.Picamera.preview_configuration.enable_raw()
                # self.Picamera.preview_configuration.raw.size = (2560,1500)
                # self.Picamera.preview_configuration.format = "SBGGR10"
                self.Picamera.preview_configuration.main.size = (2592, 1944) # set size for preview
                self.Picamera.preview_configuration.main.format = "RGB888" # set format color
                
                self.Picamera.preview_configuration.align() # set align
                self.Picamera.preview_configuration.enable_lores()
                self.Picamera.preview_configuration.lores.size = (1024, 768)
                self.Picamera.preview_configuration.lores.format = "RGB888"
                self.Picamera.preview_configuration.align()
                
                self.Picamera.configure("preview") # configuration for preview
                
                self.Picamera.start() # start Pi

            
        except Exception as e:
            print(f"Error: {e}")    
            # camera is not ready when it doesn't init before
            self.camera_ready_state = False
        
    # destructor for controller    
    def __del__(self):
        # detect right platform
        if platform.system() == 'Linux':
            self.Picamera.close() #close camera when it have no use
            
        elif platform.system() == 'Windows':
            pass

    # get preview frame form camera
    def preview_frame(self):
        global image_Tk
        
        try:
            # detec
            if platform.system() == 'Windows':
                
                frame = self.CVcamera.read() # Get frame from camera
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA) #Convert color system
                
                img = Image.fromarray(frame)
                # .resize((1024,600)) # transfer an array to img
                image_Tk = ImageTk.PhotoImage(image=img)
                return image_Tk
                
            elif platform.system() == 'Linux':
                
                frame = self.Picamera.capture_array("lores")
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
                frame = cv2.flip(frame, 1)
                img = Image.fromarray(frame)
                
                # img = self.Picamera.capture_image("lores")
                image_Tk = ImageTk.PhotoImage(image = img)
                return image_Tk
                
            else:
                raise Exception("Hệ điều hành không được hỗ trợ.")
                 
        except Exception as e:
            # thay the bang log sau
            print(f"Lỗi: {e}")  
            
    
    def capture_and_save_image(self):
        
        try:
            
            if platform.system() == 'Windows':
                
                image = self.CVcamera.read()
                cv2.imwrite(f'DataStorage/ImageGallery/image{self.Captured_numbers}.png', image)
                
            elif platform.system() == 'Linux':
                
                image = self.Picamera.capture_array("main")
                # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
                image = cv2.flip(image, 1)
                cv2.imwrite(f'DataStorage/ImageGallery/image{self.Captured_numbers}.png', image)
                # self.Picamera.capture_file(f'DataStorage/ImageGallery/image{self.Captured_numbers}.png')     
        
        except Exception as e:
            # thay the bang log sau
            print(f"Lỗi: {e}") 
        self.Captured_numbers += 1
    
    

