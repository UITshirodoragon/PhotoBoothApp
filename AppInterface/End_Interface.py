import customtkinter as ctk
from define import *
from PIL import Image
import os
import sys

# Đường dẫn tới folder chứa module 
package_controller_path = os.path.abspath(os.path.join('..', 'PhotoBoothApp'))
if package_controller_path not in sys.path:
    sys.path.append(package_controller_path)
from AppController import End_Interface_Controller as EIC

class End_Interface(ctk.CTkFrame):
    def __init__(self, parent, start_screen):
        super().__init__(parent, fg_color=COLOR_MINT)
        self.email = None
        self.parent = parent
        self.start_screen = start_screen
        self.gallery = None
        self.template_screen = None
        self.camera_configuration = None
        self.controller = EIC.End_Interface_Controller(self)

        self.thanks_label =ctk.CTkLabel(self,
                                        text = 'Thank you for using our service !',
                                        text_color='white',
                                        font = ctk.CTkFont(family=HEADER_FONT, size=50))
        self.thanks_label.place(relx = 0.5, rely = 0.45, anchor = 'center')

        self.reset_button = ctk.CTkButton(self,
                                          text = 'Reset',
                                          height=60,
                                          corner_radius= 30,
                                          bg_color='transparent',
                                          fg_color=COLOR_BLOODRED,
                                          font = ctk.CTkFont(family=DESCRIPTION_FONT, size=40),
                                          command = self.reset_aplication
                                          )
        self.reset_button.place(relx = 0.5, rely = 0.55, anchor = 'center')

        self.destroy_window_button = ctk.CTkButton(self,
                                                   text = '',
                                                   fg_color=COLOR_BLOODRED,
                                                   bg_color='transparent',
                                                   width=40,
                                                   height=40,
                                                   corner_radius=150,
                                                   hover_color=None,
                                                   image = ctk.CTkImage(light_image=Image.open('DataStorage/Icons/exit_button.png'),
                                                                        dark_image=Image.open('DataStorage/Icons/exit_button.png'),
                                                                        size = (50, 50)),
                                                   command = self.parent.destroy)
        self.destroy_window_button.place(relx = 1, rely = 0, anchor = 'ne')

        back_button = ctk.CTkButton(master=self, 
                         text='Back',
                         text_color="#ffffff",
                         height=60,
                         font=ctk.CTkFont(family=HEADER_FONT, size=22),
                         bg_color='transparent',
                         fg_color='#BD8D5F',
                         image=LEFT_ARROW_SOLID,
                         hover=False,
                         anchor='center',
                         compound='left',
                         corner_radius=30,
                         command=self.return_email_interface)
        back_button.place(relx=0.02, rely=0.9)

    def return_email_interface(self):
        self.pack_forget()
        self.email.pack(expand = True, fill = 'both')

    def reset_aplication(self):
        self.controller.reset_parameters()
        for widget in self.gallery.gif_tab.winfo_children():
            if type(widget) is ctk.CTkButton:
                    widget.grid_forget()
        for widget in self.gallery.image_tab.winfo_children():
            if type(widget) is ctk.CTkButton:
                    widget.grid_forget()
        self.gallery.display_image_canvas.delete('all')
        self.gallery.no_image_is_chosen_label.place(relx = 0.5, rely = 0.5, anchor = 'center')
        self.gallery.no_image_label.grid(row = 2, column = 0, columnspan=2, sticky = 'nsew')
        self.gallery.no_gif_label.grid(row = 2, column = 0, columnspan=2, sticky = 'nsew')
        self.gallery.confirm_frame.place_forget()
        self.gallery.export_gif_label.configure(text = '')
        self.gallery.confirm_label.configure(text = '')

        self.template_screen.text.set('you haven'+ "'t"+ '\nselected\nanything' )
        self.template_screen.template_2grid_btn.configure(fg_color=COLOR_LION)          
        self.template_screen.template_4grid_btn.configure(fg_color=COLOR_LION)          
        self.template_screen.template_6grid_btn.configure(fg_color=COLOR_LION)          
        self.template_screen.template_8grid_btn.configure(fg_color=COLOR_LION)   

        if self.camera_configuration.capture_screen.controller.gif_mode:
            self.camera_configuration.capture_screen.controller.gif_mode = False
            self.camera_configuration.capture_screen.capture_button.configure(command = self.camera_configuration.capture_screen.controller.capture_and_update_gallery)
            self.camera_configuration.capture_mode_button.configure(image = self.camera_configuration.gif_image_CTk)
            self.camera_configuration.capture_screen.capture_button.configure(image = self.camera_configuration.capture_screen.capture_button_imageCTk)
        self.pack_forget()
        self.parent.bind_all('<Button>', self.start_screen.Next_To_Template_Screen)
        self.start_screen.pack(expand = True, fill = 'both')
        
        