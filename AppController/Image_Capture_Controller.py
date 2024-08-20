
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
import cv2
import sys
import os
# Đường dẫn tới folder chứa module 
package_controller_path = os.path.abspath(os.path.join('..', 'PhotoBoothApp'))
if package_controller_path not in sys.path:
    sys.path.append(package_controller_path)
from AppInterface.define import *
from AppController import HandDetector as HD



time_start = time.time()
frame_count = 0

# This class is responsible for controlling image capture
class Image_Capture_Controller():
    # constuctor for init the controller in each interface
    def __init__(self, capture_screen):
    
        # images are named and identified by numbers
        self.capture_screen = capture_screen
        self.Captured_image_numbers = 1
        self.Captured_gif_numbers = 1
        self.gif_image_count = 0
        self.camera_ready_state = True
        self.nw_adjust_position_x = None
        self.nw_adjust_position_y = None
        self.is_captured_yet = False
        self.just_captured_image_path = f'DataStorage/ImageGallery/user{self.capture_screen.end_screen.controller.number_of_uses}/image{self.Captured_image_numbers}.png'
        self.just_captured_gif_path = f'DataStorage/GIFGallery/user{self.capture_screen.end_screen.controller.number_of_uses}/Gif{self.Captured_gif_numbers}.gif'
        self.fps_realtime = 0
        self.gif_mode = False
        self.countdown_time = 3
        self.countdown_time_temp = self.countdown_time
        self.is_capturing = False #variable for hand detector
        self.five_fingers_on = False #Check if 5 fingers are on to ready capture when user close their hand
        self.handDetector = HD.handDetector(detectionCon=0.75)
        #Load trained model
        self.net = cv2.dnn.readNetFromCaffe('DataStorage/models/deploy.prototxt.txt',
                                       'DataStorage/models/res10_300x300_ssd_iter_140000_fp16.caffemodel')
        self.list_gif_image = []
    
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
        global image_Tk, img
        global time_start, frame_count
        
        
        try:
            # detec
            if osplatform.system() == 'Windows':
                _, frame = self.CVcamera.read() # Get frame from camera
                if self.is_capturing == False:
                    self.hand_detected_capture(frame)
                    frame = self.face_detector(frame)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA) #Convert color system
                frame_array = cv2.flip(frame, 1)
                #img = Image.fromarray(frame_array).resize((self.parent.winfo_width(), self.parent.winfo_height())) # transfer an array to img
                # image_Tk = ImageTk.PhotoImage(image=img)
                #frame = self.CVcamera.read() # Get frame from camera
                #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA) #Convert color system
                img = Image.fromarray(frame_array).resize((1024,768)) # transfer an array to img
                image_Tk = ImageTk.PhotoImage(image = img)
                frame_count += 1
                elapsed_time = time.time() - time_start
                if elapsed_time >= 1.0:
                    self.fps_realtime = frame_count / elapsed_time
                    time_start = time.time()
                    frame_count = 0
                return image_Tk
                
            elif osplatform.system() == 'Linux':
                
                frame = self.Picamera.capture_array("main")
                
                ##frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
                frame = cv2.flip(frame, 1)
                # if self.is_capturing == False:
                #     self.hand_detected_capture(frame)
                #     frame = self.face_detector(frame)
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
            
        except Exception as e:
            # thay the bang log sau
            print(f"Lỗi: {e}")  
        
    
    def capture_and_save_image(self):   
        try:
            
            if osplatform.system() == 'Windows':
                
                _, image = self.CVcamera.read()
                image = cv2.flip(image, 1)
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
        self.Captured_image_numbers += 1
        self.is_captured_yet = True
     
    def capture_and_save_gif(self):
        try:    
            if osplatform.system() == 'Windows':
                _, image = self.CVcamera.read()
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
        except Exception as e:
            
            # thay the bang log sau
            print(f"Lỗi: {e}") 

        if self.gif_image_count < 150:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(image)
            self.list_gif_image.append(img)
            self.gif_image_count += 1
            self.capture_screen.capture_frame.after(25, self.capture_and_save_gif)
        else:
            self.gif_image_count = 0
            self.list_gif_image[0].save(self.just_captured_gif_path,
                                        save_all = True,
                                        append_images=self.list_gif_image[1:],
                                        optimize = True,
                                        duration = 40,
                                        loop = 0)
            self.list_gif_image.clear()
            self.Captured_gif_numbers += 1
        self.is_captured_yet = True
        
    def update_image_to_gallery(self):
        
        captured_image_path = self.just_captured_image_path
        imageTk = ImageTk.PhotoImage(Image.open(captured_image_path).resize(((int(self.capture_screen.parent.winfo_width() * 0.6),
                                                                                int(self.capture_screen.parent.winfo_height() * 43 / 60)))))
        captured_image_button = ctk.CTkButton(self.capture_screen.gallery.image_tab,
                                                text ='',
                                                width = int(self.capture_screen.parent.winfo_width() * 3 / 32),
                                                height=int(self.capture_screen.parent.winfo_height() * 5 / 48),
                                                bg_color=COLOR_SALT,
                                                fg_color='transparent',
                                                hover_color=COLOR_MINT,
                                                image=ctk.CTkImage(light_image=Image.open(captured_image_path),
                                                                        dark_image=Image.open(captured_image_path),
                                                                        size = ((int(self.capture_screen.parent.winfo_width() * 21 / 160)),
                                                                                int(self.capture_screen.parent.winfo_height() * 7 / 48))),
                                                command = lambda index = self.capture_screen.gallery.controller.image_number: self.capture_screen.gallery.image_is_chosen(index))
        check_button = ctk.CTkCheckBox(captured_image_button,
                                        text = '',
                                        hover_color=COLOR_SKYBLUE,
                                        bg_color='transparent',
                                        checkmark_color=COLOR_PINEGREEN,
                                        fg_color=COLOR_MINT,
                                        width = 15,
                                        height= 15,
                                        onvalue= 1,
                                        offvalue= 0,
                                        command = lambda index = self.capture_screen.gallery.controller.image_number: self.capture_screen.gallery.controller.export_image(index))
        check_button.place(relx = 1, rely = 1, anchor = 'se')
        self.capture_screen.gallery.controller.list_image_Tk.append(imageTk)
        self.capture_screen.gallery.controller.list_export_image_check_button.append(check_button)
        self.capture_screen.gallery.controller.list_image_paths.append(captured_image_path)
        self.capture_screen.gallery.controller.list_image_button.append(captured_image_button)
        self.capture_screen.gallery.controller.image_number += 1
        self.capture_screen.gallery.gallery_images_update()

    def update_gif_to_gallery(self):
        gif_file = Image.open(self.just_captured_gif_path)
        frames_Tk = []
        frames = []
        for index in range(gif_file.n_frames):
                gif_file.seek(index)
                frame = gif_file.copy()
                frame_Tk = ImageTk.PhotoImage(gif_file.copy().resize(((int(self.capture_screen.parent.winfo_width() * 0.6),
                                                                    int(self.capture_screen.parent.winfo_height() * 43 / 60)))))
                frames.append(frame)
                frames_Tk.append(frame_Tk)
        self.capture_screen.gallery.controller.list_gif_Tk.append(frames_Tk)
        self.capture_screen.gallery.controller.list_gif.append(frames)
        gif = ctk.CTkButton(self.capture_screen.gallery.gif_tab,
                        text ='',
                        width = int(self.capture_screen.parent.winfo_width() * 3 / 32),
                        height=int(self.capture_screen.parent.winfo_height() * 5 / 48),
                         bg_color=COLOR_SALT,
                        fg_color='transparent',
                        hover_color=COLOR_MINT,
                        image=ctk.CTkImage(light_image=frames[0],
                                            dark_image=frames[0],
                                            size = (int(self.capture_screen.parent.winfo_width() * 21 / 160),
                                                    int(self.capture_screen.parent.winfo_height() * 7 / 48))),
                        command = lambda index = self.capture_screen.gallery.controller.gif_number: self.capture_screen.gallery.gif_is_chosen(index))
        check_gif_button = ctk.CTkCheckBox(gif,
                                        text = '',
                                        hover_color=COLOR_SKYBLUE,
                                        bg_color='transparent',
                                        checkmark_color=COLOR_PINEGREEN,
                                        fg_color=COLOR_MINT,
                                        width = 15,
                                        height= 15,
                                        onvalue= 1,
                                        offvalue= 0,
                                        command = lambda index = self.capture_screen.gallery.controller.gif_number: self.capture_screen.gallery.controller.export_gif(index))
        check_gif_button.place(relx = 1, rely = 1, anchor = 'se')
        self.capture_screen.gallery.controller.export_gif_check_button.append(check_gif_button)
        self.capture_screen.gallery.controller.list_gif_button.append(gif)
        self.capture_screen.gallery.controller.gif_number += 1
        #Update image gallery
        self.capture_screen.gallery.gallery_gif_update()
        
     
    def hand_detected_capture(self, frame):
        frame = self.handDetector.findHands(frame, draw = False)
        list_fingers_position = self.handDetector.findPosition(frame, draw = False)

        if len(list_fingers_position) != 0:
            fingers_number = 0
            if list_fingers_position[8][1] > list_fingers_position[12][1]:
                if list_fingers_position[4][1] > list_fingers_position[3][1]:
                    fingers_number += 1
                for id in range (8, 21, 4):
                    if list_fingers_position[id][2] < list_fingers_position[id - 2][2]:
                        fingers_number += 1
            else:
                return None
        else:
            return None
        if fingers_number == 5:
            self.five_fingers_on = True
        if self.five_fingers_on and fingers_number == 0:
            self.five_fingers_on = False
            if self.gif_mode:
                self.capture_screen.take_gif_and_update_gallery()
            else:
                self.capture_screen.capture_and_update_gallery()
            # self.capture_and_update_gallery()
            #self.capture_screen.capture_and_update_gallery()
    
    def face_detector(self, frame):
        # Prepare input data
        blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), (104, 177, 123), swapRB = False) # Take a data of a picture to detect
        ''' frame: your picture
            1.0 : streching scale
            (300, 300) : require size of model for input
            (104, 177, 123) : average color of each pixels
            swapRB = false : not changing color channel (for here is changing red and blue channel)
        '''

        # Set data input into net
        self.net.setInput(blob)

        # Run to detect face
        faces = self.net.forward()
        #faces have 4 dimensions, use faces.shape to see: (number of input, number of output, number of face detected, number information of each detected face)
        '''every detected face have 7 informations in turn is:
            - image number order
            - class id (1 or 0): usually is 1 refer to face
            - confidence of detection
            - start x
            - start y
            - end x
            - end y
            * 4 coordinate is scaled in range [0, 1]'''
        # Get the input picture size
        h = frame.shape[0] # height
        w = frame.shape[1] # width

        for i in range(faces.shape[2]):
            confidence = faces[0, 0, i, 2] #Get the confidence
            if confidence > 0.4:
                #Extract coordiante
                startx = int(faces[0, 0, i, 3] * w)
                starty = int(faces[0, 0, i, 4] * h)
                endx = int(faces[0, 0, i, 5] * w)
                endy = int(faces[0, 0, i, 6] * h)
                cv2.rectangle(frame, (startx, starty), (endx, endy), ((234, 206, 158))) #Draw a bounding box with color skyblue
        return frame

