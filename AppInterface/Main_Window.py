import customtkinter as ctk
from PIL import Image
import Get_Started_Interface as GSI
import Image_Capture_Interface as ICI
import User_Image_Gallery as UIG
import Get_Started_Interface as GSI
import Camera_Configuration_Interface as CCI

#Function defenition
'''Get started interface function'''
def Next_To_Capture_Screen(event):
        window.unbind_all('<Button>')
        start_screen.pack_forget()
        capture_screen.pack(expand = True, fill = 'both')
        camera_configuration.place(relx = 0,
                                    rely = -0.2,
                                    relwidth = 1,
                                    relheight = 0.2)

'''Image capture interface function'''
def back_to_start_screen():
        if camera_configuration.at_start_position == False:
              camera_configuration.Move_Up()
        capture_screen.pack_forget()
        start_screen.pack(expand = True, fill = 'both')
        window.bind_all('<Button>', Next_To_Capture_Screen) 

def go_to_gallery():
        capture_screen.pack_forget()
        gallery_screen.pack(expand = True, fill = 'both')

'''User image gallery function'''
def return_image_capture_interface():
        if camera_configuration.at_start_position == False:
              camera_configuration.Move_Up()
        gallery_screen.pack_forget()
        capture_screen.pack(expand = True, fill = 'both')
        camera_configuration.place(relx = 0,
                                    rely = -0.2,
                                    relwidth = 1,
                                    relheight = 0.2)
        
'''Camera configuration function'''
def swap_capture_mode():

    #Swap icon
    global gif_mode
    if gif_mode:
        gif_mode = False
        capture_mode_button.configure(image = capture_screen.capture_button_imageCTk)
        capture_screen.capture_button.configure(image = gif_image_CTk)
    else:
        gif_mode = True
        capture_mode_button.configure(image = gif_image_CTk)
        capture_screen.capture_button.configure(image = capture_screen.capture_button_imageCTk)

def choosing_countdown_mode():
      global is_countdown_button_pressed
      if not is_countdown_button_pressed:
        is_countdown_button_pressed = True
        choosing_frame.place(relx=0.2, rely = 0.3, anchor = 'center')
      else:
            is_countdown_button_pressed = False
            choosing_frame.place_forget()

def choosing_3():
        global current_mode_countdown_time, is_countdown_button_pressed
        current_countdown_mode_button_off.configure(image = countdown_mode_3_imageCTk)
        current_countdown_mode_button_on.configure(image = countdown_mode_3_imageCTk)
        capture_screen.countdown_time = 3
        countdown_mode_3_button.grid_forget()
        countdown_mode_5_button.grid(row = 1, column = 0, sticky = 'nsew', padx = 4, pady = 4)
        countdown_mode_10_button.grid(row = 2, column = 0, sticky = 'nsew', padx = 4, pady = 4)
        is_countdown_button_pressed = False
        choosing_frame.place_forget()

def choosing_5():
        global current_mode_countdown_time, is_countdown_button_pressed
        current_countdown_mode_button_off.configure(image = countdown_mode_5_imageCTk)
        current_countdown_mode_button_on.configure(image = countdown_mode_5_imageCTk)
        capture_screen.countdown_time = 5
        countdown_mode_5_button.grid_forget()
        countdown_mode_3_button.grid(row = 1, column = 0, sticky = 'nsew', padx = 4, pady = 4)
        countdown_mode_10_button.grid(row = 2, column = 0, sticky = 'nsew', padx = 4, pady = 4)
        is_countdown_button_pressed = False
        choosing_frame.place_forget()
      
def choosing_10():
        global current_mode_countdown_time, is_countdown_button_pressed
        current_countdown_mode_button_off.configure(image = countdown_mode_10_imageCTk)
        current_countdown_mode_button_on.configure(image = countdown_mode_10_imageCTk)
        capture_screen.countdown_time = 10
        countdown_mode_10_button.grid_forget()
        countdown_mode_3_button.grid(row = 1, column = 0, sticky = 'nsew', padx = 4, pady = 4)
        countdown_mode_5_button.grid(row = 2, column = 0, sticky = 'nsew', padx = 4, pady = 4)
        is_countdown_button_pressed = False
        choosing_frame.place_forget()

'''Create window'''
window = ctk.CTk()
window.title('Photobooth')
window.geometry('1024x600')
ctk.set_appearance_mode('light')
'''Main code'''

'''Interface'''
start_screen = GSI.Get_Started_Interface(window)
capture_screen = ICI.Image_Capture_Interface(window)
gallery_screen = UIG.User_Image_Gallery(window)
camera_configuration = CCI.Camera_Configuration_Interface(capture_screen, -0.2, 0)

start_screen.pack(expand = True, fill = 'both')
 # Detect press event on the main window to delete the frame
window.bind_all('<Button>', Next_To_Capture_Screen)

'''Image capture widgets'''
# Gallery button
#Import gallery_button_image.png
gallery_button_image = Image.open('DataStorage/Icon/gallery_button_image.png')
gallery_button_imageCTk = ctk.CTkImage(light_image=gallery_button_image,
                                        dark_image=gallery_button_image,
                                        size = (100, 100))

#Create gellery_button
gallery_button = ctk.CTkButton(capture_screen,
                                image = gallery_button_imageCTk,
                                width=80,
                                height=80,
                                fg_color='transparent',
                                bg_color='transparent',
                                border_width=0,
                                text = '',
                                hover_color='gray',
                                command = go_to_gallery)

#Layout gallery_button
gallery_button.place(relx = 0.95,
                    rely = 0.9,
                    anchor = 'center')

# Return to get started interface
#Import return_button_image.png
Return_button_image = Image.open('DataStorage/Icon/return_button_image.png')
Return_button_imageCTk = ctk.CTkImage(light_image=Return_button_image,
                                        dark_image=Return_button_image)

#Create return_button
Return_button = ctk.CTkButton(capture_screen,
                                width=50,
                                height=50,
                                fg_color='transparent',
                                bg_color='transparent',
                                border_width=0,
                                text = '',
                                hover_color='gray',
                                image = Return_button_imageCTk,
                                command = back_to_start_screen)
#Layout return_button
Return_button.place(relx = 0, 
                    rely = 0)

'''User image gallery widgets'''
 # Return image capture interface
#Import return_button_image.png
Return_button_image = Image.open('DataStorage/Icon/return_button_image.png')
Return_button_imageCTk = ctk.CTkImage(light_image=Return_button_image,
                                        dark_image=Return_button_image)
#Create Return_button
Return_button = ctk.CTkButton(gallery_screen,
                                width=50,
                                height=50,
                                fg_color='transparent',
                                bg_color='transparent',
                                border_width=0,
                                text = '',
                                hover_color='gray',
                                image = Return_button_imageCTk,
                                command = return_image_capture_interface)
Return_button.place(relx = 0, 
                    rely = 0)

'''Camera configuration widgets'''
#Capture mode button
#Variable to check what current mode is
gif_mode = True
#Import gif.png
gif_image = Image.open('DataStorage/Icon/gif.png')
gif_image_CTk = ctk.CTkImage(light_image=gif_image,
                                    dark_image=gif_image,
                                    size = (100, 100))

#Create capture mode button
capture_mode_button = ctk.CTkButton(camera_configuration,
                                        width=60,
                                        height=60, 
                                        bg_color='transparent',
                                        fg_color='transparent',
                                        border_width=2,
                                        border_color='black',
                                        text = '',
                                        image = gif_image_CTk,
                                        hover_color='gray',
                                        command = swap_capture_mode)
#Layout capture mode button
capture_mode_button.place(relx = 0.8, rely = 0.5, anchor = 'center')

#Countdown mode frame
#Import countdown mode image
countdown_mode_3_image = Image.open('DataStorage/Icon/set_countdown_3.png')
countdown_mode_5_image = Image.open('DataStorage/Icon/set_countdown_5.png')
countdown_mode_10_image = Image.open('DataStorage/Icon/set_countdown_10.png')

countdown_mode_3_imageCTk = ctk.CTkImage(light_image = countdown_mode_3_image,
                                                dark_image=countdown_mode_3_image,
                                                size = (100, 100))
countdown_mode_5_imageCTk = ctk.CTkImage(light_image = countdown_mode_5_image,
                                                dark_image=countdown_mode_5_image,
                                                size = (100, 100))
countdown_mode_10_imageCTk = ctk.CTkImage(light_image = countdown_mode_10_image,
                                                dark_image=countdown_mode_10_image,
                                                size = (100, 100))

#Create countdown mode button
#Variable to check if the button is pressed or not
is_countdown_button_pressed = False
#Choosing frame
choosing_frame = ctk.CTkFrame(capture_screen)
countdown_mode_3_button = ctk.CTkButton(choosing_frame,
                                        width=60,
                                        height=60, 
                                        bg_color='transparent',
                                        fg_color='transparent',
                                        border_width=2,
                                        border_color='black',
                                        text = '',
                                        image = countdown_mode_3_imageCTk,
                                        hover_color='gray',
                                        command = choosing_3)
countdown_mode_5_button = ctk.CTkButton(choosing_frame,
                                        width=60,
                                        height=60, 
                                        bg_color='transparent',
                                        fg_color='transparent',
                                        border_width=2,
                                        border_color='black',
                                        text = '',
                                        image = countdown_mode_5_imageCTk,
                                        hover_color='gray',
                                        command = choosing_5)
countdown_mode_10_button = ctk.CTkButton(choosing_frame,
                                        width=60,
                                        height=60, 
                                        bg_color='transparent',
                                        fg_color='transparent',
                                        border_width=2,
                                        border_color='black',
                                        text = '',
                                        image = countdown_mode_10_imageCTk,
                                        hover_color='gray',
                                        command = choosing_10)
current_countdown_mode_button_off = ctk.CTkButton(camera_configuration,
                                        width=60,
                                        height=60, 
                                        bg_color='transparent',
                                        fg_color='transparent',
                                        border_width=2,
                                        border_color='black',
                                        text = '',
                                        image = countdown_mode_3_imageCTk,
                                        hover_color='gray',
                                        command = choosing_countdown_mode)
current_countdown_mode_button_on = ctk.CTkButton(choosing_frame,
                                        width=60,
                                        height=60, 
                                        bg_color='transparent',
                                        fg_color='transparent',
                                        border_width=2,
                                        border_color='black',
                                        text = '',
                                        image = countdown_mode_3_imageCTk,
                                        hover_color='gray',
                                        command = choosing_countdown_mode)

#Layout countdown mode button
choosing_frame.columnconfigure(0, weight=1)
choosing_frame.rowconfigure((0, 1, 2), weight=1, uniform= 'a')
current_countdown_mode_button_on.grid(row = 0, column = 0, sticky = 'nsew', padx = 4, pady = 4)
countdown_mode_5_button.grid(row = 1, column = 0, sticky = 'nsew', padx = 4, pady = 4)
countdown_mode_10_button.grid(row = 2, column = 0, sticky = 'nsew', padx = 4, pady = 4)
current_countdown_mode_button_off.place(relx = 0.2, rely = 0.5, anchor = 'center')

window.mainloop()
