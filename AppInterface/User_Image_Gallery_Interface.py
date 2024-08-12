import customtkinter as ctk
from PIL import Image, ImageTk
import Image_Capture_Interface as ICI
import glob

class User_Image_Gallery_Interface(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.gif_display_frame_count = 0
        self.display_gif_index = None
        self.current_image_page = 1
        self.current_gif_page = 1
        self.image_number = 0
        self.gif_number = 0
        self.gif_end_display = True
        self.gif_mode = False
        self.export_image_number = 0
        self.export_gif_number = 0
        #Create list of button with image
        self.list_gif_button = []
        #Create a list of GIF file to display
        self.list_gif_Tk = []
        self.list_gif = []
        #Create list of export gif check button
        self.export_gif_check_button = []
        #Create list of button with image
        self.list_image_button = []
        #Create list of image
        self.list_Image = []
        #Create export image list
        self.list_export_gif = []
        self.list_export_image = []
        #Create list of export image check button
        self.export_image_check_button = []
        #Display image canvas
        self.display_image_canvas = ctk.CTkCanvas(self,
                                                  width = 614,
                                                  height = 690)
        self.display_image_canvas.place(relx = 0.05,
                                        rely = 0.1,
                                        width = 614,
                                        height= 690)
        self.display_image_canvas.bind('<Button>', lambda event : self.play_gif())
        #Create export image frame
        self.export_image_frame = ctk.CTkFrame(self)
        #Create export image label
        self.export_image_label = ctk.CTkLabel(self.export_image_frame,
                                               text = '',
                                               font = ('Arial', 25))
        self.export_image_label.place(relx = 0.01, rely = 0)
        #Create export gif frame
        self.export_gif_frame = ctk.CTkFrame(self)
        #Create export gif label
        self.export_gif_label = ctk.CTkLabel(self.export_gif_frame,
                                               text = '',
                                               font = ('Arial', 25))
        self.export_gif_label.place(relx = 0.01, rely = 0)
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
        #Create a tab to view image and gif
        self.tab = ctk.CTkTabview(self.captured_images_frame,
                                  width = self.captured_images_frame.winfo_width(),
                                  height= int(self.captured_images_frame.winfo_height() * 5 / 7),
                                  command = self.toggle_gif_mode)
        self.tab.grid(row = 1, column = 0, rowspan = 5, columnspan = 6, sticky = 'nsew')
        self.image_tab = self.tab.add('Image')
        self.image_tab.rowconfigure((0, 1, 2, 3 ,4), weight = 1, uniform='a')
        self.image_tab.columnconfigure((0, 1), weight=1, uniform='a')
        self.gif_tab = self.tab.add('   GIF   ')
        self.gif_tab.rowconfigure((0, 1, 2, 3 ,4), weight = 1, uniform='a')
        self.gif_tab.columnconfigure((0, 1), weight=1, uniform='a')
        self.no_gif_label = ctk.CTkLabel(self.gif_tab,
                                        text = 'No GIF captured yet',
                                        font = ('Arial', 20))
        #Notify that no images are captured label
        self.no_image_label = ctk.CTkLabel(self.image_tab,
                          text = 'No image captured yet',
                          font = ('Arial', 20))
        self.no_image_is_chosen_label = ctk.CTkLabel(self.display_image_canvas,
                          text = 'No image is chosen yet',
                          font = ('Arial', 20))
        self.no_gif_is_chosen_label = ctk.CTkLabel(self.display_image_canvas,
                          text = 'No GIF is chosen yet',
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
        #Get all image then transfer into button
        if self.image_number != 0:
            for i in range(self.image_number):
                image = ctk.CTkButton(self.image_tab,
                                text ='',
                                width= 153,
                                height = 100,
                                bg_color='transparent',
                                fg_color='transparent',
                                hover_color='gray',
                                image=ctk.CTkImage(light_image=Image.open(self.image_paths[i]),
                                                    dark_image=Image.open(self.image_paths[i]),
                                                    size = (153, 100)),
                                command = lambda imageTk = ImageTk.PhotoImage(Image.open(self.image_paths[i]).resize((614, 460))): self.image_is_chosen(imageTk))
                check_image_button = ctk.CTkCheckBox(image,
                                               text = '',
                                               width = 15,
                                               height= 15,
                                               onvalue= 1,
                                               offvalue= 0,
                                               command = lambda index = i: self.export_image(index))
                check_image_button.place(relx = 1, rely = 1, anchor = 'se')
                self.export_image_check_button.append(check_image_button)
                self.list_image_button.append(image)
                self.list_Image.append(Image.open(self.image_paths[i]))
            #Update image gallery
            self.gallery_images_update()
        else:
            self.no_image_label.grid(row = 2, column = 0, columnspan = 2, sticky = 'nsew')
        
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
                frame_Tk = ImageTk.PhotoImage(gif_file.copy().resize((614, 460)))
                frames.append(frame)
                frames_Tk.append(frame_Tk)
            self.list_gif_Tk.append(frames_Tk)
            self.list_gif.append(frames)

        if self.gif_number != 0:
            for i in range(self.gif_number):
                gif = ctk.CTkButton(self.gif_tab,
                                text ='',
                                width= 153,
                                height = 100,
                                bg_color='transparent',
                                fg_color='transparent',
                                hover_color='gray',
                                image=ctk.CTkImage(light_image=self.list_gif[i][0],
                                                    dark_image=self.list_gif[i][0],
                                                    size = (153, 100)),
                                command = lambda index = i: self.gif_is_chosen(index))
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
            #Update image gallery
            self.gallery_gif_update()
        else:
            self.no_gif_label.grid(row = 2, column = 0, columnspan = 2, sticky = 'nsew')

    def toggle_gif_mode(self):
        if self.gif_mode:
            self.gif_mode = False
            self.export_gif_frame.place_forget()
            self.no_gif_is_chosen_label.place_forget()
            self.display_image_canvas.delete('all')
            self.no_image_is_chosen_label.place(relx = 0.5, rely = 0.5, anchor = 'center')
            if len(self.list_export_image) != 0:
                self.export_image_frame.place(relx = 0, rely = 1, relwidth = 1, relheight = 0.14, anchor = 'sw')
        else:
            self.gif_mode = True
            self.export_image_frame.place_forget()
            self.display_image_canvas.delete('all')
            self.no_image_is_chosen_label.place_forget()
            self.no_gif_is_chosen_label.place(relx = 0.5, rely = 0.5, anchor = 'center')
            if len(self.list_export_gif) != 0:
                self.export_gif_frame.place(relx = 0, rely = 1, relwidth = 1, relheight = 0.14, anchor = 'sw')

    def export_image(self, index):
        if self.export_image_check_button[index].get():
            self.export_image_number += 1
            self.export_image_label.configure(text = f'You choosed: {self.export_image_number} image')
            self.list_export_image.append(self.list_Image[index])
            self.export_image_frame.place(relx = 0, rely = 1, relwidth = 1, relheight = 0.14, anchor = 'sw')
        else:
            self.export_image_number -= 1
            self.list_export_image.remove(self.list_Image[index])
            if self.export_image_number == 0:
                self.export_image_frame.place_forget()
            else:
                self.export_image_label.configure(text = f'You choosed: {self.export_image_number} image')

    def export_gif(self, index):
        if self.export_gif_check_button[index].get():
            self.export_gif_number += 1
            self.export_gif_label.configure(text = f'You choosed: {self.export_gif_number} gif')
            self.list_export_gif.append(self.list_gif[index])
            self.export_gif_frame.place(relx = 0, rely = 1, relwidth = 1, relheight = 0.14, anchor = 'sw')
        else:
            self.export_gif_number -= 1
            self.list_export_gif.remove(self.list_gif[index])
            if self.export_gif_number == 0:
                self.export_gif_frame.place_forget()
            else:
                self.export_gif_label.configure(text = f'You choosed: {self.export_gif_number} gif')

    def image_is_chosen(self, imageTk):
        self.no_image_is_chosen_label.place_forget()
        self.display_image_canvas.create_image(0, 0, image = imageTk, anchor = 'nw')

    def gif_is_chosen(self, index):
        self.no_gif_is_chosen_label.place_forget()
        self.display_gif_index = index
        self.gif_end_display = False
        self.tab.configure(state = 'disabled')
        self.list_gif_button[index].configure(command = None)
        self.display_gif()

    def play_gif(self):
        if ((self.gif_mode == True) and (self.gif_end_display == True) and (self.display_gif_index != None)):
            self.display_image_canvas.unbind('<Button>')
            self.gif_end_display = False
            self.tab.configure(state = 'disabled')
            self.display_gif()
        else:
            return None

    def display_gif(self):
        if self.gif_end_display:
            self.display_image_canvas.create_image(0, 0,
                                            image = self.list_gif_Tk[self.display_gif_index][self.gif_display_frame_count],
                                            anchor = 'nw')
            self.display_image_canvas.bind('<Button>', lambda event: self.play_gif())
            self.tab.configure(state = 'normal')
            self.list_gif_button[self.display_gif_index].configure(command = lambda index = self.display_gif_index: self.gif_is_chosen(index))
            return None
        else:
            self.display_image_canvas.create_image(0, 0,
                                            image = self.list_gif_Tk[self.display_gif_index][self.gif_display_frame_count],
                                            anchor = 'nw')
            self.gif_display_frame_count += 1
            if self.gif_display_frame_count == (len(self.list_gif_Tk[self.display_gif_index]) - 1):
                self.gif_end_display = True
                self.gif_display_frame_count = 0
            self.display_image_canvas.after(25, self.display_gif)

    def gallery_gif_update(self):
        #Set index number base on current page
        gif_index = self.current_gif_page * 10 - 1
        #Constrain index
        if gif_index >= self.gif_number:
            gif_index = self.gif_number - 1
        #Set stop loop number
        stop_number = (self.current_gif_page - 1) * 10
        self.no_gif_label.grid_forget()
        #Forget all gif in frame
        for widget in self.gif_tab.winfo_children():
            if type(widget) is ctk.CTkButton:
                    widget.grid_forget()
        for i in range(0, 5):
            for j in range(0, 2):
                self.list_gif_button[gif_index].grid(row = i,
                                                    column = j,
                                                    sticky='nsew',
                                                    padx=1,
                                                    pady=1)                                              
                gif_index -= 1
                if gif_index < stop_number:
                    break
            if gif_index < stop_number:
                    break

    def gallery_images_update(self):
        #Set index and stop number base on forward or backward button pressed
        #Set index number base on current page
        image_index = self.current_image_page * 10 - 1
        #Constrain index
        if image_index >= self.image_number:
            image_index = self.image_number - 1
        #Set stop loop number
        stop_number = (self.current_image_page - 1) * 10
        self.no_image_label.grid_forget()
        #Forget all image in frame
        for widget in self.image_tab.winfo_children():
            if type(widget) is ctk.CTkButton:
                    widget.grid_forget()
        for i in range(0, 5):
            for j in range(0, 2):
                self.list_image_button[image_index].grid(row = i,
                                                    column = j,
                                                    sticky='nsew',
                                                    padx=1,
                                                    pady=1)                                              
                image_index -= 1
                if image_index < stop_number:
                    break
            if image_index < stop_number:
                    break
        
    def Move_Forward(self):
        #Check if the next page exist
        if self.gif_mode:
            if (self.gif_number == 0) or (self.gif_number <= (self.current_gif_page * 10)):
                return None
            else:
                self.current_gif_page += 1
                self.gallery_gif_update()
        else:
            if (self.image_number == 0) or (self.image_number <= (self.current_image_page * 10)):
                return None
            else:
                self.current_image_page += 1
                self.gallery_images_update()
    
    def Move_Backward(self):
         #Check if the next page exist
        if self.gif_mode:
            if (self.gif_number == 0) or (self.gif_number <= (self.current_gif_page * 10)):
                return None
            else:
                self.current_gif_page -= 1
                self.gallery_gif_update()
        else:
            if (self.image_number == 0) or (self.image_number <= (self.current_image_page * 10)):
                return None
            else:
                self.current_image_page -= 1
                self.gallery_images_update()
