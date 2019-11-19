import _thread
from playsound import playsound
import time

def print_image(num, time, base_dir):
    textVideo = []
    text = ""
    sleepTime = time / num
    for path in range(num):
        full_path = base_dir + str(path) + '.txt'
        with open(full_path, "r") as file:
            text = file.read()
        textVideo.append(text)

    _thread.start_new_thread(print_run, (num, textVideo, sleepTime))


def print_run(num, textVideo, sleepTime):
    for i in range(num):
        print(textVideo[i], end="")
        time.sleep(sleepTime)

def play(filename):
    playsound(filename)
