# 基本数据类型
# Number python3 int float bool complex
# int


'''
PyLongObject
struct _longobject{
    PyObject_VAR_HEAD
    digit ob_digit[1] //unsigned short
}
'''

num = 1
print(num)
# 获取变量类型
print(type(num))
# 获取变量地址
print(id(num))


# float
# PyFloatObject
#  typedef stuct{
#    PyObject_HEAD
#    double ob_fval;
#  }PyFloatObject
#
num = 1.0
print(num)
print(type(num))
print(id(num))

# bool 内部存储直接用的整形
# _longobject False=0 True=1
# 结构体对象
# struct _longobject _Py_FalseStruct = {
#   PyVarObject_HEAD_INIT(&PyBool_Type,0)
#   {0}
# }
# struct _longobject _Py_TrueStruct = {
#   PyVarObject_HEAD_INIT(&PyBool_Type,1)
#   {1}
# }

num = True
print("bool num True = ", int(num))
num = False
print("bool num False = ", int(num))
print(num)
print(type(num))
print(id(num))
