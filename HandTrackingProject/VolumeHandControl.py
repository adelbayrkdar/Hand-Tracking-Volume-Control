import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

###########################
wCam, hCam = 640, 480
###########################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.HandDetector(detection_confidence=0.7)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]
vol_lock = False  # Variable to track the volume lock status

while True:
    success, img = cap.read()
    img = detector.find_hands(img)
    hand_lms = detector.find_position(img, draw=False)

    if len(hand_lms) != 0:
        x1, y1 = hand_lms[4][1], hand_lms[4][2]
        x2, y2 = hand_lms[8][1], hand_lms[8][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        cv2.circle(img, (x1, y1), 8, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 8, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 2)
        cv2.circle(img, (cx, cy), 6, (255, 0, 255), cv2.FILLED)

        length = math.hypot(x2 - x1, y2 - y1)

        if length < 30:  # Gesture to potentially unlock volume control
            cv2.circle(img, (cx, cy), 6, (0, 255, 0), cv2.FILLED)  # Green button effect
            vol_lock = False

        if not vol_lock:
            vol = np.interp(length, [50, 300], [minVol, maxVol])
            volume.SetMasterVolumeLevel(vol, None)

            if vol >= maxVol * 0.95:  # Consider it as max volume if it's very close to 100%
                vol_lock = True

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (40, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    cv2.imshow("Img", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
