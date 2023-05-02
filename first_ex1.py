from picamera2 import Picamera2, Preview 
import time

picam2 = Picamera2()
print("hello1")
camera_config = picam2.create_preview_configuration() 
print("hello2")
picam2.configure(camera_config) 
print("hello3")
picam2.start_preview(Preview.QTGL)
print("hello4")
picam2.start()
time.sleep(2)
print("hello5")
picam2.capture_file("test.jpg")