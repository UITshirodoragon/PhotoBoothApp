import customtkinter as ctk
from PIL import Image, ImageTk
import cv2
import sys
import os
# Đường dẫn tới folder chứa module 
package_controller_path = os.path.abspath(os.path.join('..', 'PhotoBoothApp'))
if package_controller_path not in sys.path:
    sys.path.append(package_controller_path)
from AppInterface.define import *
from AppController import HandDetector as HD



class Image_Capture_Controller():
    def __init__(self, capture_screen):
        self.capture_screen = capture_screen
        self.is_captured_yet = False
        self.is_capturing = False #variable for hand detector
        self.just_captured_image_path = None
        self.countdown_time = 3
        self.countdown_time_temp = self.countdown_time
        self.Captured_numbers = 0
        self.five_fingers_on = False #Check if 5 fingers are on to ready capture when user close their hand
        self.handDetector = HD.handDetector(detectionCon=0.75)
        #Load trained model
        self.net = cv2.dnn.readNetFromCaffe('DataStorage/models/deploy.prototxt.txt',
                                       'DataStorage/models/res10_300x300_ssd_iter_140000_fp16.caffemodel')
    def capture_and_update_gallery(self):
        if self.is_captured_yet:
                self.is_captured_yet = False
                self.is_capturing = False
                #Enable capture button
                self.capture_screen.capture_button.configure(state = 'normal', command = self.capture_and_update_gallery)
                self.capture_screen.gallery_button.configure(state = 'normal', command = self.capture_screen.go_to_gallery)
                self.capture_screen.camera_configuration.toggle_button.configure(state = 'normal', command = self.capture_screen.camera_configuration.Toggle_Slide)
                self.capture_screen.Return_template_screen_button.configure(state = 'normal', command = self.capture_screen.back_to_template_screen)
                captured_image_path = self.just_captured_image_path
                imageTk = ImageTk.PhotoImage(Image.open(captured_image_path).resize(((int(self.capture_screen.parent.winfo_width() * 0.6),
                                                                                     int(self.capture_screen.parent.winfo_height() * 43 / 60)))))
                captured_image_button = ctk.CTkButton(self.capture_screen.gallery.display_image_button_frame,
                                                        text ='',
                                                        width = int(self.capture_screen.parent.winfo_width() * 3 / 32),
                                                        height=int(self.capture_screen.parent.winfo_height() * 5 / 48),
                                                        bg_color=COLOR_SALT,
                                                        fg_color='transparent',
                                                        hover_color=COLOR_MINT,
                                                        image=ctk.CTkImage(light_image=Image.open(captured_image_path),
                                                                                dark_image=Image.open(captured_image_path),
                                                                                size = ((int(self.capture_screen.parent.winfo_width() * 3 / 32)),
                                                                                        int(self.capture_screen.parent.winfo_height() * 5 / 48))),
                                                        command = lambda index = self.capture_screen.gallery.controller.image_number: self.capture_screen.gallery.image_is_chosen(index))
                check_button = ctk.CTkCheckBox(captured_image_button,
                                               text = '',
                                               hover_color=COLOR_SKYBLUE,
                                               bg_color='transparent',
                                               checkmark_color=COLOR_PINEGREEN,
                                               fg_color=COLOR_MINT,
                                               width = 15,
                                               height= 15,
                                               onvalue= 1,
                                               offvalue= 0,
                                               command = lambda index = self.capture_screen.gallery.controller.image_number: self.capture_screen.gallery.controller.export_image(index))
                check_button.place(relx = 1, rely = 1, anchor = 'se')
                self.capture_screen.gallery.controller.list_image_Tk.append(imageTk)
                self.capture_screen.gallery.controller.list_export_image_check_button.append(check_button)
                self.capture_screen.gallery.controller.list_image_paths.append(captured_image_path)
                self.capture_screen.gallery.controller.list_image_button.append(captured_image_button)
                self.capture_screen.gallery.controller.image_number += 1
                self.capture_screen.gallery.gallery_images_update()
        else:
                #Disable capture button
                self.capture_screen.capture_button.configure(state = 'disable', command = None)
                self.capture_screen.gallery_button.configure(state = 'disable', command = None)
                self.capture_screen.camera_configuration.toggle_button.configure(state = 'disable', command = None)
                self.capture_screen.Return_template_screen_button.configure(state = 'disable', command = None)
                if self.capture_screen.camera_configuration.at_start_position == False:
                        self.capture_screen.camera_configuration.Toggle_Slide()
                self.is_capturing = True
                #Capture
                self.Countdown()
                #Wait for image is captured then update gallery
                self.capture_screen.gallery.after(int((self.countdown_time + 0.5) * 1000), self.capture_and_update_gallery)
    
    def Take_Picture(self):
        ret, frame = self.capture_screen.cap.read()
        # Check if image is successfully captured
        if ret:
            self.Captured_numbers +=1
            self.capture_screen.Notification_label.configure(text = 'Captured successfully')
            cv2.imwrite(f'DataStorage/ImageGallery/image{self.Captured_numbers}.png', frame) # Save image
            #Tell that an image is captured
            self.is_captured_yet = True
            self.just_captured_image_path = f'DataStorage/ImageGallery/image{self.Captured_numbers}.png'
        else:
            self.capture_screen.Notification_label.configure(text = 'Captured unsuccessfully')
        self.capture_screen.Notification_label.place(relx = 0.5, rely = 0.5, anchor = 'center') # layout nofitication
        self.capture_screen.Notification_label.after(500, self.capture_screen.Notification_label.place_forget) # close the nofitication

    def Countdown(self):
        if self.countdown_time_temp > 0:            
            self.capture_screen.countdown_label.configure(text = f'{self.countdown_time_temp}')
            self.capture_screen.countdown_label.place(relx=0.5, rely=0.5, anchor = 'center')
            self.countdown_time_temp -= 1
            self.capture_screen.after(1000, self.Countdown)
        else:
            self.countdown_time_temp = self.countdown_time
            self.capture_screen.countdown_label.place_forget()
            self.Take_Picture()

    def hand_detected_capture(self, frame):
        frame = self.handDetector.findHands(frame, draw = False)
        list_fingers_position = self.handDetector.findPosition(frame, draw = False)

        if len(list_fingers_position) != 0:
            fingers_number = 0
            if list_fingers_position[8][1] > list_fingers_position[12][1]:
                if list_fingers_position[4][1] > list_fingers_position[3][1]:
                    fingers_number += 1
                for id in range (8, 21, 4):
                    if list_fingers_position[id][2] < list_fingers_position[id - 2][2]:
                        fingers_number += 1
            else:
                return None
        else:
            return None
        if fingers_number == 5:
            self.five_fingers_on = True
        if self.five_fingers_on and fingers_number == 0:
            self.five_fingers_on = False
            self.capture_and_update_gallery()
    
    def face_detector(self, frame):
        coordinate_list = []
        # Prepare input data
        blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), (104, 177, 123), swapRB = False) # Take a data of a picture to detect
        ''' frame: your picture
            1.0 : streching scale
            (300, 300) : require size of model for input
            (104, 177, 123) : average color of each pixels
            swapRB = false : not changing color channel (for here is changing red and blue channel)
        '''

        # Set data input into net
        self.net.setInput(blob)

        # Run to detect face
        faces = self.net.forward()
        #faces have 4 dimensions, use faces.shape to see: (number of input, number of output, number of face detected, number information of each detected face)
        '''every detected face have 7 informations in turn is:
            - image number order
            - class id (1 or 0): usually is 1 refer to face
            - confidence of detection
            - start x
            - start y
            - end x
            - end y
            * 4 coordinate is scaled in range [0, 1]'''
        # Get the input picture size
        h = frame.shape[0] # height
        w = frame.shape[1] # width

        for i in range(faces.shape[2]):
            confidence = faces[0, 0, i, 2] #Get the confidence
            if confidence > 0.4:
                #Extract coordiante
                startx = int(faces[0, 0, i, 3] * w)
                starty = int(faces[0, 0, i, 4] * h)
                endx = int(faces[0, 0, i, 5] * w)
                endy = int(faces[0, 0, i, 6] * h)
                cv2.rectangle(frame, (startx, starty), (endx, endy), ((234, 206, 158))) #Draw a bounding box with color skyblue
        return frame

