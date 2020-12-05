from playsound import playsound


def playMp3File(filename):
    filename = "../audiofiles/" + filename
    print('Playing file', filename)
    playsound(filename, False)
