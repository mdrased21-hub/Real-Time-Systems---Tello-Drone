import cv2
import numpy as np
import mediapipe as mp
import drone
import drone_movement as movements
import threading
from tensorflow.keras.models import load_model


def gesture(tello_drone):
    # drone.thread = threading.Thread(target=drone.path_one, args=(tello_drone,))

    # initialize mediapipe
    mpHands = mp.solutions.hands
    hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
    mpDraw = mp.solutions.drawing_utils

    # Load the gesture recognizer model
    model = load_model('mp_hand_gesture')

    # Load class names
    f = open('gesture.names', 'r')
    classNames = f.read().split('\n')
    f.close()
    print(classNames)


    # Initialize the webcam
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    while True:
        # Read each frame from the webcam
        _, frame = cap.read()

        x, y, c = frame.shape

        # Flip the frame vertically
        frame = cv2.flip(frame, 1)
        framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Get hand landmark prediction
        result = hands.process(framergb)

        # print(result)

        className = ''

        # post process the result
        if result.multi_hand_landmarks:
            landmarks = []
            for handslms in result.multi_hand_landmarks:
                for lm in handslms.landmark:
                    # print(id, lm)
                    lmx = int(lm.x * x)
                    lmy = int(lm.y * y)

                    landmarks.append([lmx, lmy])

                # Drawing landmarks on frames
                mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS,
                                         mpDraw.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                                        mpDraw.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                                    )

                # Predict gesture
                prediction = model.predict([landmarks])
                # print(prediction)
                classID = np.argmax(prediction)
                className = classNames[classID]

        # show the prediction on the frame
        cv2.putText(frame, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                       1, (121, 22, 76), 2, cv2.LINE_AA)

        # Show the final output
        cv2.imshow("Output", frame)

        if className=='okay':
            print("----------OKAY GESTURE DETECTED----------")
            # START: TELLO DRONE MOVEMENT
            # //
            if not drone.thread.is_alive():
                drone.thread = threading.Thread(target=movements.path_one, args=(tello_drone,))
                drone.thread.start()
            # //
            # END: TELLO DRONE MOVEMENT

        if className=='peace':
            print("----------PEACE GESTURE DETECTED----------")
            # START: TELLO DRONE MOVEMENT
            # //
            if not drone.thread.is_alive():
                drone.thread = threading.Thread(target=movements.path_two, args=(tello_drone,))
                drone.thread.start()
            # //
            # END: TELLO DRONE MOVEMENT

        # if cv2.waitKey(1) == ord('q') or className=='smile':
        if cv2.waitKey(1) == ord('q'):
            break

    # release the webcam and destroy all active windows
    cap.release()

    cv2.destroyWindow("Output")