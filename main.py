from Video import Video
import Play
import Trans
import Out
import os
import sys
import pickle

video_path = ""
save_dir = "pic/"
op_path = 'out/'
save_file = video_path[:video_path.rfind("/") + 1] + "audio.mp3"


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("error: no param")
    else:
        name = sys.argv[1]
        name.replace("\\","/")
        if(name == 'run'):
            with open("run", "rb") as file:
                arg = pickle.load(file)
                Play.print_image(arg[0], arg[1], arg[2])
                Play.play(save_file)
        else:
            print("running...")
            video_path = video_path + name

            v = Video(video_path)
            c = v.savePic(save_dir)
            print("success: " + str(c) + " images is saved!")
            time = v.saveAudio(save_file)
            print (time)

            now = 0
            for path in range(c):
                now = now + 1
                full_path = save_dir + str(path) + '.jpg'

                text = Trans.createText(full_path, 0.03)

                txt_path = op_path + str(path) + ".txt"
                Out.out(txt_path, text)

                print("\r transToText: " + txt_path.rjust(20) + "-----" + str(round(now * 100 / c, 2)), end="%")

            print("\nfinished!")

            arg = [c, time, op_path]
            with open("run", "wb") as file:
                pickle.dump(arg, file)

            Play.print_image(c, time, op_path)
            Play.play(save_file)
