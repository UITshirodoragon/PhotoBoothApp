import customtkinter as ctk
from PIL import Image, ImageTk
import Image_Capture_Interface as ICI
import glob

class User_Image_Gallery_Interface(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        #back-end
        self.current_page = 1
        self.image_number = 0
        self.export_image_number = 0
        #Create list of button with image
        self.list_image_button = []
        #Create list of image
        self.list_Image = []
        #Create export image list
        self.list_export_image = []
        #Create list of export image check button
        self.export_image_check_button = []
        #Display image canvas
        self.display_image_canvas = ctk.CTkCanvas(self,
                                                  width = 614,
                                                  height = 460)
        self.display_image_canvas.place(relx = 0.05,
                                        rely = 0.1,
                                        width = 614,
                                        height= 460)
        #Create export image frame
        self.export_image_frame = ctk.CTkFrame(self)
        #Create export image label
        self.export_image_label = ctk.CTkLabel(self.export_image_frame,
                                               text = '',
                                               font = ('Arial', 25))
        self.export_image_label.place(relx = 0.01, rely = 0)
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
        self.no_image_is_chosen_label = ctk.CTkLabel(self.display_image_canvas,
                          text = 'No image is chosen yet',
                          font = ('Arial', 20))
        self.no_image_is_chosen_label.place(relx = 0.5, rely = 0.5, anchor = 'center')
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
        if self.image_number != 0:
            for i in range(self.image_number):
                image = ctk.CTkButton(self.captured_images_frame,
                                text ='',
                                width= 153,
                                height = 100,
                                bg_color='transparent',
                                fg_color='transparent',
                                hover_color='gray',
                                image=ctk.CTkImage(light_image=Image.open(self.image_paths[i]),
                                                    dark_image=Image.open(self.image_paths[i]),
                                                    size = (153, 100)),
                                command = lambda imageTk = ImageTk.PhotoImage(Image.open(self.image_paths[i]).resize((614, 460))): self.button_is_chosen(imageTk))
                check_button = ctk.CTkCheckBox(image,
                                               text = '',
                                               width = 15,
                                               height= 15,
                                               onvalue= 1,
                                               offvalue= 0,
                                               command = lambda index = i: self.export_image(index))
                check_button.place(relx = 1, rely = 1, anchor = 'se')
                self.export_image_check_button.append(check_button)
                self.list_image_button.append(image)
                self.list_Image.append(Image.open(self.image_paths[i]))
            #Update image gallery
            self.gallery_images_update()
        else:
            self.no_image_label.grid(row = 3, column = 0, columnspan = 6, sticky = 'nsew')



    def export_image(self, index):
        if self.export_image_check_button[index].get():
            self.export_image_number += 1
            self.export_image_label.configure(text = f'You choosed: {self.export_image_number} image')
            self.list_export_image.append(self.list_Image[index])
            self.export_image_frame.place(relx = 0, rely = 1, relwidth = 1, relheight = 0.14, anchor = 'sw')
        else:
            self.export_image_number -= 1
            if self.export_image_number < 0:
                self.export_image_number = 0
            if self.export_image_number == 0:
                self.export_image_frame.place_forget()
            else:
                self.list_export_image.remove(self.list_Image[index])
                self.export_image_label.configure(text = f'You choose: {self.export_image_number} image')

    def button_is_chosen(self, imageTk):
        self.no_image_is_chosen_label.place_forget()
        self.display_image_canvas.create_image(0, 0, image = imageTk, anchor = 'nw')


    def gallery_images_update(self):
        #Set index and stop number base on forward or backward button pressed
        #Set index number base on current page
        image_index = self.current_page * 10 - 1
        #Constrain index
        if image_index >= self.image_number:
            image_index = self.image_number - 1
        #Set stop loop number
        stop_number = (self.current_page - 1) * 10
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
                                                    columnspan = 3,
                                                    padx=1,
                                                    pady=1)                                              
                image_index -= 1
                if image_index < stop_number:
                    break
            if image_index < stop_number:
                    break
        
    def Move_Forward(self):
        #Check if the next page exist
        if (self.image_number == 0) or (self.image_number <= (self.current_page * 10)):
            return None
        else:
            self.current_page += 1
            self.gallery_images_update()
    
    def Move_Backward(self):
        if (self.current_page == 1) or (self.image_number == 0):
            return None
        else:
            self.current_page -= 1
            self.gallery_images_update()
