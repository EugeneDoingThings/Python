arr = [1,3,4,10,9,11,-9,0,-100]
for i in range(len(arr)):
    v = arr[i]
    j = i
    while (arr[j-1] > v) and (j > 0):
        arr[j] = arr[j-1]
        j = j - 1
    arr[j] = v
print(arr)