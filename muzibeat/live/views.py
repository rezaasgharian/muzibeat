from urllib import request

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import StreamingHttpResponse
from django.http import HttpResponse
import cv2
import threading
from django.views.decorators import gzip


# Create your views here.
@gzip.gzip_page
@login_required(login_url='/login/')
def Home(request):
    x = request.GET.get('value')
    print(x)
    return render(request, 'live/stream.html')


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()


    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()


def gen(camera):
    while True:

        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n'
               )


def stream(request):
    cam = VideoCamera()
    return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    # elif request.method == "POST":
    #     cam = VideoCamera()
    #     return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
