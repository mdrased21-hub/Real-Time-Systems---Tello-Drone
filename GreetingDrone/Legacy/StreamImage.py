from djitellopy import tello
import cv2

donna = tello.Tello()
donna.connect()
print(donna.get_battery())

donna.streamon()

# To get continuous frame we use while loop
while True:
    img = donna.get_frame_read().frame
   # img = cv2.resize(img, (360, 240)) #resize for faster processing
    cv2.imshow("Donna's view", img) # window
    cv2.waitKey(1) # delay to avoid the frame shutdown before we see it
