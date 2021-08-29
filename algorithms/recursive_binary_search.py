def recursive_binary_search(list, target):
    if len(list) == 0:
        return None
    else: 
        midpoint = len(list) // 2

        if list[midpoint] == target:
            return list[midpoint]
        else:
            if list[midpoint] < target:
               return recursive_binary_search(list[midpoint + 1:], target)
            if list[midpoint] > target:
               return recursive_binary_search(list[:midpoint], target)


l = [1,2,3,4,5,6]

print(recursive_binary_search(l, 4))