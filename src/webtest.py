from flask import Flask, render_template, redirect, url_for,request, Response
from camera import Camera
from Image import *
from recycable import *
from InfoRetriever import *

Im = Image()
R = Recyable()
app = Flask(__name__)
camera = None
mail_server = None
mail_conf = "static/mail_conf.json"

def get_camera():
    global camera
    if not camera:
        camera = Camera()
    return camera

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/takepic')
def takepic():
    return render_template("takepic.html")


def get_camera():
    global camera
    if not camera:
        camera = Camera()

    return camera


def gen(camera):
    while True:
        frame = camera.get_feed()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed/')
def video_feed():
    camera = get_camera()
    return Response(gen(camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/capture/')
def capture():
    camera = get_camera()
    stamp = camera.capture()
    return redirect(url_for('show_capture', timestamp=stamp))


def stamp_file(timestamp):
    return 'captures/' + timestamp + ".jpg"


@app.route('/capture/image/<timestamp>', methods=['POST', 'GET'])
def show_capture(timestamp):
    path = stamp_file(timestamp)

    return render_template('capture.html',
                           stamp=timestamp, path=path)

@app.route('/product/<p>', methods=['POST', 'GET'])
def productInfo(p):
    info = R.getRecycableInfo(p)
    return render_template('info.html', item = p, info = info)

@app.route('/upload/')
def upload():
    return render_template('imageupload.html')

@app.route('/uploader/', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        return 'file uploaded successfully'

@app.route('/analyze/', methods=['GET', 'POST'])
def analyze():
    I = Image()
    if request.method == 'POST':
        I.image = request.form['image'][1:]
        I.findLabels()
        In = InfoRetriever(R.getRecycables())
        L = []
        for i in I.labels[:8]:
            # print(I.findMatching(i.description))
            L.append(In.findMatching(i.description))
        Sort_Tuple(L)
        list = [el[0] for el in L]
    return render_template('analyzed.html', labels = list[0:len(list)//2])
if __name__ == "__main__":
    app.run(debug=True)