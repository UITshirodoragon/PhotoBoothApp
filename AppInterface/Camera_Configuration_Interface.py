import sys
import os

# Đường dẫn tới folder chứa module 
package_controller_path = os.path.abspath(os.path.join('..', 'PhotoBoothApp'))
if package_controller_path not in sys.path:
    sys.path.append(package_controller_path)
import customtkinter as ctk
from PIL import Image
from AppController import Camera_Configuration_Controller as CCC
from define import *

class Camera_Configuration_Interface(ctk.CTkFrame):
    def __init__(self, parent, start_position, end_position):
        super().__init__(parent, height = abs(start_position - end_position), width = parent.winfo_width(), fg_color=COLOR_PISTACHIO)
        self.parent = parent
        self.controller = CCC.Camera_Configuration_Controller(self)
        self.capture_screen = parent
        #Animation variables
        self.current_position = start_position
        self.start_position = start_position
        self.end_position = end_position
        self.at_start_position = True

        # Toggle button
        #import down_arrow.png
        toggle_button_image_down_arrow = Image.open('DataStorage/Icons/down_arrow.png')
        self.toggle_button_imageCTk_down_arrow = ctk.CTkImage(light_image = toggle_button_image_down_arrow,
                                                                dark_image = toggle_button_image_down_arrow,
                                                                size = (20, 15))
        #import up_arrow.png
        toggle_button_image_up_arrow = Image.open('DataStorage/Icons/up_arrow.png')
        self.toggle_button_imageCTk_up_arrow = ctk.CTkImage(light_image = toggle_button_image_up_arrow,
                                                                dark_image = toggle_button_image_up_arrow,
                                                                size = (20, 15))

        #Capture mode button
        #Import gif.png
        gif_image = Image.open('DataStorage/Icons/gif.png')
        self.gif_image_CTk = ctk.CTkImage(light_image=gif_image,
                                            dark_image=gif_image,
                                            size = (100, 100))

        #Create capture mode button
        self.capture_mode_button = ctk.CTkButton(self,
                                                width=60,
                                                height=60, 
                                                bg_color='transparent',
                                                fg_color=COLOR_PISTACHIO,
                                                border_width=2,
                                                border_color='black',
                                                text = '',
                                                image = self.gif_image_CTk,
                                                hover_color='gray',
                                                command = self.swap_capture_mode)
        #Layout capture mode button
        self.capture_mode_button.place(relx = 0.8, rely = 0.5, anchor = 'center')

        #Flash button  
        #Variable to check if flash are on or off
        self.flash_state = False

        #Import flash_on.png and flash_off.png image
        flash_on_image = Image.open('DataStorage/Icons/flash_on.png')
        flash_off_image = Image.open('DataStorage/Icons/flash_off.png')

        self.flash_on_imageCTk = ctk.CTkImage(light_image=flash_on_image,
                                            dark_image=flash_on_image,
                                            size = (100, 100))
        self.flash_off_imageCTk = ctk.CTkImage(light_image=flash_off_image,
                                            dark_image=flash_off_image,
                                            size = (100, 100))
        
        #Create flash button
        self.flash_button = ctk.CTkButton(self,
                                    width=60,
                                    height=60, 
                                    bg_color='transparent',
                                    fg_color=COLOR_PISTACHIO,
                                    border_width=2,
                                    border_color='black',
                                    text = '',
                                    image = self.flash_off_imageCTk,
                                    hover_color='gray',
                                    command = self.toggle_flash)
        
        #Layout flash button
        self.flash_button.place(relx = 0.5, rely = 0.5, anchor = 'center')
        #Countdown mode frame
        #Import countdown mode image
        countdown_mode_3_image = Image.open('DataStorage/Icons/set_countdown_3.png')
        countdown_mode_5_image = Image.open('DataStorage/Icons/set_countdown_5.png')
        countdown_mode_10_image = Image.open('DataStorage/Icons/set_countdown_10.png')

        self.countdown_mode_3_imageCTk = ctk.CTkImage(light_image = countdown_mode_3_image,
                                                        dark_image=countdown_mode_3_image,
                                                        size = (100, 100))
        self.countdown_mode_5_imageCTk = ctk.CTkImage(light_image = countdown_mode_5_image,
                                                        dark_image=countdown_mode_5_image,
                                                        size = (100, 100))
        self.countdown_mode_10_imageCTk = ctk.CTkImage(light_image = countdown_mode_10_image,
                                                        dark_image=countdown_mode_10_image,
                                                        size = (100, 100))

        #Create countdown mode button
        #Choosing frame
        self.countdown_mode_3_button = ctk.CTkButton(self.capture_screen.choosing_frame,
                                                width=60,
                                                height=60, 
                                                bg_color='transparent',
                                                fg_color=COLOR_PISTACHIO,
                                                border_width=2,
                                                border_color='black',
                                                text = '',
                                                image = self.countdown_mode_3_imageCTk,
                                                hover_color='gray',
                                                command = self.choosing_3)
        self.countdown_mode_5_button = ctk.CTkButton(self.capture_screen.choosing_frame,
                                                width=60,
                                                height=60, 
                                                bg_color='transparent',
                                                fg_color=COLOR_PISTACHIO,
                                                border_width=2,
                                                border_color='black',
                                                text = '',
                                                image = self.countdown_mode_5_imageCTk,
                                                hover_color='gray',
                                                command = self.choosing_5)
        self.countdown_mode_10_button = ctk.CTkButton(self.capture_screen.choosing_frame,
                                                width=60,
                                                height=60, 
                                                bg_color='transparent',
                                                fg_color=COLOR_PISTACHIO,
                                                border_width=2,
                                                border_color='black',
                                                text = '',
                                                image = self.countdown_mode_10_imageCTk,
                                                hover_color='gray',
                                                command = self.choosing_10)
        self.current_countdown_mode_button_off = ctk.CTkButton(self,
                                                width=60,
                                                height=60, 
                                                bg_color='transparent',
                                                fg_color=COLOR_PISTACHIO,
                                                border_width=2,
                                                border_color='black',
                                                text = '',
                                                image = self.countdown_mode_3_imageCTk,
                                                hover_color='gray',
                                                command = self.choosing_countdown_mode)
        self.current_countdown_mode_button_on = ctk.CTkButton(self.capture_screen.choosing_frame,
                                                width=60,
                                                height=60, 
                                                bg_color='transparent',
                                                fg_color=COLOR_PISTACHIO,
                                                border_width=2,
                                                border_color='black',
                                                text = '',
                                                image = self.countdown_mode_3_imageCTk,
                                                hover_color='gray',
                                                command = self.choosing_countdown_mode)

        #Layout countdown mode button
        self.current_countdown_mode_button_on.grid(row = 0, column = 0, sticky = 'nsew', padx = 4, pady = 4)
        self.countdown_mode_5_button.grid(row = 1, column = 0, sticky = 'nsew', padx = 4, pady = 4)
        self.countdown_mode_10_button.grid(row = 2, column = 0, sticky = 'nsew', padx = 4, pady = 4)
        self.current_countdown_mode_button_off.place(relx = 0.2, rely = 0.5, anchor = 'center')

        # Create toggle button
        self.toggle_button = ctk.CTkButton(self.capture_screen,
                                        width=60,
                                        height=3,
                                        bg_color='transparent',
                                        fg_color=COLOR_LION,
                                        border_width=0,
                                        text = '',
                                        hover_color=COLOR_PINEGREEN,
                                        image = self.toggle_button_imageCTk_down_arrow,
                                        command = self.Toggle_Slide)
        #Layout toggle button
        self.toggle_button.place(relx = 0.5, rely = self.current_position + -self.start_position, anchor = 'n')

    def toggle_flash(self):
        if self.flash_state:
            #Changing flash state to False
            self.flash_state = False

            #Turn off the flash

            #Changing flash icon to off
            self.flash_button.configure(image = self.flash_off_imageCTk)
        else:
             #Changing flash state to True
            self.flash_state = True

            #Turn on the flash

            #Changing flash icon to on
            self.flash_button.configure(image = self.flash_on_imageCTk)

    #Animation
    def Toggle_Slide(self):
        #Unpack the frame and the button
        self.toggle_button.place_forget()
        self.place_forget()
        # Check if the slider is at start position
        if self.at_start_position:
            self.Move_Down()
        else:
            self.capture_screen.choosing_frame.place_forget()
            self.Move_Up()

    #Pop animation
    def Move_Down(self):
        self.current_position += 0.2
        self.toggle_button.place(relx = 0.5,
                            rely = self.current_position + -self.start_position,
                            anchor = 'n')
        self.place(relx = 0,
                    rely = self.current_position,
                    relwidth = 1,
                    relheight = abs(self.start_position - self.end_position))
        # Change direction of arrow and toggle_at_start_position value
        self.toggle_button.configure(image = self.toggle_button_imageCTk_up_arrow)
        self.at_start_position = False

    def Move_Up(self):
        self.current_position -= 0.2
        self.toggle_button.place(relx = 0.5,
                            rely = self.current_position + -self.start_position,
                            anchor = 'n')
        self.place(relx = 0,
                    rely = self.current_position,
                    relwidth = 1,
                    relheight = abs(self.start_position - self.end_position))
        # Change direction of arrow and toggle_at_start_position value
        self.toggle_button.configure(image = self.toggle_button_imageCTk_down_arrow)
        self.at_start_position = True

    def swap_capture_mode(self):
        if self.controller.gif_mode:
            self.controller.gif_mode = False
            self.capture_mode_button.configure(image = self.capture_screen.capture_button_imageCTk)
            self.capture_screen.capture_button.configure(image = self.gif_image_CTk)
        else:
            self.controller.gif_mode = True
            self.capture_mode_button.configure(image = self.gif_image_CTk)
            self.capture_screen.capture_button.configure(image = self.capture_screen.capture_button_imageCTk)

    def choosing_countdown_mode(self):
        if not self.controller.is_countdown_button_pressed:
            self.controller.is_countdown_button_pressed = True
            self.capture_screen.choosing_frame.place(relx=0.2, rely = 0.29, anchor = 'center')
        else:
            self.controller.is_countdown_button_pressed = False
            self.capture_screen.choosing_frame.place_forget()

    def choosing_3(self):
        self.current_countdown_mode_button_off.configure(image = self.countdown_mode_3_imageCTk)
        self.current_countdown_mode_button_on.configure(image = self.countdown_mode_3_imageCTk)
        self.controller.set_countdown_time(3)
        self.countdown_mode_3_button.grid_forget()
        self.countdown_mode_5_button.grid(row = 1, column = 0, sticky = 'nsew', padx = 4, pady = 4)
        self.countdown_mode_10_button.grid(row = 2, column = 0, sticky = 'nsew', padx = 4, pady = 4)
        self.capture_screen.choosing_frame.place_forget()

    def choosing_5(self):
        self.current_countdown_mode_button_off.configure(image = self.countdown_mode_5_imageCTk)
        self.current_countdown_mode_button_on.configure(image = self.countdown_mode_5_imageCTk)
        self.controller.set_countdown_time(5)
        self.countdown_mode_5_button.grid_forget()
        self.countdown_mode_3_button.grid(row = 1, column = 0, sticky = 'nsew', padx = 4, pady = 4)
        self.countdown_mode_10_button.grid(row = 2, column = 0, sticky = 'nsew', padx = 4, pady = 4)
        self.capture_screen.choosing_frame.place_forget()
    
    def choosing_10(self):
        self.current_countdown_mode_button_off.configure(image = self.countdown_mode_10_imageCTk)
        self.current_countdown_mode_button_on.configure(image = self.countdown_mode_10_imageCTk)
        self.controller.set_countdown_time(10)
        self.countdown_mode_10_button.grid_forget()
        self.countdown_mode_3_button.grid(row = 1, column = 0, sticky = 'nsew', padx = 4, pady = 4)
        self.countdown_mode_5_button.grid(row = 2, column = 0, sticky = 'nsew', padx = 4, pady = 4)
        self.capture_screen.choosing_frame.place_forget()
