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

#私有成员变量无法访问
#print(video.__name)
print("video.get_name() = ", video.get_name())

print("=====================================")
# 类继承
class Mp4Video(Video):
    def __init__(self, path): # 不会主动调用父类构造函数，需要显示调用
        Video.__init__(self, path)
        print("Create Mp4Video")

    def __del__(self):
        print("Delete Mp4Video")

mp4 = Mp4Video("e:/test.mp4")
print("mp4.get_name()", mp4.get_name())

class AviVideo(Video):
    pass

print(isinstance(mp4, Mp4Video))
print(isinstance(mp4, Video))
print(isinstance(mp4, AviVideo))
