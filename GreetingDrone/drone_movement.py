from djitellopy import tello
from time import sleep
import cv2


# isMoving = False

# def isMoving():
#     return isMoving

def path_one(drone):
    # Use statement below when testing at home
    print("Weehee I'm flying to Path One!")

    drone.takeoff()
    drone.move_up(50)  # avoid tables and people
    sleep(2)

    drone.rotate_clockwise(90)
    drone.move_forward(50)
    drone.rotate_counter_clockwise(90)
    drone.move_forward(50)
    drone.rotate_clockwise(90)
    sleep(2)

    drone.move_forward(300)
    drone.move_forward(200)

    sleep(2)

    drone.rotate_counter_clockwise(90)
    drone.move_forward(100)
    drone.rotate_clockwise(180)
    # drone.move_down(50)
    # drone.land();
    #
    # reverse code

    sleep(2)

    # drone.takeoff()
    # drone.move_up(50)  # avoid tables and people
    # sleep(2)
    drone.move_forward(100)
    drone.rotate_clockwise(90)
    sleep(2)
    drone.move_forward(200)
    drone.move_forward(300)
    # drone.move_forward(290)
    sleep(2)
    drone.rotate_counter_clockwise(90)
    drone.move_forward(50)
    drone.rotate_clockwise(90)
    drone.move_forward(50)
    drone.rotate_clockwise(90)
    # drone.move_down(50)
    drone.land()

def path_one_old(drone):
    # Use statement below when testing at home
    print("Weehee I'm flying to Path One!")

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

    # reverse code

    sleep(2)

    drone.takeoff()
    drone.move_up(50)  # avoid tables and people
    sleep(2)
    drone.move_forward(100)
    drone.rotate_counter_clockwise(90)
    sleep(2)
    drone.move_forward(300)
    drone.move_forward(300)
    drone.move_forward(290)
    sleep(2)
    drone.rotate_counter_clockwise(90)
    drone.move_forward(70)
    drone.rotate_clockwise(90)
    drone.move_forward(50)
    drone.rotate_clockwise(90)
    drone.move_down(50)
    drone.land()

def path_two(drone):
    # Use statement below when testing at home
    print("Weehee I'm flying to Path Two!")
    #
    drone.takeoff()
    drone.move_up(50)  # avoid tables and people
    sleep(2)

    drone.rotate_clockwise(90)
    drone.move_forward(50)
    drone.rotate_counter_clockwise(90)
    drone.move_forward(50)
    drone.rotate_clockwise(90)
    sleep(2)

    drone.move_forward(270)
    drone.rotate_clockwise(90)
    drone.move_forward(125)
    sleep(2)
    drone.rotate_clockwise(180)
    # drone.move_down(50)
    # drone.land()

    # reverse code
    # sleep(2)

    # drone.takeoff()
    # drone.move_up(50)
    sleep(2)

    drone.move_forward(125)
    drone.rotate_counter_clockwise(90)
    drone.move_forward(270)

    sleep(2)
    drone.rotate_counter_clockwise(90)
    drone.move_forward(50)
    drone.rotate_clockwise(90)
    drone.move_forward(50)
    drone.rotate_clockwise(90)
    sleep(2)
    drone.land()

def path_two_old(drone):
    # Use statement below when testing at home
    print("Weehee I'm flying to Path Two!")

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
    drone.land()

    # reverse code
    # sleep(2)
    #
    # drone.takeoff()
    # # drone.move_up(50)  # avoid tables and people
    # sleep(2)
    #
    # drone.move_forward(100)
    # drone.rotate_clockwise(90)
    # drone.move_forward(100)
    #
    # sleep(2)
    # drone.rotate_counter_clockwise(90)
    # drone.move_forward(70)
    # drone.rotate_clockwise(90)
    # drone.move_forward(50)
    # drone.rotate_clockwise(90)
    # sleep(2)
    # drone.land()
