import customtkinter as ctk
from PIL import Image
import Image_Capture_Interface as ICI
import glob

class User_Image_Gallery(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.current_page = 1
        self.image_number = 0
        self.is_forward_button_pressed = False
        self.is_backward_button_pressed = False
        self.is_any_image_presenting = False
        #Create list of button with image
        self.list_image_button = []
        #Create list of button state
        self.is_any_image_presenting = []
        #Display image label
        self.display_image_label = ctk.CTkLabel(self,
                                                text = '',
                                                fg_color='transparent',
                                                bg_color='transparent')
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
        self.captured_images_label.grid(row = 0, column = 0, columnspan = 6, sticky = 'nsew')
        self.captured_images_frame.place(relx = 1, rely = 0, relheight=1, relwidth = 0.3, anchor = 'ne')
    
        #Notify that no images are captured label
        self.no_image_label = ctk.CTkLabel(self.captured_images_frame,
                          text = 'No image captured yet',
                          font = ('Arial', 20))
        
        #Move forward button
        #Import right_arrow.png
        move_forward_button_image = Image.open('DataStorage/Icon/right_arrow.png')
        move_forward_button_imageCTk = ctk.CTkImage(light_image=move_forward_button_image,
                                                    dark_image=move_forward_button_image,
                                                    size = (50, 50)) 
        #Create move forward button
        self.move_forward_button = ctk.CTkButton(self.captured_images_frame,
                                            fg_color='transparent',
                                            bg_color='transparent',
                                            border_width=0,
                                            text = '',
                                            hover_color='gray',
                                            image = move_forward_button_imageCTk,
                                            command = self.Move_Forward)
        self.move_forward_button.grid(row = 6, column = 3, columnspan = 3, sticky = 'nsew')

        #Move backward button
        #Import right_arrow.png
        move_backward_button_image = Image.open('DataStorage/Icon/left_arrow.png')
        move_backward_button_imageCTk = ctk.CTkImage(light_image=move_backward_button_image,
                                                    dark_image=move_backward_button_image,
                                                    size = (50, 50)) 
        #Create move backward button
        self.move_backward_button = ctk.CTkButton(self.captured_images_frame,
                                            fg_color='transparent',
                                            bg_color='transparent',
                                            border_width=0,
                                            text = '',
                                            hover_color='gray',
                                            image = move_backward_button_imageCTk,
                                            command = self.Move_Backward)
        self.move_backward_button.grid(row = 6, column = 0, columnspan = 3,sticky = 'nsew')
        #Update images
        #Update image paths
        self.image_paths = glob.glob('DataStorage/ImageGallery/*.png')
        #Change folder path format
        for path in self.image_paths:
            path.replace('\\', '/')
        #Get image number
        self.image_number = len(self.image_paths)
        for i in range(self.image_number):
            image = ctk.CTkButton(self.captured_images_frame,
                            text ='',
                            bg_color='transparent',
                            fg_color='transparent',
                            hover_color='gray',
                            image=ctk.CTkImage(light_image=Image.open(self.image_paths[i]),
                                                dark_image=Image.open(self.image_paths[i]),
                                                size = (150, 100)),
                                                command = self.display_image)
            self.is_any_image_presenting.append(False)
            self.list_image_button.append(image)
        #Update images in gallery
        self.gallery_images_update()
            
    def display_image(self):
        if self.is_any_image_presenting:
            self.display_image_label.place_forget()
        else:
            self.display_image_label.place(relx = 0, rely = 0.1)
            for state_index in range(len(self.is_any_image_presenting)):
                if state_index:
                   self.display_image_label.configure(image = self.list_image_button[state_index]._image)

    def gallery_images_update(self):
        #Set index and stop number base on forward or backward button pressed
        #Set index number base on current page
        image_index = self.current_page * 10 - 1
        #Constrain index
        if image_index >= self.image_number:
            image_index = self.image_number - 1
        #Set stop loop number
        stop_number = (self.current_page - 1) * 10
        if self.image_number == 0:
           self.no_image_label.grid(row = 3, column = 0, columnspan = 6, sticky = 'nsew')
        else:
            self.no_image_label.grid_forget()
            #Forget all image in frame
            for widget in self.captured_images_frame.winfo_children():
                if type(widget) is ctk.CTkButton:
                        widget.grid_forget()
            self.move_forward_button.grid(row = 6, column = 3, columnspan = 3, sticky = 'nsew')
            self.move_backward_button.grid(row = 6, column = 0, columnspan = 3,sticky = 'nsew')
            for i in range(1, 6):
                for j in range(0, 4, 3):
                    self.list_image_button[image_index].grid(row = i,
                                                        column = j,
                                                        sticky='nsew',
                                                        columnspan = 2)
                                                        
                    image_index -= 1
                    if image_index < stop_number:
                        break
                if image_index < stop_number:
                        break
        
    def Move_Forward(self):
        #Check if the next page exist
        if self.image_number <= (self.current_page * 10):
            self.is_forward_button_pressed = False
            self.current_page -= 1
            return None
        if self.image_number == 0:
            return None
        self.current_page += 1
        self.is_forward_button_pressed = True
        self.gallery_images_update()
    
    def Move_Backward(self):
        if (self.current_page == 1) or (self.image_number == 0):
            return None
        self.current_page -= 1
        self.is_backward_button_pressed = True
        self.gallery_images_update()
