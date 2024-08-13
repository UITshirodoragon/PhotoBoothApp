import customtkinter as ctk
from customtkinter import CTkFont
from PIL import ImageFont, Image
from define import *
import os

class Template_edit(ctk.CTkFrame):
    
     def __init__(self, root):
          super().__init__(root)
          self.configure(fg_color = COLOR_MINT)

          header_font = CTkFont(family=HEADER_FONT, size=25)
          desciption_font = CTkFont(family=DESCRIPTION_FONT, size=27)   

          temp = Image.open('DataStorage/ImageGallery/final.png')
          w, h = temp.size
          template_img = ctk.CTkImage(light_image=temp, dark_image=temp, size = (500/h*w, 500))
          frame = ctk.CTkLabel(master=self, image=template_img, text=None)
          frame.pack()