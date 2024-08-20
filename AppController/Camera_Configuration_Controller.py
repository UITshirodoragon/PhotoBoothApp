
class Camera_Configuration_Controller():
    def __init__(self, camera_configuration):
        
        self.gif_mode = True
        self.camera_configuration = camera_configuration
        #Variable to check if the button is pressed or not
        self.is_countdown_button_pressed = False
        self.flash_state = False
        
        # setting camera
    #Swap capture button and gif mode button
    def set_countdown_time(self, countdown_time):
        self.camera_configuration.capture_screen.controller.countdown_time = countdown_time
        self.camera_configuration.capture_screen.controller.countdown_time_temp = countdown_time
        self.is_countdown_button_pressed = False

    def turn_on_flash(self):
        self.flash_state = True
        
    
    def turn_off_flash(self):
        self.flash_state = False
        