print("Test Dictionary")
# {"key1":value1, "key2",value2 } key需要计算hash值 value可以装任意类型
# dictionary 初始化
dic = {"name": "Python",
       "year":1991,
       "ver":3.7,
       4:5,
       "keys":["print","for"]}
print(dic)
# 新增和更改
dic[4] = 6
dic["src"] = "C"
print(dic)
# 删除
del dic[4]
dic.pop("keys")
print(dic)


# 判断关键字
try:
    print(dic["name"])
    print(dic["arg"])
except KeyError:
    print("dic KeyError ")

if "year" in dic:
    print("key year in dic")

dic.clear()