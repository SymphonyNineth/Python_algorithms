l = [1,2,3,4,5,6]
def invert_array(arr:list):
    length = len(arr)
    for k in range(length // 2):
        arr[k], arr[length - 1 - k] = arr[length - 1 - k],  arr[k]

invert_array(l)
print(l)