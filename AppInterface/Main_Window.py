import customtkinter as ctk
import Image_Capture_Interface as ICI
import User_Image_Gallery_Interface as UIGI
from customtkinter import CTkFont
from PIL import Image, ImageTk
import sys
import os

# Đường dẫn tới folder chứa module 
package_controller_path = os.path.abspath(os.path.join('..', 'PhotoBoothApp'))
if package_controller_path not in sys.path:
    sys.path.append(package_controller_path)
import Get_Started_Interface as GSI
import Camera_Configuration_Interface as CCI
import Template_export as TEX
import Template_edit as TED
import email_interface as EMI
from define import *
from AppController.Template_export_controller import *
from AppController.email_controller import send_email

def change_to_template_edit(prev):
        # call export template function and save in DataStorage/ImageGallery as final.png
        template_screen.controller.export_template(template_screen.get_template())

        # create template edit interface
        template_edit = TED.Template_edit(window)

        # pager button
        back_button = ctk.CTkButton(master=template_edit, 
                        text='Back',
                        text_color="#ffffff",
                        height=60,
                        font=CTkFont(family=HEADER_FONT, size=22),
                        bg_color='transparent',
                        fg_color='#BD8D5F',
                        image=LEFT_ARROW_SOLID,
                        hover=False,
                        anchor='center',
                        compound='left',
                        corner_radius=30,
                        command=lambda prev=template_edit, next=template_screen: back(prev=prev, next=next))
        back_button.place(relx=0.02, rely=0.9)

        next_button = ctk.CTkButton(master=template_edit, 
                                text='NEXT',
                                text_color="#ffffff",
                                height=60,
                                font=CTkFont(family=HEADER_FONT, size=22),
                                bg_color='transparent',
                                fg_color='#BD8D5F',
                                image=RIGHT_ARROW_SOLID,
                                hover=False,
                                anchor='center',
                                compound='right',
                                corner_radius=30,
                                command=lambda prev=template_edit: change_to_email_inter(prev=prev))
        next_button.place(relx=0.8, rely=0.9)

        # delete previous page and show template edit interface
        prev.pack_forget()
        template_edit.pack(expand = True, fill = 'both')

def change_to_email_inter(prev):
        # delete previous page and show template edit interface
        prev.pack_forget()
        email_screen = EMI.Email_interface(window)
        email_screen.pack(expand = True, fill = 'both')

        # button
        back_button = ctk.CTkButton(master=email_screen, 
                        text='Back',
                        text_color="#ffffff",
                        height=60,
                        font=CTkFont(family=HEADER_FONT, size=22),
                        bg_color='transparent',
                        fg_color='#BD8D5F',
                        image=LEFT_ARROW_SOLID,
                        hover=False,
                        anchor='center',
                        compound='left',
                        corner_radius=30,
                        command=lambda prev=email_screen, next=prev: back(prev=prev, next=next))
        back_button.place(relx=0.02, rely=0.9)

        submit_button = ctk.CTkButton(master=email_screen, 
                                text='SUBMIT',
                                text_color="#ffffff",
                                height=60,
                                font=CTkFont(family=HEADER_FONT, size=20),
                                bg_color='transparent',
                                fg_color=COLOR_BLOODRED,
                                image=RIGHT_ARROW_SOLID,
                                hover=False,
                                anchor='center',
                                compound='right',
                                corner_radius=30,
                                command=lambda email=email_screen.get_user_email, 
                                name=email_screen.get_user_name: send_email(email, name))
        submit_button.place(relx=0.8, rely=0.9)

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
template_screen = TEX.Template_export(window, gallery_screen)

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
next_button = ctk.CTkButton(master=template_screen.get_container(), 
                        text='NEXT',
                        text_color="#ffffff",
                        height=60,
                        font=CTkFont(family=HEADER_FONT, size=22),
                        bg_color='transparent',
                        fg_color='#BD8D5F',
                        image=RIGHT_ARROW_SOLID,
                        hover=False,
                        anchor='center',
                        compound='right',
                        corner_radius=30,
                        command=lambda prev=template_screen: change_to_template_edit(prev=prev))
next_button.place(relx=0.75, rely=0.85)



#window loop
window.mainloop()
