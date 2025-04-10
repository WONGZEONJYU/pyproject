print("Test Pack")

# 导入包的初始化
import mypack
mypack.init()

import mypack.video
mypack.video.view()

#引入了包mypack的命名空间
from mypack import audio
audio.play()

#引入包和模块的命名空间
from mypack.audio import play
play()

#不导入包的全部模块 要定义__all__
from mypack import *
mypack.opengl.draw()

#导入子包
import mypack.sub.pydir
mypack.sub.pydir.pydir()

#这种导入函数容易产生同名覆盖问题
from mypack.sub.pydir import *
pydir()

# 包=》模块=》函数、类、变量
