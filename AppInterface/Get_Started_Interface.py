import customtkinter as ctk
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
        
        '''Get started interface function'''
    def Next_To_Capture_Screen(self, event):
        self.parent.unbind_all('<Button>')
        self.pack_forget()
        self.capture_screen.pack(expand = True, fill = 'both')
        self.camera_configuration.place(relx = 0,
                                    rely = -0.2,
                                    relwidth = 1,
                                    relheight = 0.2)    