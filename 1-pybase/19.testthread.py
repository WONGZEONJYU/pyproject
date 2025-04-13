
print("Test Thread")
from threading import Thread
from threading import Lock
import time
from queue import Queue

# == False时退出所有线程
is_runing = True

# 互斥锁
mux = Lock()

# 产品队列
products = Queue()

# 生产者线程
class Producer(Thread):
    def __init__(self):
        Thread.__init__(self)
        print("Producer Created!")

    #线程入口函数
    def run(self):
        print("In Producer Thread")
        product_id = 1000
        while is_runing:
            product_id += 1
            #获取锁
            mux.acquire()
            print("produce a product", product_id)
            # 产品放入队列
            products.put(product_id)
            mux.release()

            time.sleep(1)
        print("Producer thread exited")


#消费者线程
class Consumer(Thread):
    def __init__(self):
        Thread.__init__(self)
        print("Consumer Created!")

    #线程入口函数
    def run(self):
        print("In Consumer Thread")
        #product_id = 1000
        while is_runing:
            #product_id += 1
            # 获取锁
            mux.acquire()
            if products.empty():
                mux.release() #不释放死锁
                continue

            print("consumed a product", products.get())
            mux.release()
            time.sleep(1)
        print("Consumer thread exited")

producer = Producer()
consumer = Consumer()
producer.start()
consumer.start()

ths = [producer, consumer]
time.sleep(5)
is_runing = False
time.sleep(5)
# 主线程等待所有子线程退出
for th in ths:
    th.join() #等待线程退出
print("main thread exit")

