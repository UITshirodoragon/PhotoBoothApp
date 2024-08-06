import customtkinter as ctk
from PIL import Image
import Image_Capture_Interface as ICI
import glob

class User_Image_Gallery(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        #Create captured images frame
        self.captured_images_frame = ctk.CTkFrame(self,
                                                   bg_color='black',
                                                   width=self.parent.winfo_width() * 0.3,
                                                   height = self.parent.winfo_height()) #main frame
        self.captured_images_label = ctk.CTkLabel(self.captured_images_frame,
                                                  text = 'Photos galllery',
                                                  font = ('Arial', 40))
        self.captured_images_frame.rowconfigure((1, 2, 3, 4, 5), weight=2, uniform='a')
        self.captured_images_frame.rowconfigure((0, 6), weight=1, uniform='a')
        self.captured_images_frame.columnconfigure((0 ,1, 2, 3, 4, 5), weight=1, uniform='a')
        self.captured_images_label.grid(row = 0, column = 0, columnspan = 5, sticky='nsew')
        self.captured_images_frame.place(relx = 1, rely = 0, relheight=1, relwidth = 0.3, anchor = 'ne')
    
        #Notify that no images are captured label
        self.no_image_label = ctk.CTkLabel(self.captured_images_frame,
                          text = 'No image captured yet',
                          font = ('Arial', 20))

        #Display images in gallery
        self.gallery_images_display()

    def gallery_images_display(self):
        #Get all captured image name
        image_paths = glob.glob('DataStorage/ImageGallery/*.png')
        #Change folder path format
        for path in image_paths:
             path.replace('\\', '/')
        #Image count variable
        img_index = len(image_paths) - 1
        if img_index < 0:
           self.no_image_label.grid(row = 3, column = 0, columnspan = 5, sticky = 'nsew')
        else:
            self.no_image_label.grid_forget()
            for i in range(1, 6):
                for j in range(0, 4, 3):
                    ctk.CTkButton(self.captured_images_frame,
                                text ='',
                                bg_color='transparent',
                                fg_color='transparent',
                                hover_color='gray',
                                image=ctk.CTkImage(light_image=Image.open(image_paths[int(img_index)]),
                                                    dark_image=Image.open(image_paths[int(img_index)]),
                                                    size = (150, 100))).grid(row = i,
                                                                            column = j,
                                                                            sticky='nsew',
                                                                            columnspan = 2,
                                                                            padx=1,
                                                                            pady=1)
                    img_index -= 1
                    if img_index < 0:
                        break
                if img_index < 0:
                        break
        
        def Move_forward():
            pass
        def Move_Backward():
            pass
