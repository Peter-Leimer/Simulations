def bubbleSort(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
 
# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]
arr2 = []
arr3 = [94, 56, 81] 

bubbleSort(arr)
bubbleSort(arr2)
bubbleSort(arr3)


print ("Sorted array  1 is:")
print (arr)
print ("Sorted array 2 is:")
print (arr2)
print ("Sorted array 3 is:")
print (arr3)
#for i in range(len(arr)):
 #   print ("%d" %arr[i]), 
