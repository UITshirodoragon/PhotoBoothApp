import platform
import cv2
from picamera2 import Picamera2
from PIL import Image, ImageTk
import time

class Image_Capture_Controller:
    def __init__(self):
        #back-end
        # self.is_captured_yet = False
        # self.just_captured_image_path = None
        # self.Captured_numbers = 0
        #back_end?
        try:
            if platform.system() == 'Windows':
                #back-end CV2
                self.CVcam = cv2.VideoCapture(0) # Choose camera
                
            elif platform.system() == 'Linux': 
                #back-end Picamera
                self.camera = Picamera2()
                self.camera.preview_configuration.main.size = (1024, 600)
                self.camera.preview_configuration.main.format = "RGB888"
                self.camera.preview_configuration.align()
                self.camera.configure("preview")
                self.camera.start()
                
        except ImportError as e:
            # thay the bang log sau
            print(f"Lỗi nhập thư viện: {e}")
        except Exception as e:
            # thay the bang log sau
            print(f"Lỗi: {e}")    #back-end
        
        # self.preview_frame()
        
        
    def __del__(self):
        self.camera.close()

    # def startPreview(self):
    #     self.camera.start_preview()

    # def stopPreview(self):
    #     self.camera.stop_preview()

    # def captureImage(self, filename="image.jpg"):
    #     self.camera.capture(filename)


    #back-end
    def preview_frame(self):
        global image_Tk
        try:
            if platform.system() == 'Windows':
                
                _, frame = self.CVcam.read() # Get frame from camera
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA) #Convert color system
                img = Image.fromarray(frame)
                # .resize((self.parent.winfo_width(), self.parent.winfo_height())) # transfer an array to img
                image_Tk = ImageTk.PhotoImage(image=img)
                # self.capture_frame.create_image(0,0, image = image_Tk, anchor = 'nw')
                # self.capture_frame.after(10, self.Update_frame) # Call the Update_Frame() method after every 10 miliseconds
                return image_Tk
                
            elif platform.system() == 'Linux':
                
                frame = self.camera.capture_array("main")
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
                img = Image.fromarray(frame)
                image_Tk = ImageTk.PhotoImage(image = img)
                # label.imgtk = image_tk
                # label.configure(image=image_tk)
                # root.after(1, update_frame)
                return image_Tk
                
            else:
                raise Exception("Hệ điều hành không được hỗ trợ.")
                 
        except ImportError as e:
            # thay the bang log sau
            print(f"Lỗi nhập thư viện: {e}")
        except Exception as e:
            # thay the bang log sau
            print(f"Lỗi: {e}")    #back-end
            
            
    def capture(self):
        try:
            if platform.system() == 'Windows':
                return self.CVcam.read()
            elif platform.system() == 'Linux':
                return Image.fromarray( self.camera.capture_image("main"))
            
        except:
            print("Lỗi!")
            
    
    def capture_and_save_image(self, path = None):
        try:
            
            if platform.system() == 'Windows':
                
                image = self.CVcam.read()
                self.CVcam.imwrite(path, image)
            elif platform.system() == 'Linux':
                
                capture_config = self.camera.create_still_configuration()
                self.camera.switch_mode_and_capture_file( capture_config, path)     
        except:
            print("Lỗi!")
        
    # def Take_Picture(self):
    #     ret, frame = self.cap.read()
    #     # Check if image is successfully captured
    #     if ret:
    #         self.Captured_numbers +=1
    #         self.Notification_label.configure(text = 'Captured successfully')
    #         cv2.imwrite(f'DataStorage/ImageGallery/image{self.Captured_numbers}.png', frame) # Save image
    #         #Tell that an image is captured
    #         self.is_captured_yet = True
    #         self.just_captured_image_path = f'DataStorage/ImageGallery/image{self.Captured_numbers}.png'
    #     else:
    #         self.Notification_label.configure(text = 'Captured unsuccessfully')
    #     self.Notification_label.place(relx = 0.5, rely = 0.5, anchor = 'center') # layout nofitication
    #     self.Notification_label.after(500, self.Notification_label.place_forget) # close the nofitication
        
    # #back-end    
    
    


