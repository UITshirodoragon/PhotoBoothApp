import customtkinter as ctk
from PIL import Image, ImageTk
import glob

class User_Image_Gallery_Controller():
    def __init__(self, gallery):
        self.gallery = gallery
        #Image variable
        self.list_Image = []
        self.list_export_image = []
        self.list_export_image_check_button = []
        self.list_image_button = []
        self.image_number = 0
        self.export_image_number = 0
        self.current_image_page = 1

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
        image_paths = glob.glob('DataStorage/ImageGallery/*.png')
        #Change folder path format
        for path in image_paths:
            path.replace('\\', '/')
        #Get image number
        self.image_number = len(image_paths)
        if self.image_number != 0:
            for i in range(self.image_number):
                image = ctk.CTkButton(self.gallery.image_tab,
                                text ='',
                                width = int(self.gallery.parent.winfo_width() * 0.15),
                                height=int(self.gallery.parent.winfo_height() / 6),
                                bg_color='transparent', 
                                fg_color='transparent',
                                hover_color='gray',
                                image=ctk.CTkImage(light_image=Image.open(image_paths[i]),
                                                    dark_image=Image.open(image_paths[i]),
                                                    size = ((int(self.gallery.parent.winfo_width() * 0.15),
                                                            int(self.gallery.parent.winfo_height() / 6)))),
                                command = lambda imageTk = ImageTk.PhotoImage(Image.open(image_paths[i]).resize((int(self.gallery.parent.winfo_width() * 0.6),
                                                                                                                int(self.gallery.parent.winfo_height() * 43 / 60)))): self.gallery.image_is_chosen(imageTk))
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

    def read_gif_file(self):
         #Get all gif then transfer into button
        self.gif_paths = glob.glob('DataStorage/GIFGallery/*.gif')
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
                               width = int(self.gallery.parent.winfo_width() * 0.15),
                                height=int(self.gallery.parent.winfo_height() / 6),
                                bg_color='transparent',
                                fg_color='transparent',
                                hover_color='gray',
                                image=ctk.CTkImage(light_image=self.list_gif[i][0],
                                                    dark_image=self.list_gif[i][0],
                                                    size = (int(self.gallery.parent.winfo_width() * 0.15),
                                                            int(self.gallery.parent.winfo_height() / 6))),
                                command = lambda index = i: self.gallery.gif_is_chosen(index))
                check_gif_button = ctk.CTkCheckBox(gif,
                                               text = '',
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
                self.export_gif_frame.place_forget()
            else:
                self.gallery.export_gif_label.configure(text = f'You choosed: {self.export_gif_number} gif')


    def Export_Image(self):
        pass