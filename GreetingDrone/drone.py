from djitellopy import tello
import threading
import drone_movement as drone

dollah = tello.Tello()
# dollah.connect()
# a = dollah.get_battery()
thread = threading.Thread(target=drone.path_one, args=(dollah,))
