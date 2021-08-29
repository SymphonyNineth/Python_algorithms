def insertion_sort(arr):
    """Insertion sort"""
    length = len(arr)
    for top in range(1, length):
        k = top
        while k > 0 and arr[k - 1] > arr[k]:
            arr[k], arr[k - 1] = arr[k - 1], arr[k]
            k -= 1


def sort_testing(fn):
    print("Testing: ", fn.__doc__)
    l = [5, 2, 4, 1, 3]
    l2 = []
    l3 = [1]
    l4 = list(range(10, 20)) + list(range(0, 10))
    l4_sorted = list(range(20))


    l_sorted = [1, 2, 3, 4, 5]

    fn(l)
    print("OK - 1" if l == l_sorted else "Fail - 1")
    
    fn(l2)
    print("OK - 2" if l2 == [] else "Fail - 2")
    
    fn(l3)
    print("OK - 3" if l3 == [1] else "Fail - 3")
    
    fn(l4)
    print("OK - 4" if l4 == l4_sorted else "Fail - 4")


sort_testing(insertion_sort)