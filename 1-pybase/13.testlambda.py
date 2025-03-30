print("Test Lambada")

# 不符合 PEP8编码规则 有命名的函数不要用lambda
fun = lambda x, y: x*y
print("type(fun) = ",type(fun))
print("lambda fun = ", fun(3, 5) )

def testfun():
    return lambda x,y:x+y

f = testfun()
print("type(f) = ",type(f))
print(f(1,2))
