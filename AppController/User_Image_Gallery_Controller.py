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
        self.current_image_page = 1
        self.list_image_paths = []

        #GIF variable
        self.current_gif_page = 1
        self.gif_number = 0
        self.gif_end_display = True
        self.gif_mode = False
        self.export_gif_number = 0
        self.list_gif_button = []
        self.list_gif_Tk = []
        self.list_gif = []
        self.export_gif_check_button = []
        self.list_export_gif = []
        
    def read_image_file(self):
        #Read image
        #Update image paths
        self.list_image_paths = glob.glob(f'DataStorage/ImageGallery/user{self.gallery.end_screen.controller.number_of_uses}/*.png')
        #Change folder path format
        for path in self.list_image_paths:
            path.replace('\\', '/')
        #Get image number
        self.image_number = len(self.list_image_paths)
        print(self.image_number)
        if self.image_number != 0:
            for i in range(self.image_number):
                image = ctk.CTkButton(self.gallery.image_tab,
                                text ='',
                                width = int(self.gallery.parent.winfo_width() * 3 / 32),
                                height=int(self.gallery.parent.winfo_height() * 5 / 48),
                                bg_color=COLOR_SALT, 
                                fg_color='transparent',
                                hover_color=COLOR_MINT,
                                image=ctk.CTkImage(light_image=Image.open(self.list_image_paths[i]),
                                                    dark_image=Image.open(self.list_image_paths[i]),
                                                    size = ((int(self.gallery.parent.winfo_width() * 21 / 160),
                                                            int(self.gallery.parent.winfo_height() * 7 / 48)))),
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

    def read_gif_file(self):
         #Get all gif then transfer into button
        self.gif_paths = glob.glob(f'DataStorage/GIFGallery/user{self.gallery.end_screen.controller.number_of_uses}/*.gif')
        for gif in self.gif_paths:
            gif.replace('\\', '/')
        self.gif_number = len(self.gif_paths)
        #Get frames of each gif file and put in a list
        for i in range(self.gif_number):
            gif_file = Image.open(self.gif_paths[i])
            frames_Tk = []
            frames = []
            for index in range(gif_file.n_frames):
                gif_file.seek(index)
                frame = gif_file.copy()
                frame_Tk = ImageTk.PhotoImage(gif_file.copy().resize((int(self.gallery.parent.winfo_width() * 0.6),
                                                                    int(self.gallery.parent.winfo_height() * 43 / 60))))
                frames.append(frame)
                frames_Tk.append(frame_Tk)
            self.list_gif_Tk.append(frames_Tk)
            self.list_gif.append(frames)

        if self.gif_number != 0:
            for i in range(self.gif_number):
                gif = ctk.CTkButton(self.gallery.gif_tab,
                                text ='',
                               width = int(self.gallery.parent.winfo_width()  * 3 / 32),
                                height=int(self.gallery.parent.winfo_height() * 5 / 48),
                                bg_color=COLOR_SALT, 
                                fg_color='transparent',
                                hover_color=COLOR_MINT,
                                image=ctk.CTkImage(light_image=self.list_gif[i][0],
                                                    dark_image=self.list_gif[i][0],
                                                    size = (int(self.gallery.parent.winfo_width() * 21 / 160),
                                                            int(self.gallery.parent.winfo_height() * 7 / 48))),
                                command = lambda index = i: self.gallery.gif_is_chosen(index))
                check_gif_button = ctk.CTkCheckBox(gif,
                                                text = '',
                                               hover_color=COLOR_SKYBLUE,
                                               bg_color='transparent',
                                               checkmark_color=COLOR_PINEGREEN,
                                               fg_color=COLOR_MINT,
                                               width = 15,
                                               height= 15,
                                               onvalue= 1,
                                               offvalue= 0,
                                               command = lambda index = i: self.export_gif(index))
                check_gif_button.place(relx = 1, rely = 1, anchor = 'se')
                self.export_gif_check_button.append(check_gif_button)
                self.list_gif_button.append(gif)

    def export_gif(self, index):
        if self.export_gif_check_button[index].get():
            self.export_gif_number += 1
            self.gallery.export_gif_label.configure(text = f'You choosed: {self.export_gif_number} gif')
            self.list_export_gif.append(self.list_gif[index])
            self.gallery.export_gif_frame.place(relx = 0, rely = 1, relwidth = 1, relheight = 0.14, anchor = 'sw')
        else:
            self.export_gif_number -= 1
            self.list_export_gif.remove(self.list_gif[index])
            if self.export_gif_number == 0:
                self.gallery.export_gif_frame.place_forget()
            else:
                self.gallery.export_gif_label.configure(text = f'You choosed: {self.export_gif_number} gif')


    def confirm_image(self):
        if self.gif_mode:
                for button in self.gallery.image_tab.winfo_children():
                    if button._bg_color == COLOR_MINT:
                        button.configure(bg_color = COLOR_SALT)
                self.gallery.no_gif_is_chosen_label.place(relx = 0.5, rely = 0.5, anchor = 'center')
        else:
            for button in self.gallery.image_tab.winfo_children():
                    if button._bg_color == COLOR_MINT:
                        button.configure(bg_color = COLOR_SALT)
            self.gallery.no_image_is_chosen_label.place(relx = 0.5, rely = 0.5, anchor = 'center')
            self.gallery.display_image_canvas.delete('all')
        self.gallery.template_screen.controller.export_template(self.gallery.template_screen.get_template())
        self.gallery.pack_forget()
        temp = Image.open(f'DataStorage/ImageGallery/user{self.gallery.end_screen.controller.number_of_uses}/final.png')
        w, h = temp.size
        template_img = ctk.CTkImage(light_image=temp, dark_image=temp, size = (500/h*w, 500))
        self.gallery.template_edit.display_final_frame.configure(image=template_img)
        self.gallery.template_edit.pack(expand = True, fill = 'both')
