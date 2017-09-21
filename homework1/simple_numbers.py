a = input('a:')
lst = []
for i in range(2, a+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        lst.append(i)
print lst
