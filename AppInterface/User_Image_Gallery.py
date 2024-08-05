import customtkinter as ctk
from PIL import Image
import Image_Capture_Interface as ICI
import os

class User_Image_Gallery(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    '''    #Create captured images frame
        self.captured_images_frame = ctk.CTkFrame(self,
                                                   bg_color='black',
                                                   width=self.parent.winfo_width() * 0.3,
                                                   height = self.parent.winfo_height()) #main frame
        self.captured_images_label = ctk.CTkLabel(self.captured_images_frame,
                                                  text = 'Photos galllery',
                                                  font = ('Arial', 40))
        self.captured_images_frame.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1, uniform='a')
        self.captured_images_frame.columnconfigure((0 ,1), weight=1, uniform='a')
        self.captured_images_label.grid(row = 0, column = 0, columnspan = 2, sticky='nsew')
        self.captured_images_frame.place(relx = 1, rely = 0, relheight=1, relwidth = 0.3, anchor = 'ne')
        image_names = os.listdir('./Captured_images_gallery')
        print(image_names)
        #Image count variable
        img_index = len(image_names) - 1
        for i in range(1,6):
            for j in range(2):
                ctk.CTkButton(self.captured_images_frame,
                            text ='',
                            bg_color='transparent',
                            fg_color='transparent',
                            hover_color='gray',
                            image=ctk.CTkImage(light_image=Image.open('./Captured_images_gallery/' + image_names[img_index]),
                                                dark_image=Image.open('./Captured_images_gallery/' + image_names[img_index]),
                                                size = (150, 100))).grid(row = i,
                                                                         column = j,
                                                                         sticky='nsew',
                                                                         padx=1,
                                                                         pady=1)
                img_index -= 1
                if img_index < 0:
                    break
            if img_index < 0:
                    break'''
