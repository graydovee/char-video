# 视频转字符动画

## 使用方法：
* 命令行进入工程目录，输入以下命令即可运行
```sh
vtoc <视频文件地址或URL>
```
> 视频文件支持本地文件与网络视频，网络视频将使用you-get下载
* 若无法运行，执行install.bat重新打包exe文件：

## 参数
* 执行以下命令可查看详细参数
```sh
vtoc -h
```

* 参数列表：
```
    -h 或 --help             帮助文档\n
    --rebuild 或 -r          重新制作字符动画
    --out=<目录>             指定保存目录
    --fps=<数字>             指定字符动画刷新率fps，默认为15
    --clear=n/no/false       不使用清屏方式，默认使用清屏
    --python=<文件>          指定python环境(不推荐)
```


## 依赖组件

* [you-get(已经内置)](https://github.com/soimort/you-get)
* [opencv]( https://github.com/opencv/opencv )
* [playsound]( https://github.com/TaylorSMarks/playsound )
* [moviepy ]( https://github.com/Zulko/moviepy )

