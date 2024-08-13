import tkinter as tk
import customtkinter as ctk
from customtkinter import CTkFont
from PIL import Image, ImageTk
from define import *

uppercase = False

class Keyboard(ctk.CTkFrame):
    info = None
    def __init__(self, root, iEntry = None, background = COLOR_SALT, buttoncolor = COLOR_SKYBLUE):
        self.entry = iEntry
        super().__init__(root)

        self.configure(fg_color=buttoncolor)
        keys = [
                ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
                ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
                ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
                ['Toggle Case', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'Backspace'],
                ['@', '.', 'Space', '-', '_']
            ]
        
        def on_key_press(key):
            current_text = self.entry.get()
            self.entry.delete(0, ctk.END)
            self.entry.insert(0, current_text + key)
            self.info = self.entry.get()

        def toggle_case():
            global uppercase
            uppercase = not uppercase
            update_keyboard()

        def update_keyboard():
            for widgets in self.winfo_children():
                for widget in widgets.winfo_children():
                    key = widget.cget("text")
                    key = key.upper() if uppercase else key.lower()
                    if len(key) == 1:
                        widget.configure(text=key,
                                         command=lambda k=key: on_key_press(k))

        def create_keyboard():
            
            key_font = (DESCRIPTION_FONT, 24)
            for row in keys:
                row_frame = ctk.CTkFrame(master=self, fg_color = buttoncolor)
                row_frame.pack(side='top', pady=2)  # Giảm khoảng cách giữa các hàng
                for key in row:
                    if key == 'Space':
                        button = ctk.CTkButton(row_frame, 
                                           text='Space',
                                           text_color=COLOR_PINEGREEN,
                                           bg_color= "transparent",
                                           fg_color=background, 
                                           width=200, height=70, 
                                           command=lambda k=' ': on_key_press(k),
                                           font = key_font)
                    elif key == 'Backspace':
                        img_backspace = ctk.CTkImage(light_image=Image.open('DataStorage/Icons/tag-x-solid-72.png'))
                        button = ctk.CTkButton(master=row_frame, 
                                           width=110, height=70,
                                           text='',
                                           text_color=COLOR_PINEGREEN,
                                           bg_color= "transparent",
                                           fg_color=background,
                                           image=img_backspace,
                                           compound='left',
                                           anchor='center',
                                           command=lambda: self.entry.delete(len(self.entry.get())-1),
                                           font = (DESCRIPTION_FONT, 48))
                    elif key == 'Toggle Case':
                        button = ctk.CTkButton(master=row_frame, 
                                           text='Shift', 
                                           text_color=COLOR_PINEGREEN,
                                           width=110, height=70, 
                                           bg_color= "transparent",
                                           fg_color=background,
                                           command=toggle_case,
                                           font = key_font)
                    else:
                        display_key = key if uppercase else key.lower()
                        button = ctk.CTkButton(master=row_frame, 
                                           text=display_key, 
                                           text_color=COLOR_PINEGREEN,
                                           bg_color= "transparent",
                                           fg_color=background, 
                                           width=70, height=70, 
                                           command=lambda k=display_key: on_key_press(k),
                                           font = key_font)
                    button.pack(side='left', padx=2)

        create_keyboard()

    def get_info(self):
        return self.info
    
    def set_current_entry(self, entry):
        self.entry = entry

class Email_interface(ctk.CTkFrame):
    def __init__(self, root):
        super().__init__(root)
        self.configure(fg_color=COLOR_SKYBLUE)
        self.user_name = ctk.StringVar()
        self.user_email = ctk.StringVar()

        def set_email_entry(event):
            keyboard.set_current_entry(event.widget)

            if email_entry.get() == "User email":
                email_entry.delete(0, 'end')
                email_entry.configure(text_color=COLOR_PINEGREEN)

        def set_name_entry(event):
            keyboard.set_current_entry(event.widget)

            if name_entry.get() == "User name":
                name_entry.delete(0, 'end')
                name_entry.configure(text_color=COLOR_PINEGREEN)
        
        def email_entry_focus_out(event):

            if email_entry.get() == "":
                email_entry.insert(0, "User email")
                email_entry.configure(text_color='#899aab')
        
        def name_entry_focus_out(event):

            if name_entry.get() == "":
                name_entry.insert(0, "User name")
                name_entry.configure(text_color='#899aab')
             
        #? create header
        header = ctk.CTkLabel(master=self,
                              text="Please enter your information",
                              text_color=COLOR_PINEGREEN,
                              font=(HEADER_FONT, 25),
                              bg_color="transparent",
                              fg_color="transparent")
        header.pack(pady=(40,0))

        #? create entry container
        entry_container = ctk.CTkFrame(master=self, fg_color="transparent")
        entry_container.pack()
         
        # email entry
        email_entry = ctk.CTkEntry(master=entry_container,
                                   font=(DESCRIPTION_FONT, 22),
                                   text_color='#899aab',
                                   width=250, height=60,
                                   bg_color=COLOR_SKYBLUE,
                                   fg_color=COLOR_SALT,
                                   corner_radius=20,
                                   border_color=COLOR_PINEGREEN,
                                   border_width=5,
                                   textvariable=self.user_email)
        email_entry.pack(side='left', pady=(20,40), padx=40)
        # name entry
        name_entry = ctk.CTkEntry(master=entry_container,
                                   font=(DESCRIPTION_FONT, 24),
                                   text_color='#899aab',
                                   width=250, height=60,
                                   bg_color=COLOR_SKYBLUE,
                                   fg_color=COLOR_SALT,
                                   corner_radius=20,
                                   border_color=COLOR_PINEGREEN,
                                   border_width=5, 
                                   textvariable=self.user_name, )
        name_entry.pack(side='left', pady =(20,40), padx=40)
            
        #? create entry container
        keyboard = Keyboard(root=self, iEntry=email_entry)
        keyboard.pack()

        email_entry.insert(0, "User email")
        name_entry.insert(0, "User name")

        email_entry.bind("<FocusIn>", set_email_entry)
        email_entry.bind("<FocusOut>", email_entry_focus_out)
        name_entry.bind("<FocusIn>", set_name_entry)
        name_entry.bind("<FocusOut>", name_entry_focus_out)

# window = ctk.CTk()
# window.title('Photobooth')
# window.geometry('1024x600')
# window.resizable(width=False, height=False)

# email_screen = Email_interface(window)
# email_screen.pack(expand = True, fill = 'both')

# window.mainloop()