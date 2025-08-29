def binarySearch(numArr, target):
    l, r = 0,len(numArr) 

    while l <= r:
        m = (l+r)//2

        if numArr[m] > target:
            r = m - 1
        elif numArr[m] < target:
            l = m + 1
        else:
            return m
    else:
        return -1
Sarr = [1,5,2,23,1,5,521,321,-1,52,3,5,5,677,78,1,5,2,6,6]
Sarr.sort()
print(binarySearch(Sarr,5))
