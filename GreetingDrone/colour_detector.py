# youtube tutorial >> https://youtu.be/ddSo8Nb0mTw

# import numpy as np
import cv2
import numpy as np
import drone_movement as drone
from djitellopy import tello
import threading
from time import sleep

# method tho check confirm the colour
def checkForColour(pixel_center, h_lower, h_higher, s_lower, s_higher, v_lower, v_higher):
    hue_flag = False
    saturation_flag = False
    lightness_flag = False

    # check HSV colour values
    # HUE
    if h_lower <= pixel_center[0] and pixel_center[0] <= h_higher:
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

    if hue_flag == True and saturation_flag == True and lightness_flag == True:
        return True
    else:
        return False



def color(tello_drone):
    t1 = threading.Thread(target=drone.moveDrone, args=(tello_drone,))
    t2 = threading.Thread(target=drone.pathTwo, args=(tello_drone,))

    # SETUP CAMERA
    capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    # SETUP COLOUR PICKER
    def nothing(x):
        pass

    # LIST OF ALL COLOR PICKER PRESET
    blue = [[94, 80, 2], [126, 255, 255]]
    red = [[161, 155, 84], [179, 255, 255]]

    # Create slider for fine tune colour
    cv2.namedWindow("Colour Picker Blue", cv2.WINDOW_FREERATIO)
    cv2.createTrackbar("H-Lower Bound", "Colour Picker Blue", blue[0][0], 179, nothing)
    cv2.createTrackbar("S-Lower Bound", "Colour Picker Blue", blue[0][1], 255, nothing)
    cv2.createTrackbar("V-Lower Bound", "Colour Picker Blue", blue[0][2], 255, nothing)
    cv2.createTrackbar("H-Higher Bound", "Colour Picker Blue", blue[1][0], 179, nothing)
    cv2.createTrackbar("S-Higher Bound", "Colour Picker Blue", blue[1][1], 255, nothing)
    cv2.createTrackbar("V-Higher Bound", "Colour Picker Blue", blue[1][2], 255, nothing)
    cv2.resizeWindow("Colour Picker Blue", 300, 300)

    cv2.namedWindow("Colour Picker Red", cv2.WINDOW_FREERATIO)
    cv2.createTrackbar("H-Lower Bound", "Colour Picker Red", red[0][0], 179, nothing)
    cv2.createTrackbar("S-Lower Bound", "Colour Picker Red", red[0][1], 255, nothing)
    cv2.createTrackbar("V-Lower Bound", "Colour Picker Red", red[0][2], 255, nothing)
    cv2.createTrackbar("H-Higher Bound", "Colour Picker Red", red[1][0], 179, nothing)
    cv2.createTrackbar("S-Higher Bound", "Colour Picker Red", red[1][1], 255, nothing)
    cv2.createTrackbar("V-Higher Bound", "Colour Picker Red", red[1][2], 255, nothing)
    cv2.resizeWindow("Colour Picker Red", 300, 300)

    # prepare hsv array
    img_hsv_lower_BLUE = img_hsv_lower_RED = np.zeros((250, 500, 3), np.uint8)
    img_hsv_higher_BLUE = img_hsv_higher_RED = np.zeros((250, 500, 3), np.uint8)


    while True:
        # while the color is not detected the this loop will continue iterating:

        # setup colour picker's slider [BLUE]
        h_BLUE_lower, h_BLUE_higher = cv2.getTrackbarPos("H-Lower Bound", "Colour Picker Blue"), cv2.getTrackbarPos("H-Higher Bound", "Colour Picker Blue")
        s_BLUE_lower, s_BLUE_higher = cv2.getTrackbarPos("S-Lower Bound", "Colour Picker Blue"), cv2.getTrackbarPos("S-Higher Bound", "Colour Picker Blue")
        v_BLUE_lower, v_BLUE_higher = cv2.getTrackbarPos("V-Lower Bound", "Colour Picker Blue"), cv2.getTrackbarPos("V-Higher Bound", "Colour Picker Blue")

        img_hsv_lower_BLUE[:], img_hsv_higher_BLUE[:] = (h_BLUE_lower, s_BLUE_lower, v_BLUE_lower), (h_BLUE_higher, s_BLUE_higher, v_BLUE_higher)
        img_bgr_lower_BLUE, img_bgr_higher_BLUE = cv2.cvtColor(img_hsv_lower_BLUE, cv2.COLOR_HSV2BGR), cv2.cvtColor(img_hsv_higher_BLUE, cv2.COLOR_HSV2BGR)

        cv2.imshow("Blue-Lower-Bound", img_bgr_lower_BLUE)
        cv2.resizeWindow("Blue-Lower-Bound", 300, 100)
        cv2.imshow("Blue-Higher-Bound", img_bgr_higher_BLUE)
        cv2.resizeWindow("Blue-Higher-Bound", 300, 100)

        # setup colour picker's slider [RED]
        h_RED_lower, h_RED_higher = cv2.getTrackbarPos("H-Lower Bound", "Colour Picker Red"), cv2.getTrackbarPos("H-Higher Bound", "Colour Picker Red")
        s_RED_lower, s_RED_higher = cv2.getTrackbarPos("S-Lower Bound", "Colour Picker Red"), cv2.getTrackbarPos("S-Higher Bound", "Colour Picker Red")
        v_RED_lower, v_RED_higher = cv2.getTrackbarPos("V-Lower Bound", "Colour Picker Red"), cv2.getTrackbarPos("V-Higher Bound", "Colour Picker Red")

        img_hsv_lower_RED[:], img_hsv_higher_RED[:] = (h_RED_lower, s_RED_lower, v_RED_lower), (h_RED_higher, s_RED_higher, v_RED_higher)
        img_bgr_lower_RED, img_bgr_higher_RED = cv2.cvtColor(img_hsv_lower_RED, cv2.COLOR_HSV2BGR), cv2.cvtColor(img_hsv_higher_RED, cv2.COLOR_HSV2BGR)

        cv2.imshow("Red-Lower-Bound", img_bgr_lower_RED)
        cv2.resizeWindow("Red-Lower-Bound", 300, 100)
        cv2.imshow("Red-Higher-Bound", img_bgr_higher_RED)
        cv2.resizeWindow("Red-Higher-Bound", 300, 100)



        # get the frame
        _, frame_Og = capture.read()
        frame_BLUE = frame_RED = frame_Og;


        # get the dimension of the frame
        height, width, _ = frame_Og.shape

        # change the image to hsv (hue, saturation, lightness) image
        hsv_frame_Og = cv2.cvtColor(frame_Og, cv2.COLOR_BGR2HSV)
        hsv_frame_BLUE = hsv_frame_RED = hsv_frame_Og


        # get colour bound
        lower_colour_bound_BLUE = np.array([h_BLUE_lower, s_BLUE_lower, v_BLUE_lower])
        upper_colour_bound_BLUE = np.array([h_BLUE_higher, s_BLUE_higher, v_BLUE_higher])

        lower_colour_bound_RED = np.array([h_RED_lower, s_RED_lower, v_RED_lower])
        upper_colour_bound_RED = np.array([h_RED_higher, s_RED_higher, v_RED_higher])


        # create a mask
        mask_BLUE = cv2.inRange(hsv_frame_BLUE, lower_colour_bound_BLUE, upper_colour_bound_BLUE)
        result_BLUE = cv2.bitwise_and(frame_BLUE, frame_BLUE, mask=mask_BLUE)

        mask_RED = cv2.inRange(hsv_frame_RED, lower_colour_bound_RED, upper_colour_bound_RED)
        result_RED = cv2.bitwise_and(frame_RED, frame_RED, mask=mask_RED)





        # get the center pixel
        cx = int(width / 2)
        cy = int(height / 2)
        pixel_center = hsv_frame_Og[cy, cx]
        # print(pixel_center)

        # DRAW CENTER PIXEL TARGET
        cv2.circle(frame_Og, (cx, cy), 5, (255, 255, 255), 3)
        cv2.circle(result_BLUE, (cx, cy), 5, (255, 255, 255), 3)
        cv2.circle(result_RED, (cx, cy), 5, (255, 255, 255), 3)


        if checkForColour(pixel_center, h_BLUE_lower, h_BLUE_higher, s_BLUE_lower, s_BLUE_higher, v_BLUE_lower, v_BLUE_higher):
            print("----------BLUE COLOUR DETECTED----------")
            cv2.circle(frame_Og, (cx, cy), 15, (255, 255, 255), 3)
            cv2.circle(frame_Og, (cx, cy), 25, (255, 255, 255), 3)
            cv2.circle(result_BLUE, (cx, cy), 15, (255, 255, 255), 3)
            cv2.circle(result_BLUE, (cx, cy), 25, (255, 255, 255), 3)
            # if not t1.is_alive() and not t2.is_alive():
            #     t1.start()

        if checkForColour(pixel_center, h_RED_lower, h_RED_higher, s_RED_lower, s_RED_higher, v_RED_lower, v_RED_higher):
            print("----------RED COLOUR DETECTED----------")
            cv2.circle(frame_Og, (cx, cy), 15, (255, 255, 255), 3)
            cv2.circle(frame_Og, (cx, cy), 25, (255, 255, 255), 3)
            cv2.circle(result_RED, (cx, cy), 15, (255, 255, 255), 3)
            cv2.circle(result_RED, (cx, cy), 25, (255, 255, 255), 3)
            # if not t1.is_alive() and not t2.is_alive():
            #     t2.start()



        cv2.imshow("Original Frame", frame_Og)
        cv2.imshow("result_red", result_RED)
        cv2.imshow("result_blue", result_BLUE)


        if cv2.waitKey(1) == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()
