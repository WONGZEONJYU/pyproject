str4 = "str004"
i1 = 5
list1 = ["str001", "str002", "str003", str4, i1]
print("list1 = ",list1)
print("type(list1) = ",type(list1))
print("id(list1) = ",id(list1))
print("len(list1) = ",len(list1))

list1[0] = 1001
print(list1)
list1.insert(1, "xcj") #插入数据 O(n)
print(list1)
list1.append("dst") #O(1)
print(list1)

list1.pop(-1) #清理最后一个元素
print(list1)
list1.pop(2) #清理最后一个元素
print(list1)

print("====================================================================================")

list2 = ["str01", "str02", [1,2,3] ]
print("list2 = ",list2)
print("list1[2] = ",list1[2])
print("type(list1[2]) = ",type(list1[2]))
print("list2[2][2] = ",list2[2][2])
print("list2[-2] = ",list2[-2]) #负数从最后开始往前
