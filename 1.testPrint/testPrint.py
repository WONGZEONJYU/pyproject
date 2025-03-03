import sys
print("hello world",flush=True)
print("Test Print!",end='\t')
print("No warp")
print("String 1","String 2",1000,sep=",")
#标准输出和错误输出
print("Error out",file=sys.stderr)

#print 输出到文件
log = open("log.txt","a") #a表示追加写入
# noinspection PyTypeChecker
print("Log to File" , file=log)
log.close()

csv = open("python.csv","a")
# noinspection PyTypeChecker
print("名称","数量","内容",sep=",",file=csv)
# noinspection PyTypeChecker
print("name1","1","1111",sep=",",file=csv)
# noinspection PyTypeChecker
print("name2","2","2222",sep=",",file=csv)
# noinspection PyTypeChecker
print("name3","3","3333",sep=",",file=csv)
csv.close()

#一行注释

"""
多行注释1
多行注释2
多行注释3
"""
#多行语句写法
print("test 1");print("test 2");print("test 3")
#换行不结束1
print("long string。。。。。。。。。。。。。。。。。。"
    "。。。。。。。。。。。。。。。")
#换行不结束2
print("long string===============\
=============================")



