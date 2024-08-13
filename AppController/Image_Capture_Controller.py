
import platform
import cv2
try:
    if platform.system() == "Linux":
        from picamera2 import Picamera2
        import libcamera
    elif platform.system() == "Windows":
        pass
except ImportError as e:
    print(f"Lỗi {e}")
import customtkinter as ctk
from PIL import Image, ImageTk
import time
import numpy


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
        self.just_captured_image_path = None
        
        try:
            # camera state is ready or not
            self.camera_ready_state = True
            # detect right platform 
            if platform.system() == 'Windows':
                # Choose and init camera from CV
                self.CVcamera = cv2.VideoCapture(0) 
                self.nw_adjust_position_y = 0
                
            elif platform.system() == 'Linux': 
                
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

    def capture_and_update_gallery(self):
        if self.capture_screen.is_captured_yet:
                self.capture_screen.is_captured_yet = False
                #Enable capture button
                self.capture_screen.capture_button.configure(state = 'normal', command = self.capture_and_update_gallery)
                self.capture_screen.gallery_button.configure(state = 'normal', command = self.capture_screen.go_to_gallery)
                self.capture_screen.camera_configuration.toggle_button.configure(state = 'normal', command = self.capture_screen.camera_configuration.Toggle_Slide)
                self.capture_screen.Return_start_screen_button.configure(state = 'normal', command = self.capture_screen.back_to_start_screen)
                captured_image_path = self.just_captured_image_path
                imageTk = ImageTk.PhotoImage(Image.open(captured_image_path).resize(((int(self.capture_screen.parent.winfo_width() * 0.6),
                                                                                     int(self.capture_screen.parent.winfo_height() * 43 / 60)))))
                captured_image_button = ctk.CTkButton(self.capture_screen.gallery.captured_images_frame,
                                                        text ='',
                                                        width = int(self.capture_screen.parent.winfo_width() * 3 / 32),
                                                        height=int(self.capture_screen.parent.winfo_height() * 5 / 48),
                                                        bg_color='transparent',
                                                        fg_color='transparent',
                                                        hover_color='gray',
                                                        image=ctk.CTkImage(light_image=Image.open(captured_image_path),
                                                                                dark_image=Image.open(captured_image_path),
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
                self.capture_screen.gallery.controller.list_Image.append(Image.open(captured_image_path))
                self.capture_screen.gallery.controller.list_image_button.append(captured_image_button)
                self.capture_screen.gallery.controller.image_number += 1
                self.capture_screen.gallery.gallery_images_update()
        else:
                #Disable capture button
                self.capture_screen.capture_button.configure(state = 'disable', command = None)
                self.capture_screen.gallery_button.configure(state = 'disable', command = None)
                self.capture_screen.camera_configuration.toggle_button.configure(state = 'disable', command = None)
                self.capture_screen.Return_start_screen_button.configure(state = 'disable', command = None)
                if self.capture_screen.camera_configuration.at_start_position == False:
                        self.capture_screen.camera_configuration.Toggle_Slide()
                #Capture
                self.capture_screen.Countdown()
                #Wait for image is captured then update gallery
                self.capture_screen.gallery.after(int((self.capture_screen.countdown_time + 0.5) * 1000), self.capture_and_update_gallery)
    
    # get preview frame form camera  
    def preview_frame(self):
        global image_Tk
        # time_start = time.time()
        try:
            # detec
            if platform.system() == 'Windows':
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
                
            elif platform.system() == 'Linux':
                
                frame = self.Picamera.capture_array("lores")
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
                frame = cv2.flip(frame, 1)
                img = Image.fromarray(frame)
                
                # img = self.Picamera.capture_image("lores")
                image_Tk = ImageTk.PhotoImage(image = img)
                # time_end = time.time()
                # time_loop = time_end - time_start
                # self.fps_realtime = .9 * self.fps_realtime + .1 * (1 / time_loop) 
                return image_Tk
                
            else:
                raise Exception("Hệ điều hành không được hỗ trợ.")
                 
        except Exception as e:
            # thay the bang log sau
            print(f"Lỗi: {e}")  
        
    
    def capture_and_save_image(self):
        
        try:
            
            if platform.system() == 'Windows':
                
                _, image = self.CVcamera.read()
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
    
    
    
    
    