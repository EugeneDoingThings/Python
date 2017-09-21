a = int(input('a:'))
b = int(input('b:'))
for i in range(a,b+1):
    if (i % 5) == 0:
        print(i)
    else:
        continue
