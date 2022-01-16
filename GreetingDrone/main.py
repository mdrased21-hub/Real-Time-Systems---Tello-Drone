import PySimpleGUI as sg  # Part 1 - The import
import colour_detector as colorDetect
import gestures as gestureDetect
import threading
import drone
# import drone_movement as movements

a=50


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
        threading.Thread(target=colorDetect.color, args=(drone.dollah,)).start()
    if event == "Gesture Recognition":
        threading.Thread(target=gestureDetect.gesture, args=(drone.dollah,)).start()
    if event == "Cancel" or event == sg.WINDOW_CLOSED:
        break

window.close()

if drone.thread.is_alive():
    drone.thread.join()
