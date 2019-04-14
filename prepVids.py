import os

dataset = './dataset/'
fight = dataset + 'fights'
nofight = dataset + 'nofights'

print('Length of Fight Dataset: ',len(os.listdir(fight)))
print('Length of No-Fight Dataset : ',len(os.listdir(fight)))

os.mkdir(fight+'-prep')
os.mkdir(nofight+'-prep')

for vid in os.listdir(fight):
    if(os.path.isdir(vid)):
        print('Directory Already exists i.e. Dataset Already Prepped')
        continue
    else:
        os.mkdir(fight+'-prep/'+vid[:-4])

print('Directories Created for Fight Data')

for vid in os.listdir(nofight):
    if(os.path.isdir(vid)):
        print('Directory Already exists i.e. Dataset Already Prepped')
        continue
    else:
        os.mkdir(nofight+'-prep/'+vid[:-4])

print('Directories Created for No-Fight Data')

print('Beginning Frame Extraction !!!')
print('Initializing Sequence for Fight Data!!')

for vid in os.listdir(fight):
    loc = fight+'-prep/'+vid[:-4]+'/'
    video = fight+'/' + vid
    os.system(f'ffmpeg -i {video} -vf fps=5 {loc}frame%04d.jpg -hide_banner')

for vid in os.listdir(nofight):
    loc = nofight+'-prep/'+vid[:-4]+'/'
    video = nofight+'/' + vid
    os.system(f'ffmpeg -i {video} -vf fps=5 {loc}frame%04d.jpg -hide_banner')