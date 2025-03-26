print("Test function return")

#return 默认返回None return 和 return None 一样
def fun1():
    print("fun1")

re = fun1()
print(re)

def fun2():
    print("fun2")
    return
    #return None

re = fun2()
print(re)

def fun3():
    list1 = [1,2,3,4]
    return list1 #返回时会将引用计数+1

v1 = fun3()
print(v1)

# 返回多个值
def fun4():
    return 5,"test",[7,8,9]

#分开变量接收,自动对应类型
i,s,l = fun4()
print("i = ", i)
print("s = ", s)
print("l = ", l)

#如果只用一个变量接收,该变量为元祖
t = fun4()
print("a = ",t)
print("type(t) = ",type(t))
