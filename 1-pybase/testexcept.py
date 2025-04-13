
print("Test except")
list1 = []
try:
    print(list1[3])
except IndexError:
    print("IndexError")

try:
    print(list1[3])
except IndexError as e:
    print("IndexError", e)

try:
    print(list1[3])
except :
    print("未知异常")

try:
    print(list1[3])
except Exception as e:
    print("未知异常", e)
else:
    print("未抛出异常")
finally:
    print("任何情况都进入1")

try:
    pass
except:
    pass
else:
    print("未抛出异常")
finally:
    print("任何情况都进入2")

#自定义异常
class XError(Exception):
    def __init__(self, value= ""):
        self.value = value

    #用来print
    def __str__(self):
        return "XError :" + str(self.value)


try:
    raise XError("test error")
except XError as e:
    print(e)
