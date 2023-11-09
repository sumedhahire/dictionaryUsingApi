import json
import requests

url="https://api.dictionaryapi.dev/api/v2/entries/en/word"
res=requests.get(url=url)

jobj=res.json()
print(len(jobj[0]["phonetic"]))
flag=0
for val in jobj[0]["phonetics"]:
    print(val["audio"])
    if val["audio"]!="":
        flag=1
        print(jobj[0]["phonetic"][val])
        break
print(flag)
