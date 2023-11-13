from flask import *
import requests
import json
import shutil
import os
from werkzeug.exceptions import HTTPException
import pastWords
#make this py file and give apikey and engine key
import config



app=Flask(__name__,template_folder="templates")
q=pastWords.Qclass(5)


@app.route("/word",methods=['GET','POST'])
def chat():
    if request.method=='GET':
        return render_template('word.html')
    elif request.form["para"]=="":
        return render_template('word.html',data="")
    else:
        url="https://api.dictionaryapi.dev/api/v2/entries/en/"+request.form["para"]
        res=requests.get(url=url)
        image="https://www.googleapis.com/customsearch/v1?q="+request.form["para"]+"&cx="+config.apiEngine+"&searchType=image&key="+config.apiKey

        resImg=requests.get(url=image)

        imgJson=resImg.json()
        if resImg.status_code == requests.codes.ok:
           img=imgJson["items"][0]["link"]
           print("=========="+img+"=============")
        else:
            print("error:",resImg.status_code,resImg.text)
        

        jObj=res.json()
        word=jObj[0]["word"]
        q.put(word)
        
        mp3=""
        if 'phonetics' in jObj[0]:
            #print(len(jObj[0]["phonetic"]))
            for val in jObj[0]["phonetics"]:
                print(val["audio"])
                if val["audio"]!="":
                    mp3=val["audio"]
                    break
            phonetic=jObj[0]["phonetic"]
            # mp3=jObj[0]["phonetics"][0]["audio"]
            # if jObj[0]["phonetics"][0]["audio"]=="":
            #     mp3=jObj[0]["phonetics"][2]["audio"]
        else:
            phonetic=None
        defN=syN=defV=syV=None
        if 'meanings' in jObj[0]:
            defN=jObj[0]["meanings"][0]["definitions"][0]["definition"]
            print(defN)        
            syN=jObj[0]["meanings"][0]["synonyms"]
            defV=jObj[0]["meanings"][1]["definitions"][0]["definition"]
            syV=jObj[0]["meanings"][1]["synonyms"]
        if len(syN)==None:
            lenN=0
        else:
            lenN=len(syN)
        if len(syV)==None:
            lenV=0
        else:
            lenV=len(syV)
        return render_template(
            'word.html',
            past=q.get(),
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


@app.route("/")
def reHome():
    return redirect("/word")


app.run(port=8081,debug=True)
