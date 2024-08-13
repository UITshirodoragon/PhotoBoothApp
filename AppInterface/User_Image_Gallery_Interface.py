import sys
import os

# Đường dẫn tới folder chứa module 
package_controller_path = os.path.abspath(os.path.join('..', 'PhotoBoothApp'))
if package_controller_path not in sys.path:
    sys.path.append(package_controller_path)
import customtkinter as ctk
from PIL import Image, ImageTk
import glob
from AppController import User_Image_Gallery_Controller as UIGC

class User_Image_Gallery_Interface(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = UIGC.User_Image_Gallery_Controller(self)
        self.camera_configuration = None
        self.capture_screen = None
        self.parent = parent
        #Display image canvas
        self.display_image_canvas = ctk.CTkCanvas(self,
                                                  width = int(self.parent.winfo_width() * 0.6),
                                                  height = int(self.parent.winfo_height() * 43 / 60))
        self.display_image_canvas.place(relx = 0.05,
                                        rely = 0.1,
                                        width = int(self.parent.winfo_width() * 0.6),
                                        height= int(self.parent.winfo_height() * 43 / 60))
        #Display image canvas
        self.display_image_canvas = ctk.CTkCanvas(self,
                                                  width = int(self.parent.winfo_width() * 0.6),
                                                  height = int(self.parent.winfo_height() * 43 / 60))
        self.display_image_canvas.place(relx = 0.05,
                                        rely = 0.1,
                                        width = int(self.parent.winfo_width() * 0.6),
                                        height= int(self.parent.winfo_height() * 43 / 60))
        self.display_image_canvas.bind('<Button>', lambda event : self.play_gif())
        self.gif_display_frame_count = 0
        self.display_gif_index = None

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
                                                   width=int(self.parent.winfo_width() * 0.3),
                                                   height = int(self.parent.winfo_height())) #main frame
        self.captured_images_label = ctk.CTkLabel(self.captured_images_frame,
                                                  text = 'Photos galllery',
                                                  font = ('Arial', 40))
        self.captured_images_frame.rowconfigure((1, 2, 3, 4, 5), weight=2, uniform='b')
        self.captured_images_frame.rowconfigure((0, 6), weight=1, uniform='a')
        self.captured_images_frame.columnconfigure((0 ,1), weight=1, uniform='a')
        self.captured_images_label.grid(row = 0, column = 0, columnspan = 2, sticky = 'nsew')
        self.captured_images_frame.place(relx = 1, rely = 0, relheight=1, relwidth = 0.3, anchor = 'ne')
        #Create a tab to view image and gif
        self.tab = ctk.CTkTabview(self.captured_images_frame,
                                  width = self.captured_images_frame.winfo_width(),
                                  height= int(self.captured_images_frame.winfo_height() * 5 / 7),
                                  command = self.toggle_gif_mode)
        self.tab.grid(row = 1, column = 0, rowspan = 5, columnspan = 2, sticky = 'nsew')
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
                                            text = 'Next',
                                            text_color='black',
                                            font = ('Arial', 30),
                                            compound='right',
                                            hover_color='gray',
                                            image = move_forward_button_imageCTk,
                                            command = self.Move_Forward)
        self.move_forward_button.grid(row = 6, column = 1, sticky = 'nsew')

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
                                            text = 'Prev',
                                            text_color='black',
                                            font = ('Arial', 30),
                                            compound='left',
                                            hover_color='gray',
                                            image = move_backward_button_imageCTk,
                                            command = self.Move_Backward)
        self.move_backward_button.grid(row = 6, column = 0, sticky = 'nsew')

         # Return image capture interface
        #Import return_button_image.png
        Return_button_image = Image.open('DataStorage/Icon/return_button_image.png')
        self.Return_button_imageCTk = ctk.CTkImage(light_image=Return_button_image,
                                                dark_image=Return_button_image)
        #Create Return_button
        self.Return_image_capture_button = ctk.CTkButton(self,
                                                            width=50,
                                                            height=50,
                                                            fg_color='transparent',
                                                            bg_color='transparent',
                                                            border_width=0,
                                                            text = '',
                                                            hover_color='gray',
                                                            image = self.Return_button_imageCTk,
                                                            command = self.return_image_capture_interface)
        self.Return_image_capture_button.place(relx = 0, 
                                  rely = 0)
        
        #Create export image button
        export_image_button = ctk.CTkButton(self.export_image_frame,
                                                        text = 'Export',
                                                        width = 100,
                                                        height=40,
                                                        corner_radius= 30,
                                                        font = ('Arial', 20),
                                                        command = self.controller.Export_Image)
        export_image_button.place(relx = 0.01, rely = 0.97, anchor = 'sw')
        
        self.controller.read_image_file()
        if self.controller.image_number != 0:
            #Update image gallery
            self.gallery_images_update()
        else:
            self.no_image_label.grid(row = 2, column = 0, sticky = 'nsew')

        self.controller.read_gif_file()
        if self.controller.gif_number != 0:
            #Update image gallery
            self.gallery_gif_update()
        else:
            self.no_gif_label.grid(row = 2, column = 0, columnspan = 2, sticky = 'nsew')
        
    def gif_is_chosen(self, index):
        self.no_gif_is_chosen_label.place_forget()
        self.display_image_canvas.delete('all')
        self.display_gif_index = index
        self.controller.gif_end_display = False
        for button in self.controller.list_gif_button:
            button.configure(state = 'disable', command = None)
        self.tab.configure(state = 'disabled')
        self.controller.list_gif_button[index].configure(command = None)
        self.display_gif()

    def play_gif(self):
        if ((self.controller.gif_mode == True) and (self.controller.gif_end_display == True) and (self.display_gif_index != None)):
            self.display_image_canvas.unbind('<Button>')
            self.controller.gif_end_display = False
            for button in self.controller.list_gif_button:
                button.configure(state = 'disable', command = None)
            self.tab.configure(state = 'disabled')
            self.display_gif()
        else:
            return None

    def display_gif(self):
        if self.controller.gif_end_display:
            self.display_image_canvas.create_image(0, 0,
                                            image = self.controller.list_gif_Tk[self.display_gif_index][self.gif_display_frame_count],
                                            anchor = 'nw')
            self.display_image_canvas.bind('<Button>', lambda event: self.play_gif())
            self.tab.configure(state = 'normal')
            for i in range(len(self.controller.list_gif_button)):
               self.controller.list_gif_button[i].configure(state = 'normal', command = lambda index = i: self.gif_is_chosen(index))
            self.controller.list_gif_button[self.display_gif_index].configure(command = lambda index = self.display_gif_index: self.gif_is_chosen(index))
            return None
        else:
            self.display_image_canvas.create_image(0, 0,
                                            image = self.controller.list_gif_Tk[self.display_gif_index][self.gif_display_frame_count],
                                            anchor = 'nw')
            self.gif_display_frame_count += 1
            if self.gif_display_frame_count == (len(self.controller.list_gif_Tk[self.display_gif_index]) - 1):
                self.controller.gif_end_display = True
                self.gif_display_frame_count = 0
            self.display_image_canvas.after(25, self.display_gif)

    def gallery_gif_update(self):
        #Set index number base on current page
        gif_index = self.controller.current_gif_page * 10 - 1
        #Constrain index
        if gif_index >= self.controller.gif_number:
            gif_index = self.controller.gif_number - 1
        #Set stop loop number
        stop_number = (self.controller.current_gif_page - 1) * 10
        self.no_gif_label.grid_forget()
        #Forget all gif in frame
        for widget in self.gif_tab.winfo_children():
            if type(widget) is ctk.CTkButton:
                    widget.grid_forget()
        for i in range(0, 5):
            for j in range(0, 2):
                self.controller.list_gif_button[gif_index].grid(row = i,
                                                    column = j,
                                                    sticky='nsew',
                                                    padx=1,
                                                    pady=1)                                              
                gif_index -= 1
                if gif_index < stop_number:
                    break
            if gif_index < stop_number:
                    break
   
    def image_is_chosen(self, imageTk):
        self.no_image_is_chosen_label.place_forget()
        self.display_image_canvas.create_image(0, 0, image = imageTk, anchor = 'nw')

    def gallery_images_update(self):
        #Set index and stop number base on forward or backward button pressed
        #Set index number base on current page
        image_index = self.controller.current_image_page * 10 - 1
        #Constrain index
        if image_index >= self.controller.image_number:
            image_index = self.controller.image_number - 1
        #Set stop loop number
        stop_number = (self.controller.current_image_page - 1) * 10
        self.no_image_label.grid_forget()
        #Forget all image in frame
        for widget in self.image_tab.winfo_children():
            if type(widget) is ctk.CTkButton:
                    widget.grid_forget()
        for i in range(0, 5):
            for j in range(0, 2):
                self.controller.list_image_button[image_index].grid(row = i,
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
        if self.controller.gif_mode:
            if (self.controller.gif_number == 0) or (self.controller.gif_number <= (self.controller.current_gif_page * 10)):
                return None
            else:
                self.controller.current_gif_page += 1
                self.gallery_gif_update()
        else:
            if (self.controller.image_number == 0) or (self.controller.image_number <= (self.controller.current_image_page * 10)):
                return None
            else:
                self.controller.current_image_page += 1
                self.gallery_images_update()
    
    def Move_Backward(self):
         #Check if the next page exist
        if self.controller.gif_mode:
            if (self.controller.gif_number == 0) or (self.controller.gif_number <= (self.controller.current_gif_page * 10)):
                return None
            else:
                self.controller.current_gif_page -= 1
                self.gallery_gif_update()
        else:
            if (self.controller.image_number == 0) or (self.controller.image_number <= (self.controller.current_image_page * 10)):
                return None
            else:
                self.controller.current_image_page -= 1
                self.gallery_images_update()

    def return_image_capture_interface(self):
        if self.controller.gif_end_display:
            if self.controller.gif_mode:
                self.no_gif_is_chosen_label.place(relx = 0.5, rely = 0.5, anchor = 'center')
            else:
                self.no_image_is_chosen_label.place(relx = 0.5, rely = 0.5, anchor = 'center')
            self.display_image_canvas.delete('all')
            if self.camera_configuration.at_start_position == False:
                self.camera_configuration.Toggle_Slide()
            self.pack_forget()
            self.capture_screen.pack(expand = True, fill = 'both')
            self.camera_configuration.place(relx = 0,
                                        rely = -0.2,
                                        relwidth = 1,
                                        relheight = 0.2)
        else:
            return None
        
    def toggle_gif_mode(self):
        if self.controller.gif_mode:
            self.controller.gif_mode = False
            self.export_gif_frame.place_forget()
            self.no_gif_is_chosen_label.place_forget()
            self.display_image_canvas.delete('all')
            self.no_image_is_chosen_label.place(relx = 0.5, rely = 0.5, anchor = 'center')
            if len(self.controller.list_export_image) != 0:
                self.export_image_frame.place(relx = 0, rely = 1, relwidth = 1, relheight = 0.14, anchor = 'sw')
        else:
            self.controller.gif_mode = True
            self.export_image_frame.place_forget()
            self.display_image_canvas.delete('all')
            self.no_image_is_chosen_label.place_forget()
            self.no_gif_is_chosen_label.place(relx = 0.5, rely = 0.5, anchor = 'center')
            if len(self.controller.list_export_gif) != 0:
                self.export_gif_frame.place(relx = 0, rely = 1, relwidth = 1, relheight = 0.14, anchor = 'sw')
        
