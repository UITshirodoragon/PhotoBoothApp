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
        self.just_captured_gif_path = None
        self.gif_mode = False
        self.is_gif_capture_done = False
        self.list_gif_image = []
        self.gif_count = 0
        self.gif_image_count = 0
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
            self.Notification_label.configure(text = 'Captured successfully')
            cv2.imwrite(f'DataStorage/ImageGallery/image{self.Captured_numbers}.png', frame) # Save image
            #Tell that an image is captured
            self.is_captured_yet = True
            self.just_captured_image_path = f'DataStorage/ImageGallery/image{self.Captured_numbers}.png'
        else:
            self.Notification_label.configure(text = 'Captured unsuccessfully')
        self.Notification_label.place(relx = 0.5, rely = 0.5, anchor = 'center') # layout nofitication
        self.Notification_label.after(500, self.Notification_label.place_forget) # close the nofitication

    def Take_gif(self):
        ret, frame = self.cap.read()
        if ret == False:
            self.Notification_label.configure(text = 'Captured unsuccessfully')
            self.Notification_label.place(relx = 0.5, rely = 0.5, anchor = 'center') # layout nofitication
            self.Notification_label.after(500, self.Notification_label.place_forget) # close the nofitication
        if self.gif_image_count < 75:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(frame)
            self.list_gif_image.append(img)
            self.gif_image_count += 1
            self.capture_frame.after(25, self.Take_gif)
        else:
            self.gif_image_count = 0
            self.gif_count += 1
            self.list_gif_image[0].save(f'DataStorage/GifGallery/Gif{self.gif_count}.gif',
                                        save_all = True,
                                        append_images=self.list_gif_image[1:],
                                        optimize = True,
                                        duration = 30,
                                        loop = 0)
            self.list_gif_image.clear()
            self.is_captured_yet = True
            self.Notification_label.configure(text = 'Captured successfully')
            self.Notification_label.place(relx = 0.5, rely = 0.5, anchor = 'center') # layout nofitication
            self.Notification_label.after(500, self.Notification_label.place_forget) # close the nofitication
            self.just_captured_gif_path = f'DataStorage/GifGallery/Gif{self.gif_count}.gif'

    def Countdown(self):
        if self.countdown_time_temp > 0:            
            self.countdown_label.configure(text = f'{self.countdown_time_temp}')
            self.countdown_label.place(relx=0.5, rely=0.5, anchor = 'center')
            self.countdown_time_temp -= 1
            self.after(1000, self.Countdown)
        else:
            self.countdown_time_temp = self.countdown_time
            self.countdown_label.place_forget()
            if self.gif_mode:
                self.Take_gif()
            else:
                self.Take_Picture()
        