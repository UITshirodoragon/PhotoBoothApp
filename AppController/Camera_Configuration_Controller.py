import customtkinter as ctk

class Camera_Configuration_Controller():
    def __init__(self, camera_configuration):
        self.gif_mode = True
        self.camera_configuration = camera_configuration
        #Variable to check if the button is pressed or not
        self.is_countdown_button_pressed = False
        #variable to save countdown time is chosen
        self.chosen_countdown_time = 3
    #Swap capture button and gif mode button
    def swap_capture_mode(self):
        if self.gif_mode:
            self.gif_mode = False
            self.camera_configuration.capture_mode_button.configure(image = self.camera_configuration.capture_screen.capture_button_imageCTk)
            self.camera_configuration.capture_screen.capture_button.configure(image = self.camera_configuration.gif_image_CTk)
        else:
            self.gif_mode = True
            self.camera_configuration.capture_mode_button.configure(image = self.camera_configuration.gif_image_CTk)
            self.camera_configuration.capture_screen.capture_button.configure(image = self.camera_configuration.capture_screen.capture_button_imageCTk)

    def choosing_countdown_mode(self):
        if not self.is_countdown_button_pressed:
            self.is_countdown_button_pressed = True
            self.camera_configuration.capture_screen.choosing_frame.place(relx=0.2, rely = 0.29, anchor = 'center')
        else:
            self.is_countdown_button_pressed = False
            self.camera_configuration.capture_screen.choosing_frame.place_forget()

    def choosing_3(self):
        self.camera_configuration.current_countdown_mode_button_off.configure(image = self.camera_configuration.countdown_mode_3_imageCTk)
        self.camera_configuration.current_countdown_mode_button_on.configure(image = self.camera_configuration.countdown_mode_3_imageCTk)
        self.chosen_countdown_time = 3
        self.camera_configuration.capture_screen.controller.countdown_time = 3
        self.camera_configuration.capture_screen.controller.countdown_time_temp = 3
        self.camera_configuration.countdown_mode_3_button.grid_forget()
        self.camera_configuration.countdown_mode_5_button.grid(row = 1, column = 0, sticky = 'nsew', padx = 4, pady = 4)
        self.camera_configuration.countdown_mode_10_button.grid(row = 2, column = 0, sticky = 'nsew', padx = 4, pady = 4)
        self.is_countdown_button_pressed = False
        self.camera_configuration.capture_screen.choosing_frame.place_forget()

    def choosing_5(self):
        self.camera_configuration.current_countdown_mode_button_off.configure(image = self.camera_configuration.countdown_mode_5_imageCTk)
        self.camera_configuration.current_countdown_mode_button_on.configure(image = self.camera_configuration.countdown_mode_5_imageCTk)
        self.chosen_countdown_time = 5
        self.camera_configuration.capture_screen.controller.countdown_time = 5
        self.camera_configuration.capture_screen.controller.countdown_time_temp = 5
        self.camera_configuration.countdown_mode_5_button.grid_forget()
        self.camera_configuration.countdown_mode_3_button.grid(row = 1, column = 0, sticky = 'nsew', padx = 4, pady = 4)
        self.camera_configuration.countdown_mode_10_button.grid(row = 2, column = 0, sticky = 'nsew', padx = 4, pady = 4)
        self.is_countdown_button_pressed = False
        self.camera_configuration.capture_screen.choosing_frame.place_forget()
    
    def choosing_10(self):
        self.camera_configuration.current_countdown_mode_button_off.configure(image = self.camera_configuration.countdown_mode_10_imageCTk)
        self.camera_configuration.current_countdown_mode_button_on.configure(image = self.camera_configuration.countdown_mode_10_imageCTk)
        self.chosen_countdown_time = 10
        self.camera_configuration.capture_screen.controller.countdown_time = 10
        self.camera_configuration.capture_screen.controller.countdown_time_temp = 10
        self.camera_configuration.countdown_mode_10_button.grid_forget()
        self.camera_configuration.countdown_mode_3_button.grid(row = 1, column = 0, sticky = 'nsew', padx = 4, pady = 4)
        self.camera_configuration.countdown_mode_5_button.grid(row = 2, column = 0, sticky = 'nsew', padx = 4, pady = 4)
        self.is_countdown_button_pressed = False
        self.camera_configuration.capture_screen.choosing_frame.place_forget()