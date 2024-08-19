import customtkinter as ctk
from customtkinter import CTkFont
from PIL import ImageFont, Image
from define import *
import os

class Template_edit(ctk.CTkFrame):
    
     def __init__(self, root, gallery):
          super().__init__(root)
          self.configure(fg_color = COLOR_MINT)
          self.gallery = gallery
          header_font = CTkFont(family=HEADER_FONT, size=25)
          desciption_font = CTkFont(family=DESCRIPTION_FONT, size=27)   
          self.email_screen = None
          '''temp = Image.open('DataStorage/ImageGallery/final.png')
          w, h = temp.size
          template_img = ctk.CTkImage(light_image=temp, dark_image=temp, size = (500/h*w, 500))
          frame = ctk.CTkLabel(master=self, image=template_img, text=None)
          frame.pack()'''

          # create template edit interface
        
          # pager button
          back_button = ctk.CTkButton(master=self, 
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
                         command=self.return_user_gallery)
          back_button.place(relx=0.02, rely=0.9)

          next_button = ctk.CTkButton(master=self, 
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
                                command=self.next_to_email_screen)
          next_button.place(relx=0.8, rely=0.9)

          self.display_final_frame = ctk.CTkLabel(master=self, text=None)
          self.display_final_frame.pack()

     def return_user_gallery(self):
          # delete previous page and show user gallery interface
          self.pack_forget()
          self.gallery.pack(expand = True, fill = 'both')

     def next_to_email_screen(self):
          self.pack_forget()
          self.email_screen.pack(expand = True, fill = 'both')