def circular_shift_left(arr:list):
    length = len(arr)
    if(length < 2):
        return arr
    first = arr[0]
    for i in range(length - 1):
        arr[i] = arr[i + 1]
    arr[length - 1] = first
