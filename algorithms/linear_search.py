#Linear search algorithm
#LinearSearch(array, key)
#    for each element in the array
#        if element == value
#            return it's index

#Python program for Linear Search
def LinearSearch(array, n, k):
    for j in range(0, n): 
        if (array[j] == k):
            return j
    return -1        

array = [1,3,5,7,9]
k= 9
n = len(array)
result = LinearSearch(array, n , k)
if (result==-1):
    print("Element not found")
else:
    print("Element found at index: ", result)        

#Time Complexity of Linear Search
#The running time complexity of the linear search algorithm is O(n) for N number of elements in the list as the algorithm has to travel through each and every element to find the desired element.

#Applications of Linear Search
#Used to find the desired element from the collection of data when the dataset is small
#The searching operations is less than 100 items