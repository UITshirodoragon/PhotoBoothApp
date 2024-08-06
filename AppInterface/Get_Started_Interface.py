import customtkinter as ctk
import Image_Capture_Interface as ICI
from customtkinter import CTkFont
from PIL import ImageFont, ImageDraw, Image, ImageTk

class Get_Started_Interface(ctk.CTkFrame):
    
    def __init__(self, root):

        self.color1 = '#BD8D5F'
        self.color2 = '#24685B'
        self.color3 = '#9ECEEA' 
        self.color4 = '#F8FCFD'
        self.root = root
        
        header_font = CTkFont(family=ImageFont.truetype("DataStorage/Fonts/UTM Thanh Nhac TL.ttf", size=50).getname()[0], size=50)
        desciption_font = CTkFont(family=ImageFont.truetype("DataStorage/Fonts/UTM Thanh Nhac TL.ttf", size=50).getname()[0], size=30)

        frame = ctk.CTkFrame(root, fg_color=self.color2, corner_radius=20)
        frame.pack(pady=20, padx=20, fill="both")

        header_label = ctk.CTkLabel(master=frame, 
                                    text="PHOTO BOOTH", 
                                    font=header_font,
                                    text_color=self.color4)
        header_label.grid(column = 0, row = 0, padx = 40, pady = (70, 0))

        description_label = ctk.CTkLabel(master=frame, 
                                    text="Sản phẩm trưng bày",  
                                    font=desciption_font,
                                    text_color=self.color4)
        description_label.grid(column = 0, row = 1, padx = 40, pady = (0, 130), sticky = ctk.W)

        smt = ctk.CTkLabel(master=frame,
                            text="cái gì đó",
                            width=260,
                            height=200,  
                            font=desciption_font,
                            fg_color=self.color4,
                            text_color=self.color3,
                            corner_radius=10)
        smt.grid(column = 1, row = 0, padx = (150, 0), pady = (80, 0), rowspan = 2)

        button = ctk.CTkButton(master=root,
                               width=1024,
                               height=300,
                               text="tap to start!", 
                               text_color=self.color3,
                               font=desciption_font,
                               bg_color=self.color4,
                               fg_color=self.color4,
                               hover_color=self.color4,
                               command=lambda root = root: change_page(root))
        button. pack()

        def change_page(self):
            for child in root.winfo_children():
                child.destroy()