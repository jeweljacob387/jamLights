from player import playMp3File, stopPlaying
from time import sleep
from frames import frames, loadFrames
from i2cMaster import setFrame

sourceFiles = ['audio1']

for file in sourceFiles:
    loadFrames(file)
    playMp3File(file)

for frame in frames:
    setFrame(frame)


stopPlaying()
