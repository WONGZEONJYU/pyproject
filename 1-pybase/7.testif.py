print("Test If")
a = 10
b = 11
# 比较运算符  == != <> > < >= <=
if a == b:
    print("a==b")
elif 1 == 2:
    print("1==2")
else:
    print("else")
if a < b:
    print("a<b")
# 逻辑运算符 and    or     not 优先级最低
a = 10
b = 11
if a < b and a > 9:
   print("a < b and a > 9")
if a == 100 or a == 10:
    print("a == 100 or a == 10")
if not 1 == 2:
    print("not 1 == 2")

# 成员运算符 in not in
list1 = [1,2,3,4,5,6,7]
if 1 in list1:
    print("1 in list")
if 8 not in list1:
    print("8 not in list")
tup1 = (1,2,3)
if 2 in tup1:
    print("2 in tup1")

dic = {1:"001",2:"002"}
if 2 in dic: #模型查找key
    print("2 in dic")
if "002" in dic.values():
    print("002 in dic.values()")
if "003" in dic.values():
    print("003 in dic.values()")
else:
    print("003 not in dic.values()")

# 身份运算符  is        is not id(a)==id(b)
a = 100
b = 100
if a is b:
    print("a is b")
else:
    print( "a not b")
a = 10231230
b = 10231230
if a is b:
    print("a is b")
else:
    print("a not b")
c = 1
if a is not c:
    print("a is not c")
else:
    print("a is  c")

