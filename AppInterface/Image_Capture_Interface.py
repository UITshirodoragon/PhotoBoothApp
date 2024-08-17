import sys
import os

# Đường dẫn tới folder chứa module 
package_controller_path = os.path.abspath(os.path.join('..', 'PhotoBoothApp'))
if package_controller_path not in sys.path:
    sys.path.append(package_controller_path)
import customtkinter as ctk
import cv2
from PIL import Image, ImageTk
from AppController import Image_Capture_Controller as ICC
from define import *

class Image_Capture_Interface(ctk.CTkFrame):
    def __init__(self, parent, gallery, start_screen):
         # inherit from CTkFrame
        super().__init__(master = parent)
        self.controller = ICC.Image_Capture_Controller(self)
        self.camera_configuration = None
        self.gallery = gallery
        self.start_screen = start_screen
        self.parent = parent

        #check if user in capture screen, if not stop update frame
        self.in_capture_screen = False
        
        self.cap = cv2.VideoCapture(0) # Choose camera
        # Capture frame
        #Create capture_frame
        self.capture_frame = ctk.CTkCanvas(self,
                                            bd = 0,
                                            highlightthickness = 0,
                                            relief = 'ridge')
        self.capture_frame.place(relx = 0.5, rely = 0.5, anchor = 'center')
        
        #Layout capture_frame
        self.capture_frame.place(relx = 0.5
                                , rely = 0.5,
                                relheight=1,
                                relwidth=1,
                                anchor = 'center',
                                )

        # Capture button
        #Import capture_button.png
        capture_button_image = Image.open('DataStorage/Icons/capture_button.png')
        self.capture_button_imageCTk = ctk.CTkImage(light_image=capture_button_image,
                                                dark_image=capture_button_image,
                                                size = (100, 100))

        #Create capture_button
        self.capture_button = ctk.CTkButton(self,
                                        width=80,
                                        height=80,
                                        fg_color=COLOR_SALT,
                                        bg_color='transparent',
                                        border_width=0,
                                        text = '',
                                        hover_color='gray',
                                        image = self.capture_button_imageCTk,
                                        command = self.controller.capture_and_update_gallery)

        #Layout capture_button
        self.capture_button.place(relx = 1,
                                rely = 0.5,
                                anchor = 'e')

        # Gallery button
        #Import gallery_button_image.png
        gallery_button_image = Image.open('DataStorage/Icons/gallery_button_image.png')
        gallery_button_imageCTk = ctk.CTkImage(light_image=gallery_button_image,
                                                dark_image=gallery_button_image,
                                                size = (100, 100))

        #Create gellery_button
        self.gallery_button = ctk.CTkButton(self,
                                        image = gallery_button_imageCTk,
                                        width=80,
                                        height=80,
                                        fg_color=COLOR_SALT,
                                        bg_color='transparent',
                                        border_width=0,
                                        text = '',
                                        hover_color='gray',
                                        command = self.go_to_gallery)

        #Layout gallery_button
        self.gallery_button.place(relx = 1,
                            rely = 1,
                            anchor = 'se')

        # Return to get started interface
        #Import return_button_image.png
        Return_button_image = Image.open('DataStorage/Icons/return_button_image.png')
        Return_button_imageCTk = ctk.CTkImage(light_image=Return_button_image,
                                                dark_image=Return_button_image)
        #Create return_button
        self.Return_start_screen_button = ctk.CTkButton(self,
                                                        width=50,
                                                        height=50,
                                                        fg_color=COLOR_LION,
                                                        bg_color='transparent',
                                                        corner_radius=10,
                                                        text = '',
                                                        hover_color=COLOR_PINEGREEN,
                                                        image = LEFT_ARROW_SOLID,
                                        command = self.back_to_start_screen)
        #Layout return_button
        self.Return_start_screen_button.place(relx = 0, 
                                        rely = 0)


        #Create choosing frame
        self.choosing_frame = ctk.CTkFrame(self)
        self.choosing_frame.columnconfigure(0, weight=1)
        self.choosing_frame.rowconfigure((0, 1, 2), weight=1, uniform= 'a')

        #Notification label 
        self.Notification_label = ctk.CTkLabel(self,
                            text = '',
                            font = ('Arial', 30),
                            fg_color='transparent',
                            bg_color='transparent')

       # Countdown label
        self.countdown_label = ctk.CTkLabel(self,
                                        text = '',
                                        font = ('Arial', 40),
                                        fg_color = 'transparent')

        # Capture video from camera
        self.Update_frame()

    def Update_frame(self):
        global image_Tk
        if self.in_capture_screen:
            _, frame = self.cap.read() # Get frame from camera
            self.controller.hand_detected_capture(frame)
            frame = self.controller.face_detector(frame)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA) #Convert color system
            frame_array = frame
            img = Image.fromarray(frame_array).resize((self.parent.winfo_width(), self.parent.winfo_height())) # transfer an array to img
            image_Tk = ImageTk.PhotoImage(image=img)
            self.capture_frame.create_image(0,0, image = image_Tk, anchor = 'nw')
            self.capture_frame.after(25, self.Update_frame) # Call the Update_Frame() method after every 10 miliseconds
        else:
            self.cap.read()
            return None

    def back_to_start_screen(self):
        self.in_capture_screen = False
        if self.camera_configuration.at_start_position == False:
              self.camera_configuration.Toggle_Slide()
        self.pack_forget()
        self.start_screen.pack(expand = True, fill = 'both')
        self.parent.bind_all('<Button>', self.start_screen.Next_To_Capture_Screen) 

    def go_to_gallery(self):
        self.in_capture_screen = False
        self.pack_forget()
        if self.camera_configuration.at_start_position == False:
                self.camera_configuration.Toggle_Slide()
        self.gallery.pack(expand = True, fill = 'both')

    def Countdown(self):
        if self.controller.countdown_time_temp > 0:            
            self.countdown_label.configure(text = f'{self.controller.countdown_time_temp}')
            self.countdown_label.place(relx=0.5, rely=0.5, anchor = 'center')
            self.controller.countdown_time_temp -= 1
            self.after(1000, self.Countdown)
        else:
            self.countdown_time_temp = self.controller.countdown_time
            self.countdown_label.place_forget()
            self.controller.Take_Picture()
        