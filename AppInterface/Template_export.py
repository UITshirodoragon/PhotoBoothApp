import customtkinter as ctk
from customtkinter import CTkFont
from PIL import ImageFont, Image
from define import *
import os

class Template_export(ctk.CTkFrame):
    
     def __init__(self, root):
          super().__init__(root)
          self.configure(fg_color = COLOR_SALT)

          header_font = CTkFont(family=HEADER_FONT, size=50)
          desciption_font = CTkFont(family=DESCRIPTION_FONT, size=30)   

          self.columnconfigure(0, weight=0)
          self.columnconfigure(1, weight=1)
          self.rowconfigure(1, weight=1)

          self.template_buttons = []
          self.image_number_selection = 4

          # create button container 
          button_container = ctk.CTkFrame(master=self, height=80, fg_color=COLOR_PINEGREEN, corner_radius=0)
          button_container.grid(column = 0, row = 0, sticky=ctk.NW)
          button_container.columnconfigure(0, weight=1)
          button_container.columnconfigure(1, weight=1)
          button_container.columnconfigure(2, weight=1)
          button_container.columnconfigure(3, weight=1)

          # button activity and animation
          def click_button(button):
               button_1_image.configure(fg_color=COLOR_PINEGREEN, corner_radius=0)
               button_2_image.configure(fg_color=COLOR_PINEGREEN, corner_radius=0)
               button_3_image.configure(fg_color=COLOR_PINEGREEN, corner_radius=0)
               button_4_image.configure(fg_color=COLOR_PINEGREEN, corner_radius=0)

               self.template_buttons = []

               match button:
                    case 'button1':
                         button_1_image.configure(fg_color=COLOR_MINT, corner_radius=30)
                         self.image_number_selection = 1
                    case 'button2':
                         button_2_image.configure(fg_color=COLOR_MINT, corner_radius=30)
                         self.image_number_selection = 2
                    case 'button3':
                         button_3_image.configure(fg_color=COLOR_MINT, corner_radius=30)
                         self.image_number_selection = 3
                    case 'button4':
                         button_4_image.configure(fg_color=COLOR_MINT, corner_radius=30)
                         self.image_number_selection = 4

               for child in template_container.winfo_children():
                    child.destroy() 

               # Display template
               i, j = 0, 0
               
               for templates in os.listdir("DataStorage/Templates/Template" + str(self.image_number_selection)+ "image"):

                    template = Image.open('DataStorage/Templates/Template' + str(self.image_number_selection)+ 'image/' + templates)
                    template_Img = ctk.CTkImage(light_image=template,
                                                  dark_image=template,
                                                  size = (256, 150))
                    template_button = ctk.CTkButton(master=template_container,
                                                  text=None,
                                                  bg_color='transparent',
                                                  fg_color=COLOR_LION,
                                                  hover=False,
                                                  corner_radius=15,
                                                  image=template_Img,
                                                  anchor='center',
                                                  command=lambda i=i, j=j, image=template_Img: select_template(self, i, j, image))
                    self.template_buttons.append(template_button)

                    template_button.grid(column=j, row=i, padx=40, pady=40)
                    

                    if j+1<2:
                         i,j = i, j+1
                    else:
                         i,j = i+1, 0

               

          def select_template(self, i, j, templateImg):
               for child in information_container.winfo_children():
                    child.destroy()
               k, l = 0, 0
               for templateBtn in self.template_buttons:
                    if templateBtn.cget("fg_color") == COLOR_MINT:
                         templateBtn.configure(fg_color = COLOR_LION, state = "active", height=150)  
                    templateBtn.grid(column = l, row = k, padx=40, pady=40)

                    if l+1<2:
                         k,l = k, l+1
                    else:
                         k,l = k+1, 0

               button = ctk.CTkButton(master=template_container,
                                                  text=None,
                                                  height=180,
                                                  bg_color='transparent',
                                                  fg_color=COLOR_MINT,
                                                  hover=False,
                                                  corner_radius=15,
                                                  image=templateImg,
                                                  state="disable",
                                                  command=lambda i=i, j=j, image=templateImg: select_template(self, i, j, image))
               button.grid(column=j, row=i, padx=40, pady=25)
               self.template_buttons[i * 2 + j] = button

               label = ctk.CTkLabel(master=information_container, text=None, image=templateImg)
               label.pack()
          # create navigation menu bar
     
          button_1_image = ctk.CTkButton(master=button_container,
                                         width=180,
                                         height=60,
                                         text= '1 image',
                                         font = (desciption_font, 20),
                                         text_color=COLOR_SALT,
                                         bg_color='transparent',
                                         fg_color=COLOR_PINEGREEN,
                                         hover=False,
                                         corner_radius=0,
                                         command=lambda button = 'button1': click_button(button))
 
          button_2_image = ctk.CTkButton(master=button_container,
                                         width=180,
                                         height=60,
                                         text= '2 images',
                                         font = (desciption_font, 20),
                                         text_color=COLOR_SALT,
                                         bg_color='transparent',
                                         fg_color=COLOR_PINEGREEN,
                                         hover=False,
                                         corner_radius=0,
                                         command=lambda button = 'button2': click_button(button))
 
          button_3_image = ctk.CTkButton(master=button_container,
                                         width=180,
                                         height=60,
                                         text= '3 images',
                                         font = (desciption_font, 20),
                                         text_color=COLOR_SALT,
                                         bg_color='transparent',
                                         fg_color=COLOR_PINEGREEN,
                                         hover=False,
                                         corner_radius=0,
                                         command=lambda button = 'button3': click_button(button))
 
          button_4_image = ctk.CTkButton(master=button_container,
                                         width=180,
                                         height=60,
                                         text= '4 images',
                                         font = (desciption_font, 20),
                                         text_color=COLOR_SALT,
                                         bg_color='transparent',
                                         fg_color=COLOR_PINEGREEN,
                                         hover=False,
                                         corner_radius=0,
                                         command=lambda button = 'button4': click_button(button))

          button_1_image.grid(column=0, row=0, sticky=ctk.NW, pady=15, padx=5)
          button_2_image.grid(column=1, row=0, sticky=ctk.NW, pady=15, padx=5)
          button_3_image.grid(column=2, row=0, sticky=ctk.NW, pady=15, padx=5)
          button_4_image.grid(column=3, row=0, sticky=ctk.NW, pady=15, padx=5)

          # template container
          
          template_container = ctk.CTkFrame(master=self, fg_color='transparent')
          template_container.grid(column=0, row=1, sticky=ctk.NSEW)
          template_container.columnconfigure(0, weight=1)
          template_container.rowconfigure(0, weight=1)

          

          #information container
          information_container = ctk.CTkFrame(master=self, fg_color=COLOR_MINT, corner_radius=0)
          information_container.grid(column=1, row=0, rowspan=2, sticky=ctk.NSEW)