arr = [1,3,4,10,9,11,-9,0,-100]
i = 0
while i < len(arr) - 1:
    m = i
    j = i + 1
    while j < len(arr):
        if arr[j] < arr[m]:
            m = j
        j += 1
    t = arr[i]
    arr[i] = arr[m]
    arr[m] = t
    i += 1

print(arr)