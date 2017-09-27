#start_array = [1,3,4,10,9,11,-9,0,-100]
arr = [1,3,4,10,9,11,-9,0,-100]
i = 1
while i<len(arr):
    for j in range(len(arr)-i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
    i += 1
print(arr)
