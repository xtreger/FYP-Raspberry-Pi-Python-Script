# import the necessary packages
from flask import Flask, render_template, Response, request, jsonify
from camera import VideoCamera
import time
import threading
import os


# flip pi camera if upside down.
pi_camera = VideoCamera(flip=False)

app = Flask(__name__)

def gen(camera):
    #get camera frame
    while True:
    
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/Fas3Tdg4Ffg2DF5DertThG')
def video_feed():
    return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/motion')
def motion(camera=pi_camera):
    d = camera.motion_value()
    data = {'motion': d}
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
    

    


