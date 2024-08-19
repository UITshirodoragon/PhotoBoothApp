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
        self.list_export_image_button = []
        self.list_export_image_paths = []
        self.list_export_image_check_button = []
        self.list_image_button = []
        self.list_image_Tk = []
        self.image_number = 0
        self.export_image_number = 0
        self.list_image_paths = []

    def read_image_file(self):
        #Read image
        #Update image paths
        self.list_image_paths = glob.glob('DataStorage/ImageGallery/*.png')
        #Change folder path format
        for path in self.list_image_paths:
            path.replace('\\', '/')
        #Get image number
        self.image_number = len(self.list_image_paths)
        print(self.image_number)
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


    def export_image(self, index):
        if self.list_export_image_check_button[index].get():
            self.export_image_number += 1
            self.list_export_image_paths.append(self.list_image_paths[index])
            self.list_export_image_button.append(self.list_image_button[index])
            self.gallery.confirm_frame.place(relx = 0, rely = 1, relwidth = 1, relheight = 0.14, anchor = 'sw')
        else:
            self.export_image_number -= 1
            self.gallery.delete_chosen_image_order()
            self.list_export_image_paths.remove(self.list_image_paths[index])
            self.list_export_image_button.remove(self.list_image_button[index])
            if self.export_image_number == 0:
                self.gallery.confirm_frame.place_forget()

        self.gallery.update_confirm_frame()
        self.gallery.update_chosen_image_order()

    def Confirm(self):
        self.gallery.template_screen.controller.export_template(self.gallery.template_screen.get_template())
        self.gallery.pack_forget()
        temp = Image.open('DataStorage/ImageGallery/final.png')
        w, h = temp.size
        template_img = ctk.CTkImage(light_image=temp, dark_image=temp, size = (500/h*w, 500))
        self.gallery.template_edit.display_final_frame.configure(image=template_img)
        self.gallery.template_edit.pack(expand = True, fill = 'both')