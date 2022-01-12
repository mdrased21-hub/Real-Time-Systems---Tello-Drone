from djitellopy import tello
from time import sleep

donna = tello.Tello()
donna.connect()
print(donna.get_battery())

donna.takeoff()
# donna.move_forward(50, 10)
donna.send_rc_control(0, 20, 0, 0) # velocity (-100 - 100): left-right, forward-backward, up-down, yaw
sleep(5)
donna.send_rc_control(20, 0, 0, 0) # velocity (-100 - 100): left-right, forward-backward, up-down, yaw
sleep(5)
donna.land()
