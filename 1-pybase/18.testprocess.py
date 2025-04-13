print("Test Process")
# 导入进程模块
from multiprocessing import Process
import time, os


# 创建进程 进程入口函数 进程参数(元组)
def proc_fun(name):
    for i in range(10):
        #打印进程号
        print(i ,"child fun ", name,os.getpid())
        time.sleep(1)


# 进程在主模块创建
if __name__ == "__main__":
    proc1 = Process(target=proc_fun,args=("name001",))
    #启动进程
    proc1.start()
    for i in range(10):
        print(i, "Parent process ", os.getpid())
        time.sleep(1)

