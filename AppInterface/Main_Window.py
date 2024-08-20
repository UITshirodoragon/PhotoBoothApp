import customtkinter as ctk
from PIL import Image
import Get_Started_Interface as GSI
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
import End_Interface as EI
from define import *
from AppController.Template_export_controller import *
from AppController.email_controller import send_email

'''Create window'''
window = ctk.CTk()
window.title('Photobooth')
window.resizable(width=False, height=False)
window.geometry('1024x600')
window.update()
#window.attributes('-fullscreen', True)
ctk.set_appearance_mode('light')
'''Main code'''

'''Interface'''
start_screen = GSI.Get_Started_Interface(window)
end_screen = EI.End_Interface(window, start_screen)

#Create first directory
#for i in range(10):
end_screen.controller.new_user_directory()

gallery_screen = UIGI.User_Image_Gallery_Interface(window, end_screen)
capture_screen = ICI.Image_Capture_Interface(window, gallery_screen, end_screen)
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

email_screen.end = end_screen

end_screen.gallery = gallery_screen
end_screen.email = email_screen
end_screen.template_screen = template_screen
end_screen.camera_configuration = camera_configuration

 # Detect press event on the main window to delete the frame
window.bind_all('<Button>', start_screen.Next_To_Template_Screen)

#window loop
window.mainloop()
