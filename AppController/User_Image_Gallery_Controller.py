import customtkinter as ctk
from PIL import Image, ImageTk
import glob

class User_Image_Gallery_Controller():
    def __init__(self, gallery):
        self.gallery = gallery
        self.list_Image = []
        self.list_export_image = []
        self.list_export_image_check_button = []
        self.list_image_button = []
        self.image_number = 0
        self.export_image_number = 0

    def read_file(self):
        #Update images
        #Update image paths
        image_paths = glob.glob('DataStorage/ImageGallery/*.png')
        #Change folder path format
        for path in image_paths:
            path.replace('\\', '/')
        #Get image number
        self.image_number = len(image_paths)
        if self.image_number != 0:
            for i in range(self.image_number):
                image = ctk.CTkButton(self.gallery.captured_images_frame,
                                text ='',
                                width = int(self.gallery.parent.winfo_width() * 3 / 32),
                                height=int(self.gallery.parent.winfo_height() * 5 / 48),
                                bg_color='transparent', 
                                fg_color='transparent',
                                hover_color='gray',
                                image=ctk.CTkImage(light_image=Image.open(image_paths[i]),
                                                    dark_image=Image.open(image_paths[i]),
                                                    size = ((int(self.gallery.parent.winfo_width() * 3 / 32),
                                                            int(self.gallery.parent.winfo_height() * 5 / 48)))),
                                command = lambda imageTk = ImageTk.PhotoImage(Image.open(image_paths[i]).resize((int(self.gallery.parent.winfo_width() * 0.6),
                                                                                                                int(self.gallery.parent.winfo_height() * 43 / 60)))): self.gallery.button_is_chosen(imageTk))
                check_button = ctk.CTkCheckBox(image,
                                               text = '',
                                               width = 15,
                                               height= 15,
                                               onvalue= 1,
                                               offvalue= 0,
                                               command = lambda index = i: self.export_image(index))
                check_button.place(relx = 1, rely = 1, anchor = 'se')
                self.list_export_image_check_button.append(check_button)
                self.list_image_button.append(image)
                self.list_Image.append(Image.open(image_paths[i]))

    def export_image(self, index):
        if self.list_export_image_check_button[index].get():
            self.export_image_number += 1
            self.gallery.export_image_label.configure(text = f'You choosed: {self.export_image_number} image')
            self.list_export_image.append(self.list_Image[index])
            self.gallery.export_image_frame.place(relx = 0, rely = 1, relwidth = 1, relheight = 0.14, anchor = 'sw')
        else:
            self.export_image_number -= 1
            self.list_export_image.remove(self.list_Image[index])
            if self.export_image_number == 0:
                self.gallery.export_image_frame.place_forget()
            else:
                self.gallery.export_image_label.configure(text = f'You choosed: {self.export_image_number} image')

    def Export_Image(self):
        pass