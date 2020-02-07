import cv2
import os
import sys
import requests
import json

count=0

dir = os.path.abspath("./mvimages")
fname = os.listdir(dir)
fdir=list()
for i in fname:
    fdir.append(os.path.join(dir, i))


client_id = "68lu4vh157"
client_secret = "wxrDd1kSPAmq5P14HLV7XNmddjCassOqIivC6QsL"
url = "https://naveropenapi.apigw.ntruss.com/vision-pose/v1/estimate" # 사람 인식


for i in fdir:
    files = {'image': open(i, 'rb')}
    headers = {'X-NCP-APIGW-API-KEY-ID': client_id, 'X-NCP-APIGW-API-KEY': client_secret }
    response = requests.post(url,  files=files, headers=headers)
    rescode = response.status_code
    if(rescode==200):
        strTodict = json.loads(response.text)
        with open("./json/test%d.json" % count,'w', encoding='utf-8') as make_file:
            json.dump(strTodict , make_file, indent="\t")
        print(count+1, "개 완료")
        count+=1
    else:
        print("Error Code:" + rescode)
