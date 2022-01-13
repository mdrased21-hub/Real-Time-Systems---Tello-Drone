import PySimpleGUI as sg  # Part 1 - The import
import colour_detector as colorDetect
import gestures as gestureDetect
import threading
from djitellopy import tello


# a=50

dollah = tello.Tello()
dollah.connect()
a = dollah.get_battery()

# print()
sg.theme('DarkPurple1')

layout = [[sg.Text("Welcome, you will be greeted by our drone")],
          [sg.Text("Drone Battery Percentage "+str(a)+"%")],
          [sg.Button('Color Recognition')],
          [sg.Button('Gesture Recognition')],
          [sg.Cancel()]]
window = sg.Window('Event Greeter', layout, size=(480,320))

# t1 = threading.Thread(target=colorDetect.color, args=(dollah,))
# t2 = threading.Thread(target=gestureDetect.gesture, args=(dollah,))

while True:
    event, values = window.read()
    if event == "Color Recognition":
        threading.Thread(target=colorDetect.color, args=(dollah,)).start()
    if event == "Gesture Recognition":
        threading.Thread(target=gestureDetect.gesture, args=(dollah,)).start()
    if event == "Cancel" or event == sg.WINDOW_CLOSED:
        break

window.close()

# if t1.is_alive():
#     t1.join()
# if t2.is_alive():
#     t2.join()