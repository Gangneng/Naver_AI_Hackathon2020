import json
import os
from pydub import AudioSegment

jsondir = os.path.abspath("./json")
fname = os.listdir(jsondir)
fdir=list()
for i in range(len(fname)):
    fdir.append(os.path.join(jsondir,fname[i]))
data=list()
for i in fdir:
    with open(i, 'r') as f:
        data.append(json.load(f))

#json_data['predictions'][0]['0'] --> dict key = score, x, y

#key predictions
#list
#key '0' '1' ... '17' 해당 신체 부위 key
#key 'score' 'x' 'y'
#float score, x, y에 해당하는 값

x_diff=list()
y_diff=list()

for i in range(len(data)-1):
    try:
        x_diff.append(data[i+1]['predictions'][0]['4']['x']-data[i]['predictions'][0]['4']['x'])
        y_diff.append(data[i+1]['predictions'][0]['4']['y']-data[i]['predictions'][0]['4']['y'])
    except KeyError:
        x_diff.append(0)
        y_diff.append(0)

musicdir = os.path.abspath("./music")
music_name=os.listdir(musicdir)
mdir = list()
for i in range(len(music_name)):
    mdir.append(os.path.join(musicdir, music_name[i]))

sound=list()

for i in mdir:
    sound.append(Audio.Segment.from_file(i))





    
