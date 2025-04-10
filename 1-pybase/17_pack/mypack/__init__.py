print("mypack imported")
#import * 时载入模块
__all__ = ["audio", "video", "opengl"]

def init():
    print("mypack init function")