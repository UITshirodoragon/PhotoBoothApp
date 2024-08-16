import customtkinter as ctk
from PIL import Image, ImageTk
import glob
import sys
import os

# Đường dẫn tới folder chứa module 
package_controller_path = os.path.abspath(os.path.join('..', 'PhotoBoothApp'))
if package_controller_path not in sys.path:
    sys.path.append(package_controller_path)
from AppInterface.define import *

class User_Image_Gallery_Controller():
    def __init__(self, gallery):
        self.gallery = gallery
        #Image variable
        self.list_Image = []
        self.list_export_image = []
        self.list_export_image_check_button = []
        self.list_image_button = []
        self.list_image_Tk = []
        self.image_number = 0
        self.export_image_number = 0
        self.list_image_paths = None

    def read_image_file(self):
        #Read image
        #Update image paths
        self.list_image_paths = glob.glob('DataStorage/ImageGallery/*.jpg')
        #Change folder path format
        for path in self.list_image_paths:
            path.replace('\\', '/')
        #Get image number
        self.image_number = len(self.list_image_paths)
        if self.image_number != 0:
            for i in range(self.image_number):
                image = ctk.CTkButton(self.gallery.display_image_button_frame,
                                text ='',
                                width = int(self.gallery.parent.winfo_width() * 3 / 32),
                                height=int(self.gallery.parent.winfo_height() * 5 / 48),
                                bg_color=COLOR_SALT, 
                                fg_color='transparent',
                                hover_color=COLOR_MINT,
                                image=ctk.CTkImage(light_image=Image.open(self.list_image_paths[i]),
                                                    dark_image=Image.open(self.list_image_paths[i]),
                                                    size = ((int(self.gallery.parent.winfo_width() * 3 / 32),
                                                            int(self.gallery.parent.winfo_height() * 5 / 48)))),
                                command = lambda index = i: self.gallery.image_is_chosen(index))
                check_button = ctk.CTkCheckBox(image,
                                               text = '',
                                               hover_color=COLOR_SKYBLUE,
                                               bg_color='transparent',
                                               checkmark_color=COLOR_PINEGREEN,
                                               fg_color=COLOR_MINT,
                                               width = 15,
                                               height= 15,
                                               onvalue= 1,
                                               offvalue= 0,
                                               command = lambda index = i: self.export_image(index))
                check_button.place(relx = 1, rely = 1, anchor = 'se')
                self.list_image_Tk.append(ImageTk.PhotoImage(Image.open(self.list_image_paths[i]).resize((int(self.gallery.parent.winfo_width() * 0.6),
                                                                                                        int(self.gallery.parent.winfo_height() * 43 / 60)))))
                self.list_export_image_check_button.append(check_button)
                self.list_image_button.append(image)
                self.list_Image.append(Image.open(self.list_image_paths[i]))


    def export_image(self, index):
        if self.list_export_image_check_button[index].get():
            self.export_image_number += 1
            self.gallery.export_image_label.configure(text = f'You choosed: {self.export_image_number} image')
            self.list_export_image.append(self.list_image_paths[index])
            self.gallery.export_image_frame.place(relx = 0, rely = 1, relwidth = 1, relheight = 0.14, anchor = 'sw')
        else:
            self.export_image_number -= 1
            self.list_export_image.remove(self.list_image_paths[index])
            if self.export_image_number == 0:
                self.gallery.export_image_frame.place_forget()
            else:
                self.gallery.export_image_label.configure(text = f'You choosed: {self.export_image_number} image')

    def Export_Image(self):
        self.gallery.pack_forget()
        self.gallery.template_export.pack(expand = True, fill = 'both')