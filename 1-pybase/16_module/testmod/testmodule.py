print("Test module")

# 导入模块 模块代码只会被执行一次
import mymod

#import mymod
mymod.modfun()
obj = mymod.MyMod()

#from 将模块中的函数和类引入当前命名空间
from mymod import modfun
modfun()

#导入模块中的所有内容
from mymod import *
MyMod()

# 系统模块
import sys
#print(sys.path)
# 模块的查找路径
sys.path.insert(0, "../exmod")
import exmod
exmod.exmod_fun()
