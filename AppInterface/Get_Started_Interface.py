import customtkinter as ctk
import Image_Capture_Interface as ICI

class Get_Started_Interface(ctk.CTkFrame):
    def __init__(self, parent):
        # inherit from CTkFrame
        super().__init__(master = parent)
        self.state = True # state of object: True = activate, False = deactivate
        self.parent = parent

        # 'Press to start' label
        self.label = ctk.CTkLabel(self,
                                   text = 'Press to start',
                                   font = ('Arial', 20))

        # Layout
        # Put the label in the center of the frame
        self.label.place(relx = 0.5,
                          rely = 0.5,
                         anchor = 'center')