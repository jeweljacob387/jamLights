from player import playMp3File
from time import sleep
from frames import frames
from i2cMaster import setFrame, setNodesList

setNodesList()
fileName = 'audio.mp3'
playMp3File(fileName)

for frame in frames:
    setFrame(frame)
