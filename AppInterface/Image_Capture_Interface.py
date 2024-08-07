import customtkinter as ctk
import cv2
from PIL import Image, ImageTk
import time
import User_Image_Gallery_Interface as UIG
import Get_Started_Interface as GSI
import Camera_Configuration_Interface as CCI

class Image_Capture_Interface(ctk.CTkFrame):
    def __init__(self, parent):
         # inherit from CTkFrame
        super().__init__(master = parent)
        self.is_captured_yet = False
        self.just_captured_image_path = None
        self.countdown_time = 3
        self.countdown_time_temp = self.countdown_time
        self.Captured_numbers = 0
        self.parent = parent
        
        self.cap = cv2.VideoCapture(0) # Choose camera

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


       # Countdown label
        self.countdown_label = ctk.CTkLabel(self,
                                        text = '',
                                        font = ('Arial', 40),
                                        fg_color = 'transparent')

        # Capture video from camera
        self.Update_frame()

    def Update_frame(self):
        global image_Tk
        _, frame = self.cap.read() # Get frame from camera
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA) #Convert color system
        frame_array = frame
        img = Image.fromarray(frame_array).resize((self.parent.winfo_width(), self.parent.winfo_height())) # transfer an array to img
        image_Tk = ImageTk.PhotoImage(image=img)
        self.capture_frame.create_image(0,0, image = image_Tk, anchor = 'nw')
        self.capture_frame.after(10, self.Update_frame) # Call the Update_Frame() method after every 10 miliseconds

    def Take_Picture(self):
        ret, frame = self.cap.read()
        # Check if image is successfully captured
        if ret:
            self.Captured_numbers +=1
            Notification_label = ctk.CTkLabel(self,
                                        text = 'Captured successfully',
                                        font = ('Arial', 30),
                                        fg_color='transparent')
        else:
            Notification_label = ctk.CTkLabel(self,
                                          text = 'Captured unsuccessfully',
                                          font = ('Arial', 0),
                                          fg_color='transparent')
        Notification_label.place(relx = 0.5, rely = 0.5, anchor = 'center') # layout nofitication
        Notification_label.after(1000, Notification_label.place_forget) # close the nofitication
        cv2.imwrite(f'DataStorage/ImageGallery/image{self.Captured_numbers}.png', frame) # Save image
        #Tell that an image is captured
        self.is_captured_yet = True
        self.just_captured_image_path = f'DataStorage/ImageGallery/image{self.Captured_numbers}.png'


    def Countdown(self):
        if self.countdown_time_temp > 0:            
            self.countdown_label.configure(text = f'{self.countdown_time_temp}')
            self.countdown_label.place(relx=0.5, rely=0.5, anchor = 'center')
            self.countdown_time_temp -= 1
            self.after(1000, self.Countdown)
        else:
            self.countdown_time_temp = self.countdown_time
            self.countdown_label.place_forget()
            self.Take_Picture()
        