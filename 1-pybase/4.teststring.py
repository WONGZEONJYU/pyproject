print("Test String")
str1 = "测试字符串001"
print(str1)
print(type(str1))
print(id(str1))

str1 = "0123456789"
print(id(str1))
print(str1[2])
print(str1[4])
print("str1[3:6] = ",str1[3:6]) #范围[3,6) ,也可以理解为[3,5]
print("str1[-3:-1] = ",str1[-3:-1]) #负数从结尾开始,范围[-3,-1)
print("str1[:-2] = ",str1[:-2]) #去掉最后字符,不指定开始位置
str1 = "file.mp4"
print("str1[-3:] = ",str1[-3:]) #不指定结束位置
