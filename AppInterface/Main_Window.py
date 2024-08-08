import customtkinter as ctk
from PIL import Image
import Get_Started_Interface as GSI
import Template_export as TEx

'''Create window'''
window = ctk.CTk()
window.title('Photobooth')
window.geometry('1024x600')
window.resizable(width=False, height=False)
window.configure(background = '#fafafa')
'''Main code'''

def Next_To_Capture_Screen(event):
        window.unbind_all('<Button>')
        start_screen.pack_forget()
        template_export_screen.pack(expand = True, fill = 'both')


'''Interface'''
start_screen = GSI.Get_Started_Interface(window)
start_screen.pack(expand = True, fill = 'both')

template_export_screen = TEx.Template_export(window)
template_export_screen.pack(expand = True, fill = 'both')
window.bind_all('<Button>', Next_To_Capture_Screen)

window.mainloop()
 