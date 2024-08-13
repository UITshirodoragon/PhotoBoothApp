import customtkinter as ctk
from PIL import Image, ImageTk
import cv2

class Image_Capture_Controller():
    def __init__(self, capture_screen):
        self.capture_screen = capture_screen
        self.is_captured_yet = False
        self.just_captured_image_path = None
        self.countdown_time = 3
        self.countdown_time_temp = self.countdown_time
        self.Captured_numbers = 0
    def capture_and_update_gallery(self):
        if self.is_captured_yet:
                self.is_captured_yet = False
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
                                                                                size = ((int(self.capture_screen.parent.winfo_width() * 3 / 32)),
                                                                                        int(self.capture_screen.parent.winfo_height() * 5 / 48))),
                                                        command = lambda : self.capture_screen.gallery.button_is_chosen(imageTk))
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
                self.Countdown()
                #Wait for image is captured then update gallery
                self.capture_screen.gallery.after(int((self.countdown_time + 0.5) * 1000), self.capture_and_update_gallery)
    
    def Take_Picture(self):
        ret, frame = self.capture_screen.cap.read()
        # Check if image is successfully captured
        if ret:
            self.Captured_numbers +=1
            self.capture_screen.Notification_label.configure(text = 'Captured successfully')
            cv2.imwrite(f'DataStorage/ImageGallery/image{self.Captured_numbers}.png', frame) # Save image
            #Tell that an image is captured
            self.is_captured_yet = True
            self.just_captured_image_path = f'DataStorage/ImageGallery/image{self.Captured_numbers}.png'
        else:
            self.capture_screen.Notification_label.configure(text = 'Captured unsuccessfully')
        self.capture_screen.Notification_label.place(relx = 0.5, rely = 0.5, anchor = 'center') # layout nofitication
        self.capture_screen.Notification_label.after(500, self.capture_screen.Notification_label.place_forget) # close the nofitication

    def Countdown(self):
        if self.countdown_time_temp > 0:            
            self.capture_screen.countdown_label.configure(text = f'{self.countdown_time_temp}')
            self.capture_screen.countdown_label.place(relx=0.5, rely=0.5, anchor = 'center')
            self.countdown_time_temp -= 1
            self.capture_screen.after(1000, self.Countdown)
        else:
            self.countdown_time_temp = self.countdown_time
            self.capture_screen.countdown_label.place_forget()
            self.Take_Picture()