def bsearch2(arr, key, left=0, right=None):
    print(left,right)
    if right is None:
        right = len(arr)
    if right < left:
        return None
    middle = (left + right) >> 1
    if arr[middle] > key:
        return bsearch2(arr, key, left, middle)
    if arr[middle] < key:
        return bsearch2(arr, key, middle + 1, right)
    return middle

print(bsearch2([-5,10], 1))
