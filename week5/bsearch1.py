def bsearch1(arr, key):
    low, high = 0, len(arr)
    while high - low > 0:
        #print(low, high)
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1  # + 1  # take the right side, mid is not included
        else:
            high = mid
    return None

print(bsearch1([0,1,2,3], 0))
