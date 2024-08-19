import customtkinter as ctk

class Camera_Configuration_Controller():
    def __init__(self, camera_configuration):
        self.camera_configuration = camera_configuration
        #Variable to check if the button is pressed or not
        self.is_countdown_button_pressed = False
    #Swap capture button and gif mode button
    def set_countdown_time(self, countdown_time):
        self.camera_configuration.capture_screen.controller.countdown_time = countdown_time
        self.camera_configuration.capture_screen.controller.countdown_time_temp = countdown_time
        self.is_countdown_button_pressed = False