# youtube tutorial >> https://youtu.be/ddSo8Nb0mTw

# import numpy as np
import cv2
import numpy as np


# SETUP CAMERA
capture = cv2.VideoCapture(0)

# SETUP COLOUR PICKER
def nothing(x):
    pass

# LIST OF ALL COLOR PICKER PRESET
blue = [[94, 80, 2], [126, 255, 255]]
red = [[161, 155, 84], [179, 255, 255]]
selectedIntialBound = blue

cv2.namedWindow("Colour Picker LB")
cv2.createTrackbar("H", "Colour Picker LB", selectedIntialBound[0][0], 179, nothing)
cv2.createTrackbar("S", "Colour Picker LB", selectedIntialBound[0][1], 255, nothing)
cv2.createTrackbar("V", "Colour Picker LB", selectedIntialBound[0][2], 255, nothing)

cv2.namedWindow("Colour Picker HB")
cv2.createTrackbar("H", "Colour Picker HB", selectedIntialBound[1][0], 179, nothing)
cv2.createTrackbar("S", "Colour Picker HB", selectedIntialBound[1][1], 255, nothing)
cv2.createTrackbar("V", "Colour Picker HB", selectedIntialBound[1][2], 255, nothing)

img_hsv_lower = np.zeros((250, 500, 3), np.uint8)
img_hsv_higher = np.zeros((250, 500, 3), np.uint8)

while True:

    # setup colour picker's slider
    h_lower, h_higher = cv2.getTrackbarPos("H", "Colour Picker LB"), cv2.getTrackbarPos("H", "Colour Picker HB")
    s_lower, s_higher = cv2.getTrackbarPos("S", "Colour Picker LB"), cv2.getTrackbarPos("S", "Colour Picker HB")
    v_lower, v_higher = cv2.getTrackbarPos("V", "Colour Picker LB"), cv2.getTrackbarPos("V", "Colour Picker HB")

    img_hsv_lower[:], img_hsv_higher[:] = (h_lower, s_lower, v_lower), (h_higher, s_higher, v_higher)
    img_bgr_lower, img_bgr_higher = cv2.cvtColor(img_hsv_lower, cv2.COLOR_HSV2BGR), cv2.cvtColor(img_hsv_higher, cv2.COLOR_HSV2BGR)

    cv2.imshow("Colour Picker LB", img_bgr_lower)
    cv2.imshow("Colour Picker HB", img_bgr_higher)

    # get the frame
    _ , frame = capture.read()

    # get the dimension of the frame
    height, width, _ = frame.shape

    # change the image to hsv (hue, saturation, lightness) image
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    # get colour bound
    lower_colour_bound = np.array([h_lower, s_lower, v_lower])
    upper_colour_bound = np.array([h_higher, s_higher, v_higher])

    # create a mask
    mask = cv2.inRange(hsv_frame, lower_colour_bound, upper_colour_bound)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # get the center pixel
    cx = int(width / 2)
    cy = int(height / 2)
    pixel_center = hsv_frame[cy, cx]
    # print(pixel_center)

    # DRAW CENTER PIXEL TARGET
    cv2.circle(frame, (cx, cy), 5, (255, 255, 255), 3)
    cv2.circle(result, (cx, cy), 5, (255, 255, 255), 3)



    # check HSV colour values
    # HUE
    if  h_lower<= pixel_center[0] and pixel_center[0]<=h_higher:
        hue_flag = True
    else:
        hue_flag = False

    # SATURATION
    if s_lower <= pixel_center[1] and pixel_center[1] <= s_higher:
        saturation_flag = True
    else:
        saturation_flag = False

    # LIGHTNESS
    if v_lower <= pixel_center[2] and pixel_center[2] <= v_higher:
        lightness_flag = True
    else:
        lightness_flag = False

    print([hue_flag, saturation_flag, lightness_flag])
    if hue_flag == True and saturation_flag == True and lightness_flag == True:
        cv2.circle(frame, (cx, cy), 15, (255, 255, 255), 3)
        cv2.circle(frame, (cx, cy), 25, (255, 255, 255), 3)
        cv2.circle(result, (cx, cy), 15, (255, 255, 255), 3)
        cv2.circle(frame, (cx, cy), 25, (255, 255, 255), 3)
        print("COLOUR DETECTED")



    cv2.imshow("Original Frame", frame)
    cv2.imshow("Masked Frame", result)

    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()