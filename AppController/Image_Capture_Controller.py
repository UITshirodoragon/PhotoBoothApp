
import platform as osplatform
import cv2
try:
    if osplatform.system() == "Linux":
        from picamera2 import Picamera2
        import libcamera
    elif osplatform.system() == "Windows":
        pass
except ImportError as e:
    print(f"Lỗi {e}")
import customtkinter as ctk
from PIL import Image, ImageTk
import time
import numpy
import threading

time_start = time.time()
frame_count = 0

# This class is responsible for controlling image capture
class Image_Capture_Controller():
    # constuctor for init the controller in each interface
    def __init__(self, capture_screen):
    
        # images are named and identified by numbers
        self.Captured_numbers = 1
        self.camera_ready_state = True
        self.nw_adjust_position_x = None
        self.nw_adjust_position_y = None
        self.capture_screen = capture_screen
        self.is_captured_yet = False
        self.just_captured_image_path = f'DataStorage/ImageGallery/image{self.Captured_numbers}.png'
        self.fps_realtime = 0
        
        self.countdown_time = 3
        self.countdown_time_temp = self.countdown_time
        try:
            # camera state is ready or not
            self.camera_ready_state = True
            # detect right osplatform 
            if osplatform.system() == 'Windows':
                # Choose and init camera from CV
                self.CVcamera = cv2.VideoCapture(0) 
                self.nw_adjust_position_y = 0
                
            elif osplatform.system() == 'Linux': 
                
                # init camera from Picamera2
                self.Picamera = Picamera2()

                self.nw_adjust_position_y = -84
                # preview_config = self.Picamera.create_preview_configuration()
                # capture_config = self.Picamera.create_preview_configuration(lores= {"size" : (1024, 600), "format" : "RGB888"}, main= {"size" : (2592,1944), "format" : "RGB888"}, display="lores")
                
                # self.Picamera.preview_configuration.sensor.output_size = (2560, 1500)
                # self.Picamera.preview_configuration.sensor.bit_depth = 10
                # self.Picamera.preview_configuration.enable_raw()
                # self.Picamera.preview_configuration.raw.size = (2560,1500)
                # self.Picamera.preview_configuration.format = "SBGGR10"
                self.Picamera.preview_configuration.main.size = (1024, 768) # set size for preview
                self.Picamera.preview_configuration.main.format = "BGR888" # set format color
                self.Picamera.still_configuration.main.size = (2592,1944)
                self.Picamera.still_configuration.main.format = "XRGB8888"
                # self.Picamera.preview_configuration.align() # set align
                # self.Picamera.preview_configuration.enable_lores()
                # self.Picamera.preview_configuration.lores.size = (1024, 768)
                # self.Picamera.preview_configuration.lores.format = "BGR888"
                self.Picamera.preview_configuration.align()
                self.Picamera.still_configuration.align()
                
                # self.preview_config = self.Picamera.preview_configuration_
                # self.still_config = self.Picamera.still_configuration_
                
                self.Picamera.configure("preview") # configuration for preview
                
                                            #'Sharpness': 1.0, # (0.0, 16.0, 1.0)
                                            #'ExposureValue': 0.0, #(-8.0, 8.0, 0.0)
                                            #'AeConstraintMode': 0, #(0, 3, 0)
                                            #'ScalerCrop': (0, 0, 2592, 1944), # ((0, 0, 130, 98), (0, 0, 2592, 1944), (0, 0, 2592, 1944))
                                            #'AnalogueGain': 1.0, #(1.0, 63., None)
                                            #'NoiseReductionMode': 0, #(0, 4, 0)
                                            #'AeMeteringMode': 0, #(0, 3, 0)
                                            #'ExposureTime': 33333, #(92, 760636, None)
                                            #'HdrMode': 1, #(0, 4, 0)
                                            #'AwbEnable': False, #(False, True, None)
                                            #'Saturation': 1.0, #(0.0, 32.0, 1.0)
                                            #'Contrast': 1.0, #(0.0, 32.0, 1.0)
                                            #'ColourGains': 1.0, #(0.0, 32.0, None)
                                            #'Brightness': 1.0, #(-1.0, 1.0, 0.0)
                                            #'FrameDurationLimits': 23123,# (23123, 760729, None)
                                            #'AeFlickerPeriod': 10000, #(100, 1000000, None)
                                            #'AwbMode': 0, #(0, 7, 0)
                                            #'AeFlickerMode': 0, #(0, 1, 0)
                                            #'AeExposureMode': 0, #(0, 3, 0)
                                            #'StatsOutputEnable': 0, #(False, True, False)
                                            #'AeEnable': False #(False, True, None)
                
                self.Picamera.set_controls({'Brightness': 0.05, 'Sharpness': 1.0})
                
                self.Picamera.start() # start Pi

            
        except Exception as e:
            print(f"Error: {e}")    
            # camera is not ready when it doesn't init before
            self.camera_ready_state = False
        

    
    # destructor for controller    
    def __del__(self):
        # detect right osplatform
        if osplatform.system() == 'Linux':
            self.Picamera.close() #close camera when it have no use
            
        elif osplatform.system() == 'Windows':
            pass

    
    
    # get preview frame form camera  
    def preview_image(self):
        global image_Tk
        global time_start, frame_count
        
        
        try:
            # detec
            if osplatform.system() == 'Windows':
                _, frame = self.CVcamera.read() # Get frame from camera
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA) #Convert color system
                frame_array = frame
                #img = Image.fromarray(frame_array).resize((self.parent.winfo_width(), self.parent.winfo_height())) # transfer an array to img
                # image_Tk = ImageTk.PhotoImage(image=img)
                #frame = self.CVcamera.read() # Get frame from camera
                #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA) #Convert color system
                img = Image.fromarray(frame_array).resize((1024,768)) # transfer an array to img
                image_Tk = ImageTk.PhotoImage(image=img)
                return image_Tk
                
            elif osplatform.system() == 'Linux':
                
                frame = self.Picamera.capture_array("main")
                
                ##frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
                frame = cv2.flip(frame, 1)
               
                img = Image.fromarray(frame)
                
                image_Tk = ImageTk.PhotoImage(image = img)
                # time_end = time.time()
                # time_loop = time_end - time_start
                # self.fps_realtime = .9 * self.fps_realtime + .1 * (1 / time_loop)
                frame_count += 1
                elapsed_time = time.time() - time_start
                if elapsed_time >= 1.0:
                    self.fps_realtime = frame_count / elapsed_time
                    time_start = time.time()
                    frame_count = 0
                return image_Tk
                
            else:
                raise Exception("Hệ điều hành không được hỗ trợ.")
                 
        except Exception as e:
            # thay the bang log sau
            print(f"Lỗi: {e}")  
        
    
    def capture_and_save_image(self):
        
        try:
            
            if osplatform.system() == 'Windows':
                
                _, image = self.CVcamera.read()
                cv2.imwrite(self.just_captured_image_path, image)
                
            elif osplatform.system() == 'Linux':
                
                # image = self.Picamera.capture_array("main")
                image_job = self.Picamera.switch_mode_and_capture_array(camera_config="still",
                                                                         name= "main",
                                                                         wait= False)
                
                # Nhận ảnh
                image = self.Picamera.wait(image_job)
                # image = self.Picamera.switch_mode_and_capture_array(camera_config="still",
                                                                        # name= "main")
                # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
                image = cv2.flip(image, 1)
                cv2.imwrite(self.just_captured_image_path, image)
                # self.Picamera.capture_file(f'DataStorage/ImageGallery/image{self.Captured_numbers}.png')     
        
        except Exception as e:
            # thay the bang log sau
            print(f"Lỗi: {e}") 
        self.Captured_numbers += 1
        self.is_captured_yet = True
     
        
    def update_image_to_gallery(self):
        
        self.capture_screen.gallery.controller.list_Image.append(Image.open(self.just_captured_image_path))
        self.capture_screen.gallery.controller.list_image_paths.append(self.just_captured_image_path)
        imageTk = ImageTk.PhotoImage(Image.open(self.just_captured_image_path).resize(((int(self.capture_screen.parent.winfo_width() * 0.6),
                                                                                int(self.capture_screen.parent.winfo_height() * 43 / 60)))))
        captured_image_button = ctk.CTkButton(self.capture_screen.gallery.captured_images_frame,
                                                text ='',
                                                width = int(self.capture_screen.parent.winfo_width() * 3 / 32),
                                                height=int(self.capture_screen.parent.winfo_height() * 5 / 48),
                                                bg_color='transparent',
                                                fg_color='transparent',
                                                hover_color='gray',
                                                image=ctk.CTkImage(light_image=Image.open(self.just_captured_image_path),
                                                                        dark_image=Image.open(self.just_captured_image_path),
                                                                        size = ((int(self.capture_screen.parent.winfo_width() * 0.15)),
                                                                                int(self.capture_screen.parent.winfo_height() / 6))),
                                                command = lambda : self.capture_screen.gallery.image_is_chosen(imageTk))
        check_button = ctk.CTkCheckBox(captured_image_button,
                                        text = '',
                                        width = 15,
                                        height= 15,
                                        onvalue= 1,
                                        offvalue= 0,
                                        command = lambda index = self.capture_screen.gallery.controller.image_number: self.capture_screen.gallery.controller.export_image(index))
        check_button.place(relx = 1, rely = 1, anchor = 'se')
        self.capture_screen.gallery.controller.list_export_image_check_button.append(check_button)
        self.capture_screen.gallery.controller.list_Image.append(Image.open(self.just_captured_image_path))
        self.capture_screen.gallery.controller.list_image_button.append(captured_image_button)
        self.capture_screen.gallery.controller.image_number += 1
        self.capture_screen.gallery.gallery_images_update()
        self.just_captured_image_path = f'DataStorage/ImageGallery/image{self.Captured_numbers}.png'
    
    
        

    
    
    