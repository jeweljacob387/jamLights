from player import playMp3File, stopPlaying
from time import sleep, time
from frames import frames, loadFrames
from i2cMaster import setFrame

startTime = 0
frameIndex = 0
frameDuration = 50 #in ms

sourceFiles = ['audio2']

try:
    for file in sourceFiles:
        loadFrames(file)
        playMp3File(file)

        startTime = time()
        frameIndex = 0
        sleep(1)
        while(1):
            currentTime = time()
            timePassed = round((currentTime - startTime) * 1000)
            if(timePassed >= frameDuration or frameIndex == 0):
                startTime = currentTime
                # print(frameIndex)
                setFrame(frames[frameIndex])
                frameIndex += 1
                if(frameIndex > len(frames) - 1):
                    break
finally:
    stopPlaying()
