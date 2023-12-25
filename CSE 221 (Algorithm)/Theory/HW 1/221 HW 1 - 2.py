def binarySearch(array,item):
    l,r,storedIndexOfItem=0,len(array)-1,(len(array)+1)      #storedIndexOfItem is taken a large number to handle the first appearance
    while(l<=r):
        mid=(l+r)//2
        if array[mid]==item:
            if storedIndexOfItem>mid:         #Changed the code to find the least index appearance of item
                storedIndexOfItem=mid
                r=mid-1
            else:
                l=mid+1
        else:
            if item<array[mid]:
                r=mid-1
            else:
                l=mid+1

    if storedIndexOfItem==0:
        return f'Not Found'
    else:
        return f'The item {item} was found in {storedIndexOfItem}th position at first.'
    
print(binarySearch([1,3,5,7,9,9,13,13,13],13))
print(binarySearch([1,3,5,7,9,9,13,13,13],9))