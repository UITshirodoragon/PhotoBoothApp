from PIL import ImageFont, Image
import customtkinter as ctk
from customtkinter import CTkFont

# Fonts define
HEADER_FONT = ImageFont.truetype("DataStorage/Fonts/UTM Thanh Nhac TL.ttf", size=50).getname()[0]
DESCRIPTION_FONT = ImageFont.truetype("DataStorage/Fonts/UTM DAXMEDIUM.ttf", size=30).getname()[0]

# colors define
COLOR_SKYBLUE = '#9ECEEA'
COLOR_DOGWOOD = '#E8CFCB'     
COLOR_PINEGREEN = '#24685B'
COLOR_LION = '#BD8D5F'
COLOR_SALT = '#F8FCFD'
COLOR_MINT = '#2FA98C'
COLOR_BLOODRED = '#690500'
COLOR_MINT      = '#2FA98C'
COLOR_BEANGREEN = '#00DF81'
COLOR_FROG      = '#17876D'
COLOR_FOREST    = '#095544'
COLOR_BASIL     = '#0B453A'
COLOR_PINE      = '#06302B'   
COLOR_WHITE     = '#F1F7F6'
COLOR_STONE     = '#707D7D'
COLOR_PISTACHIO = '#AACBC4'
COLOR_RICHBLACK = '#021B1A'

img = Image.open('DataStorage/Icons/right-arrow-solid-24.png')
RIGHT_ARROW_SOLID = ctk.CTkImage(light_image=img, dark_image=img) 

img = Image.open('DataStorage/Icons/left-arrow-solid-24.png')
LEFT_ARROW_SOLID = ctk.CTkImage(light_image=img, dark_image=img)