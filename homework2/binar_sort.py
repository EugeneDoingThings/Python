arr = [1,3,4,10,9,11,-9,0,-100]
x = 0
i = 1
j = len(arr)-1
m = int(j/2)
while arr[m] != x and i < j:
    if x > arr[m]:
        i = m+1
    else:
        j = m-1
    m = int((i+j)/2)
if i > j:
    print('Элемент не найден')
else:
    print('Индекс элемента: ', m)
