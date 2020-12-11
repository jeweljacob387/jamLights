from os import system


def playMp3File(filename):
    filename = "../audiofiles/" + filename+'.mp3'
    print('Playing file', filename)
    command = "omxplayer --no-keys " + filename + " &"
    print("running " + command)
    system(command)


def stopPlaying():
    killCmd = "killall omxplayer.bin"
    system(killCmd)
