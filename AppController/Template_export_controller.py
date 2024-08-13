from PIL import Image
import os
from Template import *

def export_template(num):
  template = None
  match num:
     case 2:
        template = Template_2grids()
     case 4:
        template = Template_4grids()
     case 6:
        template = Template_6grids()
     case 8:
        template = Template_8grids()

  img_index = 0
  background = Image.open(f'DataStorage/Templates/template{int(num/2)}.png')
  img_pos_list = template.getImagePositionList()
  for pos in img_pos_list:
      img_index += 1
      img = Image.open(f'DataStorage/ImageGallery/image{img_index}.png').resize(template.getImageSize())
      background.paste(img, pos)

  background.save('DataStorage/ImageGallery/final.png')