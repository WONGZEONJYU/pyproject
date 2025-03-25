print("Test For")
# for 循环语句
list1 = [1,2,3,4,5,6]
for i in list1:
    print(i, end=" ")
else:
    print("end i = ", i)

for i in range(10,1000,10):
    if 0 == i % 20:
        continue
    if i > 200:
        break
    print(i, end=",")
