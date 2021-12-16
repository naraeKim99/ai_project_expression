from classifier import Predict
from melonC import MELONimpassive, MELONmusic
from bugsC import BUGSmusic, BUGSimpassive
from floC import FLOimpassive, FLOmusic
from genieC import GENIEimpassive, GENIEmusic

import json
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER']="C:/빅데이터양성/프로젝트/server/uploads"
app.config['MAX_CONTENT_LENGTH']=20*1024*1024   #20mb 이내

x, sentence= "", ""


# upload html rendering
@app.route('/')
def render_file():
    return render_template('Home.html')


@app.route('/fileUpload', methods=['GET','POST'])
def upload_file():
    global x, sentence

    # file을 classifier를 사용하여 판별
    file = request.files['file']
    if file: #파일을 업로드 했다면 
        print(file.filename)
        filename = file.filename
        sfilename = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(sfilename)
    
        x, sentence=Predict(sfilename)
        print(x, sentence, sfilename)


    # !!! json은 습관적으로 이중따옴표 사용 !!!
    return json.dumps(
        {'sentence':sentence
        })



@app.route('/getMelon', methods=['GET','POST'])
def getMelon():
    global x

    if x=='impassive':
        playList=MELONimpassive()
    else:
        playList=MELONmusic(x)

    # !!! json은 습관적으로 이중따옴표 사용 !!!
    return json.dumps(
    playList)




@app.route('/getBugs', methods=['GET','POST'])
def getBugs():
    global x

    if x=='impassive':
        playList=BUGSimpassive()
    else:
        playList=BUGSmusic(x)

    # !!! json은 습관적으로 이중따옴표 사용 !!!
    return json.dumps(
    playList)


@app.route('/getFlo', methods=['GET','POST'])
def getFlo():
    global x

    if x=='impassive':
        playList=FLOimpassive()
    else:
        playList=FLOmusic(x)

    # !!! json은 습관적으로 이중따옴표 사용 !!!
    return json.dumps(
    playList)


@app.route('/getGenie', methods=['GET','POST'])
def getGenie():
    global x

    if x=='impassive':
        playList=GENIEimpassive()
    else:
        playList=GENIEmusic(x)

    # !!! json은 습관적으로 이중따옴표 사용 !!!
    return json.dumps(
    playList)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port="5000")