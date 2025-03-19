tup1 = ("str1", "str2" ,3,[1,2,3])
#元组指向不可以修改
try:
    tup1[0] = "str001"
except TypeError:
    print("元组指向不可以修改")

#元祖指向的值可以更改
tup1[3][0] = 100

print(tup1)
