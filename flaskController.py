from flask import *
import requests
import json
import shutil
import os
app=Flask(__name__,template_folder="templates")

def isNone(arr):
    if arr==None or arr==[]:
        arr=None

@app.route("/chat",methods=['GET','POST'])
def chat():
    if request.method=='GET':
        return render_template('chatting.html')
    else:
        url="https://api.dictionaryapi.dev/api/v2/entries/en/"+request.form["para"]
        res=requests.get(url=url)
        image="https://www.googleapis.com/customsearch/v1?q="+request.form["para"]+"&cx=f4588efa05b504002&searchType=image&key=AIzaSyBzr_NQcIKXM3JnkeMxW4lPwa0tdwkHCMY"

        resImg=requests.get(url=image)

        imgJson=resImg.json()
        if resImg.status_code == requests.codes.ok:
           img=imgJson["items"][0]["link"]
           print("=========="+img+"=============")
        else:
            print("error:",resImg.status_code,resImg.text)
        
        jObj=res.json()
        word=jObj[0]["word"]
        if 'phonetic' in jObj[0]:
            phonetic=jObj[0]["phonetic"]
            if 'audio' in jObj[0]["phonetics"]:
                mp3=jObj[0]["phonetics"][1]["audio"]
            else:
                mp3=None
        else:
            phonetic=None
        defN=jObj[0]["meanings"][0]["definitions"][0]["definition"]
        
        syN=jObj[0]["meanings"][0]["synonyms"]
        defV=jObj[0]["meanings"][1]["definitions"][0]["definition"]
        syV=jObj[0]["meanings"][1]["synonyms"]
        if len(syN)==[]:
            lenN=0
        else:
            lenN=len(syN)
        if len(syV)==[]:
            lenV=0
        else:
            lenV=len(syV)
        return render_template(
            'chatting.html',
            data=word,
            phonetic=phonetic,
            defN=defN,
            defV=defV,
            syN=syN,
            lenN=lenN,
            syV=syV,
            lenV=lenV,
            mp3=mp3,
            img=img
            )


app.run(port=8081,debug=True)