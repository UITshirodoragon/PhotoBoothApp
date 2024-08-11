import customtkinter as ctk
from PIL import Image, ImageTk
import Get_Started_Interface as GSI
import Image_Capture_Interface as ICI
import User_Image_Gallery_Interface as UIG
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
              camera_configuration.Move_Up(toggle_button)
              choosing_frame.place_forget()
        capture_screen.pack_forget()
        start_screen.pack(expand = True, fill = 'both')
        window.bind_all('<Button>', Next_To_Capture_Screen) 

def go_to_gallery():
        capture_screen.pack_forget()
        choosing_frame.place_forget()
        gallery_screen.pack(expand = True, fill = 'both')

'''User image gallery function'''
def return_image_capture_interface():
        gallery_screen.no_image_is_chosen_label.place(relx = 0.5, rely = 0.5, anchor = 'center')
        gallery_screen.display_image_canvas.delete('all')
        if camera_configuration.at_start_position == False:
              camera_configuration.Move_Up(toggle_button)
        gallery_screen.pack_forget()
        capture_screen.pack(expand = True, fill = 'both')
        camera_configuration.place(relx = 0,
                                    rely = -0.2,
                                    relwidth = 1,
                                    relheight = 0.2)
        
def Export_Image():
       pass
        
def capture_and_update_gallery():
        if capture_screen.is_captured_yet:
                capture_screen.is_captured_yet = False
                #Enable capture button
                capture_button.configure(state = 'normal', command = capture_and_update_gallery)
                gallery_button.configure(state = 'normal', command = go_to_gallery)
                toggle_button.configure(state = 'normal', command = call_toggle_slide)
                Return_start_screen_button.configure(state = 'normal', command = back_to_start_screen)
                captured_image_path = capture_screen.just_captured_image_path
                imageTk = ImageTk.PhotoImage(Image.open(captured_image_path).resize(((921, 690))))
                captured_image_button = ctk.CTkButton(gallery_screen.captured_images_frame,
                                                        text ='',
                                                        width=153,
                                                        height = 100,
                                                        bg_color='transparent',
                                                        fg_color='transparent',
                                                        hover_color='gray',
                                                        image=ctk.CTkImage(light_image=Image.open(captured_image_path),
                                                                                dark_image=Image.open(captured_image_path),
                                                                                size = (153, 100)),
                                                        command = lambda : gallery_screen.button_is_chosen(imageTk))
                check_button = ctk.CTkCheckBox(captured_image_button,
                                               text = '',
                                               width = 15,
                                               height= 15,
                                               onvalue= 1,
                                               offvalue= 0,
                                               command = lambda index = gallery_screen.image_number: gallery_screen.export_image(index))
                check_button.place(relx = 1, rely = 1, anchor = 'se')
                gallery_screen.export_image_check_button.append(check_button)
                gallery_screen.list_Image.append(Image.open(captured_image_path))
                gallery_screen.list_image_button.append(captured_image_button)
                gallery_screen.image_number += 1
                gallery_screen.gallery_images_update()
        else:
                #Disable capture button
                capture_button.configure(state = 'disable', command = None)
                gallery_button.configure(state = 'disable', command = None)
                toggle_button.configure(state = 'disable', command = None)
                Return_start_screen_button.configure(state = 'disable', command = None)
                #Capture
                capture_screen.Countdown()
                #Wait for image is captured then update gallery
                gallery_screen.after(int((chosen_countdown_time + 0.5) * 1000), capture_and_update_gallery)
        
'''Camera configuration function'''
def swap_capture_mode():

    #Swap capture button and gif mode button
    global gif_mode
    if gif_mode:
        gif_mode = False
        capture_mode_button.configure(image = capture_button_imageCTk)
        capture_button.configure(image = gif_image_CTk)
    else:
        gif_mode = True
        capture_mode_button.configure(image = gif_image_CTk)
        capture_button.configure(image = capture_button_imageCTk)

def choosing_countdown_mode():
      global is_countdown_button_pressed
      if not is_countdown_button_pressed:
        is_countdown_button_pressed = True
        choosing_frame.place(relx=0.2, rely = 0.3, anchor = 'center')
      else:
            is_countdown_button_pressed = False
            choosing_frame.place_forget()

def call_toggle_slide():
       camera_configuration.Toggle_Slide(choosing_frame, toggle_button)
              

def choosing_3():
        global current_mode_countdown_time, is_countdown_button_pressed, chosen_countdown_time
        current_countdown_mode_button_off.configure(image = countdown_mode_3_imageCTk)
        current_countdown_mode_button_on.configure(image = countdown_mode_3_imageCTk)
        chosen_countdown_time = 3
        capture_screen.countdown_time = 3
        capture_screen.countdown_time_temp = 3
        countdown_mode_3_button.grid_forget()
        countdown_mode_5_button.grid(row = 1, column = 0, sticky = 'nsew', padx = 4, pady = 4)
        countdown_mode_10_button.grid(row = 2, column = 0, sticky = 'nsew', padx = 4, pady = 4)
        is_countdown_button_pressed = False
        choosing_frame.place_forget()

def choosing_5():
        global current_mode_countdown_time, is_countdown_button_pressed, chosen_countdown_time
        current_countdown_mode_button_off.configure(image = countdown_mode_5_imageCTk)
        current_countdown_mode_button_on.configure(image = countdown_mode_5_imageCTk)
        chosen_countdown_time = 5
        capture_screen.countdown_time = 5
        capture_screen.countdown_time_temp = 5
        countdown_mode_5_button.grid_forget()
        countdown_mode_3_button.grid(row = 1, column = 0, sticky = 'nsew', padx = 4, pady = 4)
        countdown_mode_10_button.grid(row = 2, column = 0, sticky = 'nsew', padx = 4, pady = 4)
        is_countdown_button_pressed = False
        choosing_frame.place_forget()
      
def choosing_10():
        global current_mode_countdown_time, is_countdown_button_pressed, chosen_countdown_time
        current_countdown_mode_button_off.configure(image = countdown_mode_10_imageCTk)
        current_countdown_mode_button_on.configure(image = countdown_mode_10_imageCTk)
        chosen_countdown_time = 10
        capture_screen.countdown_time = 10
        capture_screen.countdown_time_temp = 10
        countdown_mode_10_button.grid_forget()
        countdown_mode_3_button.grid(row = 1, column = 0, sticky = 'nsew', padx = 4, pady = 4)
        countdown_mode_5_button.grid(row = 2, column = 0, sticky = 'nsew', padx = 4, pady = 4)
        is_countdown_button_pressed = False
        choosing_frame.place_forget()

'''Create window'''
window = ctk.CTk()
window.title('Photobooth')
window.resizable(width=False, height=False)
window.geometry('1024x600')
ctk.set_appearance_mode('light')
'''Main code'''

'''Interface'''
start_screen = GSI.Get_Started_Interface(window)
capture_screen = ICI.Image_Capture_Interface(window)
gallery_screen = UIG.User_Image_Gallery_Interface(window)
camera_configuration = CCI.Camera_Configuration_Interface(capture_screen, -0.2, 0)

start_screen.pack(expand = True, fill = 'both')
 # Detect press event on the main window to delete the frame
window.bind_all('<Button>', Next_To_Capture_Screen)

'''Image capture widgets'''

# Capture button
#Import capture_button.png
capture_button_image = Image.open('DataStorage/Icon/Capture_button.png')
capture_button_imageCTk = ctk.CTkImage(light_image=capture_button_image,
                                        dark_image=capture_button_image,
                                        size = (100, 100))

#Create capture_button
capture_button = ctk.CTkButton(capture_screen,
                                width=80,
                                height=80,
                                fg_color='transparent',
                                bg_color='transparent',
                                border_width=0,
                                text = '',
                                hover_color='gray',
                                image = capture_button_imageCTk,
                                command = capture_and_update_gallery)

#Layout capture_button
capture_button.place(relx = 0.95,
                        rely = 0.5,
                        anchor = 'center')

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
Return_start_screen_button = ctk.CTkButton(capture_screen,
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
Return_start_screen_button.place(relx = 0, 
                                 rely = 0)

'''User image gallery widgets'''
 # Return image capture interface
#Import return_button_image.png
Return_button_image = Image.open('DataStorage/Icon/return_button_image.png')
Return_button_imageCTk = ctk.CTkImage(light_image=Return_button_image,
                                        dark_image=Return_button_image)
#Create Return_button
Return_image_capture_button = ctk.CTkButton(gallery_screen,
                                width=50,
                                height=50,
                                fg_color='transparent',
                                bg_color='transparent',
                                border_width=0,
                                text = '',
                                hover_color='gray',
                                image = Return_button_imageCTk,
                                command = return_image_capture_interface)
Return_image_capture_button.place(relx = 0, 
                                  rely = 0)
#Create export image button
export_image_button = ctk.CTkButton(gallery_screen.export_image_frame,
                                                text = 'Export',
                                                width = 100,
                                                height=40,
                                                corner_radius= 30,
                                                font = ('Arial', 20),
                                                command = Export_Image)
export_image_button.place(relx = 0.01, rely = 0.97, anchor = 'sw')

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
#variable to save countdown time is chosen
chosen_countdown_time = 3
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

 # Create toggle button
toggle_button = ctk.CTkButton(capture_screen,
                                width=60,
                                height=3,
                                bg_color='transparent',
                                fg_color='transparent',
                                border_width=0,
                                text = '',
                                hover_color='gray',
                                image = camera_configuration.toggle_button_imageCTk_down_arrow)
toggle_button.configure(command = call_toggle_slide)
#Layout toggle button
toggle_button.place(relx = 0.5, rely = camera_configuration.current_position + -camera_configuration.start_position, anchor = 'n')

window.mainloop()
