import os
import sys
from common import bean, run


base_dir = 'out'


def start():
    # 如果没有参数
    if len(sys.argv) == 1:
        print('error: no param')
    else:
        args = bean.Arg(sys.argv)
        if args.exist('h') or args.exist('help'):
            print('''
    介绍：
        该程序可以将视频转化为字符动画并播放
    
    基本命令：
    python main.py <视频文件地址或URL> <可选参数>
                            1                        
    参数列表：
    -h 或 --help             帮助文档\n
    --rebuild 或 -r          重新制作字符动画
    --out=<目录>             指定保存目录
    --fps=<数字>             指定字符动画刷新率fps，默认为15
    --clear=n/no/false       不使用清屏方式，默认使用清屏
    --python=<文件>          指定python环境(不推荐)
            ''')
        else:
            project_path = args.get('out')
            if project_path is None:
                project_path = os.getcwd()
            target_path = os.path.join(project_path, base_dir)

            python_command = args.get('python')
            if not (python_command is None):
                bean.CommandBuilder.python_command = python_command
            run.run(target_path, args)


if __name__ == '__main__':
    start()
