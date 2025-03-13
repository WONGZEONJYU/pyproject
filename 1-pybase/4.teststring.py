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

#字符串转义
print("AAAAAAAAA\n\\\"BBBBBBBBB")
print("'CCCCCCCCCCCCCCCCCCCCCCCCC'")
print('"CCCCCCCCCCCCCCCCCCCCCCCCC"')

#r或R 转义成为普通字符串
print(r"DDD\tDDDD\n\\\"EEEE\tEEEE")

#多行字符串
a = "11111111111111" \
    "2222222222222"  \
    "3333333333333"
print(a)
a = "11111111111111 \
    2222222222222  \
    3333333333333"
print(a)
a = """
    aaaaaaaaaaaaaaa
    bbbbbbbbbbbbbbb
    ccccccccccccccc
"""
print(a)

#字符串的拼接和格式化
#运行时进行拼接
s1 = "1234567890一二三四五"
s2 = "YYYYYYYYYYYYYYYY"
s3 = s1 + s2 + " " + str(123)+ " " + str(100.9)
print(s3)
# %s 字符串 %d 整数 %c 字符 %f浮点数
s4 = "格式化字符串 %s %d %c %c %c %f  size is %d" % ("teststring", 300, s1[0], 65, chr(66), 10.9, len(s1))
print(s4)
