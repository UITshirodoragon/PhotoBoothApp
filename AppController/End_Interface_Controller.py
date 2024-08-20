import os

class End_Interface_Controller():
    def __init__(self, end):
        self.number_of_uses = 0
        self.end = end

    def new_user_directory(self):
        self.number_of_uses += 1
        os.mkdir(f'DataStorage/ImageGallery/user{self.number_of_uses}')
        os.mkdir(f'DataStorage/GIFGallery/user{self.number_of_uses}')

    def reset_parameters(self):
        self.new_user_directory()
        if self.number_of_uses > 10:
            os.remove(f'DataStorage/ImageGallery/user{self.number_of_uses - 10}')
            os.remove(f'DataStorage/GIFGallery/user{self.number_of_uses - 10}')
         #Image variable
        self.end.gallery.controller.list_export_image_button.clear()
        self.end.gallery.controller.list_export_image_paths.clear()
        self.end.gallery.controller.list_export_image_check_button.clear()
        self.end.gallery.controller.list_image_button.clear()
        self.end.gallery.controller.list_image_Tk.clear()
        self.end.gallery.controller.image_number = 0
        self.end.gallery.controller.export_image_number = 0
        self.end.gallery.controller.current_image_page = 1
        self.end.gallery.controller.list_image_paths.clear()

        #GIF variable
        self.end.gallery.controller.current_gif_page = 1
        self.end.gallery.controller.gif_number = 0
        self.end.gallery.controller.gif_end_display = True
        self.end.gallery.controller.gif_mode = False
        self.end.gallery.controller.export_gif_number = 0
        self.end.gallery.controller.list_gif_button.clear()
        self.end.gallery.controller.list_gif_Tk.clear()
        self.end.gallery.controller.list_gif.clear()
        self.end.gallery.controller.export_gif_check_button.clear()
        self.end.gallery.controller.list_export_gif.clear()

        self.end.template_screen.image_number_selection = 0

