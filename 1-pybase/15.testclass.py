import gc

print("Test class")

class Video(object):

    # 私有成员变量 __开头
    __name = "private name"

    # 声明成员变量
    age = 20

    path = ""

    # 构造函数
    def __init__(self, path):
        print("Create Video")
        self.name = "public name"
        self.path = path
        print("path is ",path)

    def __del__(self):
        print("Delete Video")

    def get_name(self):
        return self.__name


# <class '__main__.Video'>  __main__ 模块名称
video = Video("d:/video.mp4")


print(Video)
print(video)
print(dir(video))
print("end")
# 通过对象生成成员变量
video.title = "test"

print("title = ", video.title)

# 通过 self生成成员变量
print("video.name = ", video.name)

# 通过 直接声明的成员变量
print("video.age = ", video.age)

#私有成员变量无法通过对象实例直接访问
#print(video.__name)
print("video.get_name() = ", video.get_name())
#私有成员变量可以通过 实例._类名__变量名 去访问
#例如: video._Video__name
print("video.__name = ", video._Video__name)

#__m1成员属性虽然名称前缀带__,但是它由于是动态创建,所以它并非为私有属性,私有属性只能在类内通过__前缀定义
#就算是类内通过__前缀定义的属性属于私有属性,它只是一种约定规则,并非是安全机制
video.__m1 = "m1"
print("video.__m1 = ",video.__m1)

print("=====================================")
# 类继承
class Mp4Video(Video):
    def __init__(self, path): # 不会主动调用父类构造函数,需要显式调用
        Video.__init__(self, path)
        print("Create Mp4Video")

    def __del__(self):
        print("Delete Mp4Video")

mp4 = Mp4Video("e:/test.mp4")

print("mp4.get_name()", mp4.get_name())

class AviVideo(Video):
    pass

#原型isinstance(object, classinfo)
#如果参数object是classinfo的实例,或者object是classinfo类的子类的一个实例,返回True,如果object不是一个给定类型的的对象,则返回结果总是False。
print(isinstance(mp4, Mp4Video))
print(isinstance(mp4, Video))
print(isinstance(mp4, AviVideo))
