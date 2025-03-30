print("Test Closure")
def outfun(a):
    print("outfun ",a)
    def infun(b):
        #a 外部函数变量
        nonlocal a
        a += 1
        return a+b
    return infun

fun = outfun(1)
print(type(fun))
print(fun(3))
