print("Test Scope")
# G全局作用域
gx = 1001
# L->E->G->B

"""
Local(函数内部)局部作用域
Enclosing（嵌套函数的外层函数内部）嵌套作用域（闭包）
Global（模块全局）全局作用域
Built-in（内建）内建作用域
L->E-> G->B 寻找优先级
处理关键字: global 和 nonlocal关键字
"""

def fun(a, b):
    global gx #使用全局变量
    gx += 1000
    print(gx)
    # L 局部作用域
    c = 1002
    print(a, b, c)

    def infun():
        # G内嵌作用域
        nonlocal c # 闭包函数访问外部函数的变量
        print(c)
        e = 1003
        print(e)
    return infun

f = fun(1, 2)
f()
