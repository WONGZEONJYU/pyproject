print("Test While")
i = 0
while i < 10:
    print(i,end='\t')
    i += 1
else:
    print("else i = ",i)

# 无限循环
i = 0
while True:
    i += 1
    if i > 10:
        break #退出整个循环
    # 只显示偶数
    if i % 2 != 0:
        continue #退出本次循环
    print(i, end=" ")
