def modifiedBinarySearch(array):
    l,r=0,len(array)-1
    while(l<=r):
        mid=(l+r)//2
        if array[mid]>array[mid-1] and array[mid]>array[mid+1]:
            return f'The maximum number is {array[mid]}'
        elif array[mid-1]>array[mid]:
            r=mid-1
        elif array[mid+1]>array[mid]:
            l=mid+1
        else:
            l=mid+1

print(modifiedBinarySearch([1, 3, 4, 5, 9, 6, 2, -1]))
print(modifiedBinarySearch([1, 3, 4, 5, 4, 3, 2, -1]))
print(modifiedBinarySearch([1, 3, 6, 4, 3, 2, -1]))
print(modifiedBinarySearch([1, 3, 4, 5, 9, 10, 2, -1]))
print(modifiedBinarySearch([1, 3, 4, 5, 9, 10, 11, -1]))