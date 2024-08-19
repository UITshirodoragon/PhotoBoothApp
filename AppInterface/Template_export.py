import customtkinter as ctk
from customtkinter import CTkFont
from PIL import ImageFont, Image
from define import *
import sys
import os

# Đường dẫn tới folder chứa module 
package_controller_path = os.path.abspath(os.path.join('..', 'PhotoBoothApp'))
if package_controller_path not in sys.path:
    sys.path.append(package_controller_path)
from AppController import Template_export_controller

class Template_export(ctk.CTkFrame):
    
     def __init__(self, root, start_screen, gallery, capture_screen, camera_configuration):
          super().__init__(root)
          self.parent = root
          self.start_screen = start_screen
          self.gallery = gallery
          self.capture_screen = capture_screen
          self.camera_configuration = camera_configuration
          self.controller = Template_export_controller.Template_Export_Controller(self)
          self.controller.list_export_image_paths = self.gallery.controller.list_export_image_paths
          self.configure(fg_color = COLOR_MINT)

          header_font = CTkFont(family=HEADER_FONT, size=25)
          desciption_font = CTkFont(family=DESCRIPTION_FONT, size=27)   

          self.columnconfigure(0, weight=1)
          self.columnconfigure(1, weight=4)
          self.rowconfigure(1, weight=1)

          self.template_buttons = []
          self.image_number_selection = 0
          # button activity and animation
          def click_button(button):
               # reset button color
               self.template_2grid_btn.configure(fg_color=COLOR_LION)          
               self.template_4grid_btn.configure(fg_color=COLOR_LION)          
               self.template_6grid_btn.configure(fg_color=COLOR_LION)          
               self.template_8grid_btn.configure(fg_color=COLOR_LION)   
               # set selected button color
               match button:
                    case 'button2':
                         self.template_2grid_btn.configure(fg_color=COLOR_PINEGREEN)
                         self.image_number_selection = 2
                    case 'button4':
                         self.template_4grid_btn.configure(fg_color=COLOR_PINEGREEN)
                         self.image_number_selection = 4
                    case 'button6':
                         self.template_6grid_btn.configure(fg_color=COLOR_PINEGREEN)
                         self.image_number_selection = 6
                    case 'button8':
                         self.template_8grid_btn.configure(fg_color=COLOR_PINEGREEN)
                         self.image_number_selection = 8
               self.text.set(f'{self.image_number_selection} grids\ntemplate')
               self.Notification.place_forget()
               self.gallery.update_confirm_frame()

          # templates container
          self.template_container = ctk.CTkFrame(master=self, 
                                            fg_color=COLOR_SALT, 
                                            width=800, height=520,
                                            corner_radius=30)
          self.template_container.grid(column=1, row=0, sticky=ctk.NSEW, pady = (40,0), padx=(0,40))

          #?template container

          # open template
          template2 = Image.open('DataStorage/Templates/layout2.png')
          template4 = Image.open('DataStorage/Templates/layout4.png')
          template6 = Image.open('DataStorage/Templates/layout6.png')
          template8 = Image.open('DataStorage/Templates/layout8.png')

          template_img2 = ctk.CTkImage(light_image=template2, dark_image=template2, size = (225, 165))
          template_img4 = ctk.CTkImage(light_image=template4, dark_image=template4, size = (225, 165))
          template_img6 = ctk.CTkImage(light_image=template6, dark_image=template6, size = (240, 160))
          template_img8 = ctk.CTkImage(light_image=template8, dark_image=template8, size = (180, 270))
          #create button
          self.template_2grid_btn = ctk.CTkButton(master=self.template_container,    
                                        text="2 Grids",
                                        text_color='white',
                                        font=desciption_font,
                                        width=230,
                                        height=200,
                                        bg_color='transparent',
                                        fg_color=COLOR_LION,
                                        hover=False,
                                        corner_radius=0,
                                        image=template_img2,
                                        anchor='center',
                                        compound='top',
                                        command=lambda btn="button2": click_button(btn))
          self.template_4grid_btn = ctk.CTkButton(master=self.template_container,
                                        text="4 Grids",
                                        text_color='white',
                                        width=230,
                                        height=200,
                                        font=desciption_font,
                                        bg_color='transparent',
                                        fg_color=COLOR_LION,
                                        hover=False,
                                        corner_radius=0,
                                        image=template_img4,
                                        anchor='center',
                                        compound='top',
                                        command=lambda btn="button4": click_button(btn))
          self.template_6grid_btn = ctk.CTkButton(master=self.template_container,
                                        text="6 Grids",
                                        text_color='white',
                                        width=245,
                                        height=195,
                                        font=desciption_font,
                                        bg_color='transparent',
                                        fg_color=COLOR_LION,
                                        hover=False,
                                        corner_radius=0,
                                        image=template_img6,
                                        anchor='center',
                                        compound='top',
                                        command=lambda btn="button6": click_button(btn))
          self.template_8grid_btn = ctk.CTkButton(master=self.template_container,
                                        text="8 Grids",
                                        text_color='white',
                                        width=185,
                                        height=300,
                                        font=desciption_font,
                                        bg_color='transparent',
                                        fg_color=COLOR_LION,
                                        hover=False,
                                        corner_radius=0,
                                        image=template_img8,
                                        anchor='center',
                                        compound='top',
                                        command=lambda btn="button8": click_button(btn))
          #place button on template container
          self.template_2grid_btn.place(relx=0.05, rely=0.05)
          self.template_4grid_btn.place(relx=0.05, rely=0.5)
          self.template_6grid_btn.place(relx=0.65, rely=0.05)
          self.template_8grid_btn.place(relx=0.38, rely=0.05)

          #?information container
          information_container = ctk.CTkFrame(master=self, fg_color=COLOR_MINT, corner_radius=0)
          #Return start screen button
          self.Return_start_screen_button = ctk.CTkButton(information_container,
                                                            width=50,
                                                            height=50,
                                                            fg_color=COLOR_LION,
                                                            bg_color='transparent',
                                                            corner_radius=10,
                                                            text = '',
                                                            hover_color=COLOR_PINEGREEN,
                                                            image = LEFT_ARROW_SOLID,
                                                            command = self.return_get_started_interface)
          self.Return_start_screen_button.place(relx = 0, 
                                  rely = 0)
          information_container.grid(column=0, row=0, rowspan=2, sticky=ctk.NSEW)

          #Forgot choosing template label
          self.Notification = ctk.CTkLabel(self.template_container,
                                           text = 'You forgot to choose template',
                                           text_color= COLOR_BLOODRED,
                                           font = CTkFont(family=DESCRIPTION_FONT, size=20))
          # open arrow icon for next button, change to template edit
          next_button = ctk.CTkButton(master=self.template_container, 
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
                              command=self.next_to_capture_screen)
          next_button.place(relx=0.75, rely=0.85)

          #text
          label = ctk.CTkLabel(master=information_container,
                               text="SELECTED",
                              font=header_font,
                              text_color=COLOR_PINEGREEN)
          label.pack(padx=10, pady=(80,20))

          self.text = ctk.StringVar()
          self.text.set('you haven'+ "'t"+ '\nselected\nanything' )
          template_selected = ctk.CTkLabel(master=information_container,
                                           textvariable=self.text, 
                                           font=desciption_font,
                                           text_color=COLOR_PINEGREEN)
          template_selected.pack()
          

     def get_template(self):
          return self.image_number_selection
     
     def get_container(self):
          return self.template_container
     
     def return_get_started_interface(self):
          self.pack_forget()
          self.parent.bind_all('<Button>', self.start_screen.Next_To_Template_Screen)
          self.start_screen.pack(expand = True, fill = 'both')
     
     def next_to_capture_screen(self):
          if self.image_number_selection == 0:
               self.Notification.place(relx = 0.7, rely = 0.78)
               return None
          self.capture_screen.in_capture_screen = True
          self.capture_screen.Update_frame()
          self.pack_forget()
          self.capture_screen.pack(expand = True, fill = 'both')
               