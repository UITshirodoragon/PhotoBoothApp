import customtkinter as ctk
import Image_Capture_Interface as ICI
import User_Image_Gallery_Interface as UIGI
from customtkinter import CTkFont
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

def change_to_capture_screen(prev):
        '''# call export template function and save in DataStorage/ImageGallery as final.png
        template_screen.controller.export_template(template_screen.get_template())

        '''

def change_to_email_inter(prev):
        # delete previous page and show template edit interface
        pass
       
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
template_screen = TEX.Template_export(window, start_screen, gallery_screen, capture_screen, camera_configuration)
template_edit = TED.Template_edit(window, gallery_screen)
email_screen = EMI.Email_interface(window, template_edit)

capture_screen.camera_configuration = camera_configuration
capture_screen.template_screen = template_screen

gallery_screen.camera_configuration = camera_configuration
gallery_screen.capture_screen = capture_screen
gallery_screen.template_edit = template_edit
gallery_screen.template_screen = template_screen

start_screen.template_screen = template_screen
start_screen.pack(expand = True, fill = 'both')

template_edit.email_screen = email_screen
 # Detect press event on the main window to delete the frame
window.bind_all('<Button>', start_screen.Next_To_Template_Screen)

#window loop
window.mainloop()
