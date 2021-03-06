from common import bean
import moviepy.editor as mp
import cv2, playsound
import sys, os, time, hashlib, re


max_height_size = 30
max_width_size = 90


# 下载视频
def down(url, output_dir, video_name='', command=None):
    # 创建url-文件名对应的视频文件
    if video_name == '':
        video_name = generate_filename_prefix(url)

    # 使用you-get下载
    you_get_path = os.path.join(os.getcwd(), 'dependency', 'you-get', 'you-get')

    if command is None:
        pattern = 'python[3]?(.exe)?$'
        if not (re.match(pattern, sys.executable) is None):
            command = sys.executable
        else:
            command = 'python'
    cmd = bean.CommandBuilder(command)
    cmd.add_arg(you_get_path)
    cmd.add_args('-o', output_dir).add_args('-O', video_name).add_arg(url)
    cmd.execute()

    # 删除多余文件
    for file in os.listdir(output_dir):
        full_path = os.path.join(output_dir, file)
        if os.path.isfile(full_path):
            if file.endswith('.xml'):
                os.remove(full_path)
            elif file.startswith(video_name):
                video_name = file
    return video_name


# 根据URL生成文件前缀
def generate_filename_prefix(url):
    return hashlib.md5(url.encode(encoding='UTF-8')).hexdigest()


def save_audio(video_full_path, audio_full_path):
    clip = mp.VideoFileClip(video_full_path)
    clip.audio.write_audiofile(audio_full_path, logger=None)


def get_duration_time(video_path):
    clip = mp.VideoFileClip(video_path)
    return clip.duration


def make_char_video(video_full_path):
    video = cv2.VideoCapture(video_full_path)
    if not video.isOpened():
        print("error: open video failed!")
        return 0

    asc = '@&%#*+=-. '
    asc_num = len(asc) - 1
    frames = []
    frame_count = 0
    resize_scale = 1
    is_resize = False
    while video.isOpened():
        # 提取每一帧
        ret_val, image = video.read()
        if ret_val:
            print('\r\t正在处理第{}帧'.format(str(frame_count)), end='', flush=True)
            frame_count += 1

            # 图片转化为灰度，并缩放
            gray_img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
            x, y = gray_img.shape[0:2]

            if not is_resize:
                if y*2 > x:
                    resize_scale = max_width_size / (y * 2)
                else:
                    resize_scale = max_height_size / x
                is_resize = True

            if resize_scale != 1:
                x = int(x * resize_scale)
                y = int(y * resize_scale * 2)
                gray_img = cv2.resize(gray_img, (y, x))

            # 转化为字符画面
            text = ''
            for row in range(x):
                for col in range(y):
                    gray = gray_img[row, col]
                    text += asc[int((255 - gray) / 255 * asc_num)]
                text += '\n'
            frames.append(text)

            cv2.waitKey(1)
        else:
            print('\n')
            break
    return frames


def play_char_video(char_video, sound_file, duration_time, fps=15, cls=True):
    frame_number = len(char_video)
    playsound.playsound(sound_file, block=False)
    start_time = time.time()
    while time.time() - start_time < duration_time:
        running_time = time.time() - start_time
        if running_time < duration_time:
            if cls:
                os.system('cls')
            print(char_video[int(running_time / duration_time * frame_number)])
        time.sleep(1 / fps)

    if cls:
        os.system('cls')
    print("播放结束")
