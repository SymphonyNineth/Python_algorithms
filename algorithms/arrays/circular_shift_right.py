def circular_shift_right(arr:list):
    length = len(arr)
    if(length < 2):
        return arr
    last = arr[length - 1]
    for i in range(length - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = last

l = [1,2,3,4,5,6]

circular_shift_right(l)

print(l)