#Binary search algorithms are fast and effective in comparison to linear search
#algorithms. Binary search algorithm only works on sorted lists of elements.
#if the list is not sorted , then algorithm first sorts the elements using the
#sorting algorithm and then rruns the binary search algorithm.
#preferred for large size of data
#Algorithm for binary search(Iterative method)
#do until the pointers low and high are equal
# mid = (low + high)/2
# if (k==arr[mid])
#     return mid
# elif (k> arr[mid])
#     low = mid + 1
# else
#     high = mid - 1

# Algorithm for binary search(Recursive method)
# BInary search(array, k, low, high)
# if low>high
#     return False
# else 
#     mid = (low+high)/2
#     if k==array[mid]
#         return mid
#     elif k> array[mid]
#         return BinarySearch(array, k, mid+1, high)
#     else 
#         return BinarySearch(array, k, low, mid-1)

#Python Code for Binary search algorithm(Iterative method)
def binarySearch(arr, k, low, high):
    while low <= high:
        mid = low + (high-low)//2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            high = mid-1
        else:
            low = mid + 1
    return -1     

arr = [2,4,6,8,10]
k = 8
funcBinary = binarySearch(arr, k, 0,len(arr)-1 )
if funcBinary == -1:
    print("Object not found")
else:
    print('Index of the object is ', funcBinary)

#Python code for binarySearch algorithm(Recursive method)
def BinarySearch(array, n, lower, higher):
    while lower <= higher:
        mid = (lower + higher)//2
        if array[mid] == n:
            return mid
        elif array[mid] >= n:
            return BinarySearch(array, n, lower, mid-1)

        else:
            return BinarySearch(array, n, lower+1, higher)
    return -1

array = [1,3,5,9,11]
n = 3
algorithm1 = BinarySearch(array, n, 0, len(array)-1)
if algorithm1 == -1:
    print("Object not found!")
else:
    print("Index of object is ", algorithm1)    