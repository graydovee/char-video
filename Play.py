import playsound
from apscheduler.schedulers.background  import BackgroundScheduler
import os


class CharVideo:
    flash_count = 0

    def __init__(self, char_video, sound_file, duration_time, frame_interval=0.1):
        self.char_video = char_video
        self.duration_time = duration_time
        self.sound_file = sound_file
        self.frame_interval = frame_interval
        self.frame_number = len(char_video)

    def __play(self):
        self.flash_count += 1
        if self.flash_count * self.frame_interval < self.duration_time:
            os.system('cls')
            print(self.char_video[int(self.flash_count * self.frame_interval / self.duration_time * self.frame_number)])

    def run(self):
        scheduler = BackgroundScheduler()
        seconds = self.duration_time / self.frame_number

        print(seconds)
        scheduler.add_job(self.__play, 'interval', seconds=self.frame_interval)
        scheduler.start()

        playsound.playsound(self.sound_file)
