from djitellopy import tello
from time import sleep
import cv2

# isMoving = False

# def isMoving():
#     return isMoving

def moveDrone(drone):
    
    # Use statement below when testing at home
    print("Weehee I'm flying!")

    drone.takeoff()
    drone.move_up(50)  # avoid tables and people
    sleep(2)

    drone.rotate_clockwise(90)
    drone.move_forward(50)
    drone.rotate_counter_clockwise(90)
    drone.move_forward(70)
    drone.rotate_clockwise(90)
    sleep(2)

    drone.move_forward(300)
    drone.move_forward(300)
    drone.move_forward(290)

    sleep(2)

    drone.rotate_clockwise(90)
    drone.move_forward(100)
    drone.rotate_clockwise(180)
    drone.move_down(50)
    drone.land();


def pathTwo(drone):

    # Use statement below when testing at home
    print("Weehee I'm flying!")

    drone.takeoff()
    drone.move_up(50)  # avoid tables and people
    sleep(2)

    drone.rotate_clockwise(90)
    drone.move_forward(50)
    drone.rotate_counter_clockwise(90)
    drone.move_forward(70)
    drone.rotate_clockwise(90)
    sleep(2)

    drone.move_forward(100)
    drone.rotate_counter_clockwise(90)
    drone.move_forward(100)
    sleep(2)
    drone.rotate_clockwise(180)
    # drone.move_down(50)
    drone.land();