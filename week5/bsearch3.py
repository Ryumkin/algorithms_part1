def bsearch3(arr, key):
    n = len(arr)
    if n < 2:
        return 0 if (n == 1 and arr[0] == key) else None
    m = int(0.5 * n)
    if arr[m] == key:
         return m
    if arr[m] > key:
        return bsearch3(arr[:m], key)
    result = bsearch3(arr[m:], key)
    return result + m if result is not None else None

def verify(arr):
    print(bsearch3(arr, 2))
    return


arr = [0,1,2,3,4]

verify(arr)
