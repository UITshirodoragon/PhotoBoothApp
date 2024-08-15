import sys
import os

# Đường dẫn tới folder chứa module 
package_controller_path = os.path.abspath(os.path.join('..', 'PhotoBoothApp'))
if package_controller_path not in sys.path:
    sys.path.append(package_controller_path)
import customtkinter as ctk
import cv2
from PIL import Image, ImageTk
import time
import User_Image_Gallery_Interface as UIG
import Get_Started_Interface as GSI
import Camera_Configuration_Interface as CCI
from AppController import Image_Capture_Controller


class Image_Capture_Interface(ctk.CTkFrame):
    def __init__(self, parent, gallery, start_screen):
         # inherit from CTkFrame
        super().__init__(master = parent)

        self.camera_configuration = None
        self.gallery = gallery
        self.start_screen = start_screen
        self.parent = parent
        
        
        #khoa add controller for image capture
        self.controller = Image_Capture_Controller.Image_Capture_Controller(self)

        # Capture frame
        #Create capture_frame
        self.capture_frame = ctk.CTkCanvas(self,
                                            bd = 0,
                                            highlightthickness = 0,
                                            relief = 'ridge')
        
        #Layout capture_frame
        self.capture_frame.place(relx = 0.5
                                , rely = 0.5,
                                relheight=1,
                                relwidth=1,
                                anchor = 'center',
                                )

        # Capture button
        #Import capture_button.png
        capture_button_image = Image.open('DataStorage/Icon/Capture_button.png')
        self.capture_button_imageCTk = ctk.CTkImage(light_image=capture_button_image,
                                                dark_image=capture_button_image,
                                                size = (100, 100))

        #Create capture_button
        self.capture_button = ctk.CTkButton(self,
                                        width=80,
                                        height=80,
                                        fg_color='transparent',
                                        bg_color='transparent',
                                        border_width=0,
                                        text = '',
                                        hover_color='gray',
                                        image = self.capture_button_imageCTk,
                                        command = self.capture_and_update_gallery)

        #Layout capture_button
        self.capture_button.place(relx = 1,
                                rely = 0.5,
                                anchor = 'e')

        # Gallery button
        #Import gallery_button_image.png
        gallery_button_image = Image.open('DataStorage/Icon/gallery_button_image.png')
        gallery_button_imageCTk = ctk.CTkImage(light_image=gallery_button_image,
                                                dark_image=gallery_button_image,
                                                size = (100, 100))

        #Create gellery_button
        self.gallery_button = ctk.CTkButton(self,
                                        image = gallery_button_imageCTk,
                                        width=80,
                                        height=80,
                                        fg_color='transparent',
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
        Return_button_image = Image.open('DataStorage/Icon/return_button_image.png')
        Return_button_imageCTk = ctk.CTkImage(light_image=Return_button_image,
                                                dark_image=Return_button_image)
        #Create return_button
        self.Return_start_screen_button = ctk.CTkButton(self,
                                        width=50,
                                        height=50,
                                        fg_color='transparent',
                                        bg_color='transparent',
                                        border_width=0,
                                        text = '',
                                        hover_color='gray',
                                        image = Return_button_imageCTk,
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
                            fg_color='transparent')

       # Countdown label
        self.countdown_label = ctk.CTkLabel(self,
                                        text = '',
                                        font = ('Arial', 40),
                                        fg_color = 'transparent')


        self.fps_realtime_label = ctk.CTkLabel(self,
                                        text = '',
                                        font = ('Arial', 40),
                                        fg_color = 'transparent')
        #back-end
        # Capture video from camera
        self.Update_frame()
        #back-end
    
    
        
    #back-end
    def Update_frame(self):
        global image_Tk
        
        self.capture_frame.create_image(0,-84, image = self.controller.preview_image(), anchor = 'nw')
        self.fps_realtime_label.configure(text = f'{int(self.controller.fps_realtime)}')
        self.fps_realtime_label.place(relx=0, rely=1, anchor = 'sw')
        self.capture_frame.after(10, self.Update_frame) # Call the Update_Frame() method after every 10 miliseconds
        #back-end
    
    
    
    def Take_Picture(self):
        if self.controller.camera_ready_state == True: 
            
            # cv2.imwrite(f'DataStorage/ImageGallery/image{self.Captured_numbers}.png', frame) # Save image
            self.just_captured_image_path = f'DataStorage/ImageGallery/image{self.controller.Captured_numbers}.png'
            self.controller.capture_and_save_image()
            #Tell that an image is captured
            self.Notification_label.configure(text = 'Captured successfully')
            
        else:
            self.Notification_label.configure(text = 'Captured unsuccessfully')
        self.Notification_label.place(relx = 0.5, rely = 0.5, anchor = 'center') # layout nofitication
        self.Notification_label.after(1000, self.Notification_label.place_forget)
        
        

    def go_to_gallery(self):
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
            self.controller.countdown_time_temp = self.controller.countdown_time
            self.countdown_label.place_forget()
            self.Take_Picture()
            
    def back_to_start_screen(self):
        if self.camera_configuration.at_start_position == False:
              self.camera_configuration.Toggle_Slide()
        self.pack_forget()
        self.start_screen.pack(expand = True, fill = 'both')
        self.parent.bind_all('<Button>', self.start_screen.Next_To_Capture_Screen) 

    def go_to_gallery(self):
        self.pack_forget()
        if self.camera_configuration.at_start_position == False:
                self.camera_configuration.Toggle_Slide()
        self.gallery.pack(expand = True, fill = 'both')

    def capture_and_update_gallery(self):
        if self.controller.is_captured_yet:
                self.controller.is_captured_yet = False
                #Enable capture button
                self.capture_button.configure(state = 'normal', command = self.capture_and_update_gallery)
                self.gallery_button.configure(state = 'normal', command = self.go_to_gallery)
                self.camera_configuration.toggle_button.configure(state = 'normal', command = self.camera_configuration.Toggle_Slide)
                self.Return_start_screen_button.configure(state = 'normal', command = self.back_to_start_screen)
                self.controller.update_image_to_gallery()
        else:
                #Disable capture button
                self.capture_button.configure(state = 'disable', command = None)
                self.gallery_button.configure(state = 'disable', command = None)
                self.camera_configuration.toggle_button.configure(state = 'disable', command = None)
                self.Return_start_screen_button.configure(state = 'disable', command = None)
                if self.camera_configuration.at_start_position == False:
                        self.camera_configuration.Toggle_Slide()
                #Capture
                self.Countdown()
                #Wait for image is captured then update gallery
                self.gallery.after(int((self.controller.countdown_time + 1) * 1000), self.capture_and_update_gallery)