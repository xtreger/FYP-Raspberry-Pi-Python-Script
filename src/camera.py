import cv2
from imutils.video.pivideostream import PiVideoStream
import imutils
import time
import numpy as np
#import requests

fgbg = cv2.createBackgroundSubtractorMOG2(300, 400, True)



class VideoCamera(object):
    
    def __init__(self, flip = False):
        self.vs = PiVideoStream(resolution=(480,282)).start()
        self.flip = flip
        self.count2 = 1
        time.sleep(2.0)

    def __del__(self):
        self.vs.stop()

    def flip_if_needed(self, frame):
        if self.flip:
            return np.flip(frame, 0)
        return frame

    def get_frame(self):
        frame = self.flip_if_needed(self.vs.read())
        
        resizedFrame = cv2.resize(frame, (0, 0), fx=0.50, fy=0.50)
        fgmask = fgbg.apply(resizedFrame)
        count = np.count_nonzero(fgmask)
        if (count > 500):
            self.count2 = 1
            #print('Movement Detected: %d' % (count2))
            #cv2.putText(frame, 'Movement Detected', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        else:
            self.count2 = 0
            
        ret, jpeg = cv2.imencode('.jpg', frame)
        #response = requests.put('https://finalyearproject-mihai-default-rtdb.europe-west1.firebasedatabase.app/motion.json', data = {'motion':self.count2})
        return jpeg.tobytes()
    
    def motion_value(self):
        return self.count2
    