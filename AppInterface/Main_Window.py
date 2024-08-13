import customtkinter as ctk
import Get_Started_Interface as GSI
import Image_Capture_Interface as ICI
import User_Image_Gallery_Interface as UIGI
import Get_Started_Interface as GSI
import Camera_Configuration_Interface as CCI
import platform

'''Create window'''
window = ctk.CTk()
window.title('Photobooth')
window.resizable(width=False, height=False)
window.geometry('1024x600')
window.update()
if platform.system() == "Linux":
        window.attributes("-fullscreen", True)
elif platform.system() == "Windows":
        window.update()
        window.attributes('-fullscreen', True)
ctk.set_appearance_mode('light')
'''Main code'''
'''Interface'''
start_screen = GSI.Get_Started_Interface(window)
gallery_screen = UIGI.User_Image_Gallery_Interface(window)
capture_screen = ICI.Image_Capture_Interface(window, gallery_screen, start_screen)
camera_configuration = CCI.Camera_Configuration_Interface(capture_screen, -0.2, 0)

capture_screen.camera_configuration = camera_configuration

gallery_screen.camera_configuration = camera_configuration
gallery_screen.capture_screen = capture_screen

start_screen.capture_screen = capture_screen
start_screen.camera_configuration = camera_configuration

start_screen.pack(expand = True, fill = 'both')
 # Detect press event on the main window to delete the frame
window.bind_all('<Button>', start_screen.Next_To_Capture_Screen)

window.mainloop()
