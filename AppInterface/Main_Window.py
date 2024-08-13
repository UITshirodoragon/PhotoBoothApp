import customtkinter as ctk
import Image_Capture_Interface as ICI
import User_Image_Gallery_Interface as UIGI
from customtkinter import CTkFont
from PIL import Image, ImageTk
import Get_Started_Interface as GSI
import Camera_Configuration_Interface as CCI
import Template_export as TEX
import Template_edit as TED
import email_interface as EMI
from define import *
import sys
import os
sys.path.insert(0, 'AppController')
from Template_export_controller import *

def change_page(prev):
        export_template(template_screen.get_template())
        template_edit = TED.Template_edit(window)

        back_img = Image.open('DataStorage/Icons/left-arrow-solid-24.png')
        back_icon = ctk.CTkImage(light_image=back_img, dark_image=back_img)
        back_button = ctk.CTkButton(master=template_edit, 
                        text='Back',
                        text_color="#ffffff",
                        height=60,
                        font=CTkFont(family=HEADER_FONT, size=22),
                        bg_color='transparent',
                        fg_color='#BD8D5F',
                        image=back_icon,
                        hover=False,
                        anchor='center',
                        compound='left',
                        corner_radius=30,
                        command=lambda prev=template_edit, next=template_screen: back(prev=prev, next=next))
        back_button.place(relx=0.02, rely=0.9)

        next_img = Image.open('DataStorage/Icons/right-arrow-solid-24.png')
        next_icon = ctk.CTkImage(light_image=next_img, dark_image=next_img)
        next_button = ctk.CTkButton(master=template_edit, 
                                text='NEXT',
                                text_color="#ffffff",
                                height=60,
                                font=CTkFont(family=HEADER_FONT, size=22),
                                bg_color='transparent',
                                fg_color='#BD8D5F',
                                image=next_icon,
                                hover=False,
                                anchor='center',
                                compound='right',
                                corner_radius=30,
                                command=lambda prev=template_edit: change_to_email_inter(prev=prev))
        next_button.place(relx=0.75, rely=0.9)

        prev.pack_forget()
        template_edit.pack(expand = True, fill = 'both')

def change_to_email_inter(prev):
        prev.pack_forget()
        email_screen = EMI.Email_interface(window)
        email_screen.pack(expand = True, fill = 'both')

        back_img = Image.open('DataStorage/Icons/left-arrow-solid-24.png')
        back_icon = ctk.CTkImage(light_image=back_img, dark_image=back_img)
        back_button = ctk.CTkButton(master=email_screen, 
                        text='Back',
                        text_color="#ffffff",
                        height=60,
                        font=CTkFont(family=HEADER_FONT, size=22),
                        bg_color='transparent',
                        fg_color='#BD8D5F',
                        image=back_icon,
                        hover=False,
                        anchor='center',
                        compound='left',
                        corner_radius=30,
                        command=lambda prev=email_screen, next=prev: back(prev=prev, next=next))
        back_button.place(relx=0.02, rely=0.9)

def back(prev, next):
        prev.pack_forget()
        next.pack(expand = True, fill = 'both')
def eport_template(prev, next):
        prev.get_template()
        prev.pack_forget()
        next.pack(expand = True, fill = 'both')

'''Create window'''
window = ctk.CTk()
window.title('Photobooth')
window.resizable(width=False, height=False)
window.geometry('1024x600')
window.update()
window.attributes('-fullscreen', True)
ctk.set_appearance_mode('light')
'''Main code'''



'''Interface'''
start_screen = GSI.Get_Started_Interface(window)
gallery_screen = UIGI.User_Image_Gallery_Interface(window)
capture_screen = ICI.Image_Capture_Interface(window, gallery_screen, start_screen)
camera_configuration = CCI.Camera_Configuration_Interface(capture_screen, -0.2, 0)
template_screen = TEX.Template_export(window)

capture_screen.camera_configuration = camera_configuration

gallery_screen.camera_configuration = camera_configuration
gallery_screen.capture_screen = capture_screen
gallery_screen.template_export = template_screen

start_screen.capture_screen = capture_screen
start_screen.camera_configuration = camera_configuration

start_screen.pack(expand = True, fill = 'both')

 # Detect press event on the main window to delete the frame
window.bind_all('<Button>', start_screen.Next_To_Capture_Screen)

# open arrow icon for next button, change to template edit
next_img = Image.open('DataStorage/Icons/right-arrow-solid-24.png')
next_icon = ctk.CTkImage(light_image=next_img, dark_image=next_img)
next_button = ctk.CTkButton(master=template_screen.get_container(), 
                        text='NEXT',
                        text_color="#ffffff",
                        height=60,
                        font=CTkFont(family=HEADER_FONT, size=22),
                        bg_color='transparent',
                        fg_color='#BD8D5F',
                        image=next_icon,
                        hover=False,
                        anchor='center',
                        compound='right',
                        corner_radius=30,
                        command=lambda prev=template_screen: change_page(prev=prev))
next_button.place(relx=0.75, rely=0.85)



#window loop
window.mainloop()
