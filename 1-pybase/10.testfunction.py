print("Test Function")
# 函数参数

def fun1():
    print("fun1")

fun1()
# a 1必选参数 b 2默认参数
def fun2(a,b = 2):
    print(a,b)
fun2(8,9)
fun2(5)
#fun2()

# 3可变参数 传递的元组 tuple
def fun3(fmt,*values):
    print(fmt)
    print("values type is",type(values))
    print(values)
    for v in values:
        print("v = ", v)

fun3("%d,%d", 1, 2)

# 4关键字参数
def fun4(a, **kw):
    print("a = ", a)
    print("kw type is ",type(kw))

    if "name" in kw:
        print(kw["name"])

    if "age" in kw:
        print(kw["age"])

fun4(1001)
fun4(100,name="xiaoming")
