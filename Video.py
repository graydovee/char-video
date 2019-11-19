import cv2
import os
import moviepy.editor as mp

class Video:
    def __init__(self, video_path):
        self.video_path = video_path
        

    def savePic(self, save_dir):
        video = cv2.VideoCapture(self.video_path)

        if not video.isOpened():
            print("error: open video failed!")

        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        c = 0
        while video.isOpened():
            rval, frame = video.read()
            if rval:
                pic_path = save_dir + str(c) + ".jpg"
                c += 1
                print("\r saving :" + pic_path, end = "")
                cv2.imwrite(pic_path, frame)
                cv2.waitKey(1)
            else:
                print("\nfinished!")
                break
        return c

    def saveAudio(self, save_file):
        print("Audio down start....")
        clip = mp.VideoFileClip(self.video_path)
        file_time = clip.duration
        cp2 = clip.subclip(0, 20)
        clip.audio.write_audiofile(save_file, logger=None)
        print("Audio down completed!")
        return file_time

