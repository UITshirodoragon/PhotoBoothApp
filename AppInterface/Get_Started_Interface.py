'''import customtkinter as ctk
import Image_Capture_Interface as ICI
from PIL import Image

class Get_Started_Interface(ctk.CTkFrame):
    def __init__(self, parent):
        # inherit from CTkFrame
        super().__init__(master = parent)
        self.state = True # state of object: True = activate, False = deactivate
        self.parent = parent
        self.capture_screen = None
        self.camera_configuration = None
        # 'Press to start' label
        self.label = ctk.CTkLabel(self,
                                   text = 'Press to start',
                                   font = ('Arial', 20))

        self.destroy_window_button = ctk.CTkButton(self,
                                                   text = '',
                                                   fg_color='transparent',
                                                   bg_color='transparent',
                                                   width=30,
                                                   height=30,
                                                   hover_color='gray',
                                                   image = ctk.CTkImage(light_image=Image.open('DataStorage/Icon/quit_button.png'),
                                                                        dark_image=Image.open('DataStorage/Icon/quit_button.png'),
                                                                        size = (50, 50)),
                                                   command = self.parent.destroy)
        self.destroy_window_button.place(relx = 1, rely = 0, anchor = 'ne')

        # Layout
        # Put the label in the center of the frame
        self.label.place(relx = 0.5,
                          rely = 0.5,
                         anchor = 'center')
        
        Get started interface function
    def Next_To_Capture_Screen(self, event):
        self.parent.unbind_all('<Button>')
        self.pack_forget()
        self.capture_screen.pack(expand = True, fill = 'both')
        self.camera_configuration.place(relx = 0,
                                    rely = -0.2,
                                    relwidth = 1,
                                    relheight = 0.2)'''    

import customtkinter as ctk
from PIL import ImageFont, Image
from define import *
from customtkinter import CTkFont

class Get_Started_Interface(ctk.CTkFrame):
    
    def __init__(self, root):
        super().__init__(root)
        self.configure(fg_color = COLOR_SALT)
        self.parent = root
        header_font = CTkFont(family=HEADER_FONT, size=50)
        desciption_font = CTkFont(family=DESCRIPTION_FONT, size=30)  
        self.template_screen = None 

        frame = ctk.CTkFrame(self, 
                             bg_color=COLOR_SALT, 
                             fg_color=COLOR_PINEGREEN, 
                             corner_radius=20)
        frame.pack(pady=20, padx=20, fill="both")

        header_label = ctk.CTkLabel(master=frame, 
                                    text="PHOTO BOOTH", 
                                    font=header_font,
                                    text_color=COLOR_SALT)
        header_label.grid(column = 0, row = 0, padx = 40, pady = (70, 0))

        description_label = ctk.CTkLabel(master=frame, 
                                    text="Sản phẩm trưng bày",  
                                    font=desciption_font,
                                    text_color=COLOR_SALT)
        description_label.grid(column = 0, row = 1, padx = 40, pady = (0, 130), sticky = ctk.W)

        smt = ctk.CTkLabel(master=frame,
                            text="cái gì đó",
                            width=260,
                            height=200,  
                            font=desciption_font,
                            fg_color=COLOR_SALT,
                            text_color=COLOR_SKYBLUE,
                            corner_radius=10)
        smt.grid(column = 1, row = 0, padx = (150, 0), pady = (80, 0), rowspan = 2)

        self.destroy_window_button = ctk.CTkButton(self,
                                                   text = '',
                                                   fg_color='transparent',
                                                   bg_color='transparent',
                                                   width=30,
                                                   height=30,
                                                   hover_color='gray',
                                                   image = ctk.CTkImage(light_image=Image.open('DataStorage/Icons/quit_button.png'),
                                                                        dark_image=Image.open('DataStorage/Icons/quit_button.png'),
                                                                        size = (50, 50)),
                                                   command = self.parent.destroy)
        self.destroy_window_button.place(relx = 1, rely = 0, anchor = 'ne')

        def change_page():
            self.configure(fg_color = COLOR_DOGWOOD)
            button.configure(fg_color = COLOR_DOGWOOD)

        button = ctk.CTkButton(master=self,
                               width=1024,
                               height=300,
                               text="tap to start!", 
                               text_color=COLOR_SKYBLUE,
                               font=header_font,
                               bg_color=COLOR_SALT,
                               fg_color=COLOR_SALT,
                               hover=False,
                               command=change_page)
        button. pack()

    def Next_To_Template_Screen(self, event):
        self.parent.unbind_all('<Button>')
        self.pack_forget()
        self.template_screen.pack(expand = True, fill = 'both')
