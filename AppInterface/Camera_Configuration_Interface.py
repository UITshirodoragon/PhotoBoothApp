import customtkinter as ctk
from PIL import Image
import Image_Capture_Interface as ICI
import Get_Started_Interface as GSI

class Camera_Configuration_Interface(ctk.CTkFrame):
    def __init__(self, parent, start_position, end_position):
        super().__init__(parent, height = abs(start_position - end_position), width = parent.winfo_width())
        self.parent = parent
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
                                    fg_color='transparent',
                                    border_width=2,
                                    border_color='black',
                                    text = '',
                                    image = self.flash_off_imageCTk,
                                    hover_color='gray',
                                    command = self.toggle_flash)
        
        #Layout flash button
        self.flash_button.place(relx = 0.5, rely = 0.5, anchor = 'center')

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
    def Toggle_Slide(self, choosing_frame, toggle_button):
        #Unpack the frame and the button
        toggle_button.place_forget()
        self.place_forget()
        # Check if the slider is at start position
        if self.at_start_position:
            self.Move_Down(toggle_button)
        else:
            choosing_frame.place_forget()
            self.Move_Up(toggle_button)

    #Slide animation
    
    #Pop animation
    def Move_Down(self, toggle):
        self.current_position += 0.2
        toggle.place(relx = 0.5,
                            rely = self.current_position + -self.start_position,
                            anchor = 'n')
        self.place(relx = 0,
                    rely = self.current_position,
                    relwidth = 1,
                    relheight = abs(self.start_position - self.end_position))
        # Change direction of arrow and toggle_at_start_position value
        toggle.configure(image = self.toggle_button_imageCTk_up_arrow)
        self.at_start_position = False

    def Move_Up(self, toggle):
        self.current_position -= 0.2
        toggle.place(relx = 0.5,
                            rely = self.current_position + -self.start_position,
                            anchor = 'n')
        self.place(relx = 0,
                    rely = self.current_position,
                    relwidth = 1,
                    relheight = abs(self.start_position - self.end_position))
        # Change direction of arrow and toggle_at_start_position value
        toggle.configure(image = self.toggle_button_imageCTk_down_arrow)
        self.at_start_position = True