from djitellopy import tello
import threading
import drone_movement as drone

dollah = tello.Tello()
dollah.connect()
a = dollah.get_battery()
# a = 50
thread = threading.Thread(target=drone.path_one, args=(dollah,))
