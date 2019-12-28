import os
from common import video, file_utils


def run(target_path, args):

    # 视频文件夹
    video_dir = 'video'
    video_path = os.path.join(target_path, video_dir)

    # 音频文件夹
    audio_dir = 'audio'
    audio_path = os.path.join(target_path, audio_dir)

    # 字符动画输出文件夹
    char_dir = 'character'
    char_path = os.path.join(target_path, char_dir)
    # 建好目录
    if not os.path.exists(video_path):
        os.makedirs(video_path)

    if not os.path.exists(audio_path):
        os.makedirs(audio_path)

    if not os.path.exists(char_path):
        os.makedirs(char_path)
    # 判断视频是否已经下载
    url = args.get('url')
    prefix = video.generate_filename_prefix(url)

    video_full_path = url
    if url.startswith('http'):
        video_name = file_utils.find_file(video_path, prefix)
        if video_name is None or video_name.endswith('download'):
            print('下载视频...')
            video_name = video.down(url, video_path, prefix, command=args.get('python'))
        else:
            print('视频已存在')
        video_full_path = os.path.join(video_path, video_name)

    # 提取视频音频
    audio_name = file_utils.find_file(audio_path, prefix)
    if audio_name is None:
        print('提取音频文件...')
        audio_name = prefix + '.mp3'
        video.save_audio(video_full_path, os.path.join(audio_path, audio_name))
    else:
        print('音频文件已存在')
    audio_full_path = os.path.join(audio_path, audio_name)

    # 计算视频时长
    duration_time = video.get_duration_time(video_full_path)

    # 字符动画
    char_path_this_video = os.path.join(char_path, prefix)
    char_video_info = None
    if not (args.exist('rebuild') or args.exist('r')):
        if os.path.exists(char_path_this_video) and os.path.isfile(char_path_this_video):
            char_video_info = file_utils.load(char_path_this_video)
            if char_video_info is None or not isinstance(char_video_info, list) or len(char_video_info) == 0:
                print('无法识别字符动画文件')
            else:
                print('读取字符动画文件完成！')
        else:
            print('未找到字符动画文件')

    if char_video_info is None:
        print('正在制作字符动画...')
        char_video_info = video.make_char_video(video_full_path)
        file_utils.save(char_video_info, char_path_this_video)

    # 播放
    print('一切就绪：准备播放！')

    fps = args.get('fps')
    if fps is None:
        fps = 15
    else:
        fps = int(fps)

    cls = args.get('clear')
    mod = True
    if not (cls is None):
        cls = cls.lower()
        if cls == 'n' or cls == 'no' or cls == 'false':
            mod = False
    video.play_char_video(char_video_info, audio_full_path, duration_time, fps=fps, cls=mod)
