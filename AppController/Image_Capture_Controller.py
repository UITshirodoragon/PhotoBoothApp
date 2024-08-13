import customtkinter as ctk
from PIL import Image, ImageTk
import cv2

class Image_Capture_Controller():
    def __init__(self, capture_screen):
        self.gif_mode = False
        self.capture_screen = capture_screen
        self.is_captured_yet = False
        self.just_captured_image_path = None
        self.just_captured_gif_path = None
        self.countdown_time = 3
        self.countdown_time_temp = self.countdown_time
        self.Captured_numbers = 0
        self.is_gif_capture_done = False
        self.list_gif_image = []
        self.gif_count = 0
        self.gif_image_count = 0
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
                captured_image_button = ctk.CTkButton(self.capture_screen.gallery.image_tab,
                                                        text ='',
                                                        width = int(self.capture_screen.parent.winfo_width() * 0.15),
                                                        height=int(self.capture_screen.parent.winfo_height() / 6),
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
                self.capture_screen.gallery.after(int((self.countdown_time + 0.5) * 1000), self.capture_and_update_gallery)
    
    def take_gif_and_update_gallery(self):
        if self.is_captured_yet:
                self.is_captured_yet = False
                self.capture_screen.capture_button.configure(state = 'normal', command = self.take_gif_and_update_gallery)
                self.capture_screen.gallery_button.configure(state = 'normal', command = self.capture_screen.go_to_gallery)
                self.capture_screen.camera_configuration.toggle_button.configure(state = 'normal', command = self.capture_screen.camera_configuration.Toggle_Slide)
                self.capture_screen.Return_start_screen_button.configure(state = 'normal', command = self.capture_screen.back_to_start_screen)
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
                               width = int(self.capture_screen.parent.winfo_width() * 0.15),
                                height=int(self.capture_screen.parent.winfo_height() / 6),
                                bg_color='transparent',
                                fg_color='transparent',
                                hover_color='gray',
                                image=ctk.CTkImage(light_image=frames[0],
                                                    dark_image=frames[0],
                                                    size = (int(self.capture_screen.parent.winfo_width() * 0.15),
                                                            int(self.capture_screen.parent.winfo_height() / 6))),
                                command = lambda index = self.capture_screen.gallery.controller.gif_number: self.capture_screen.gallery.gif_is_chosen(index))
                check_gif_button = ctk.CTkCheckBox(gif,
                                               text = '',
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
                #Capture and update gallery
                self.capture_screen.gallery.after(int((self.countdown_time + 3 + 3.5) * 1000), self.take_gif_and_update_gallery)
