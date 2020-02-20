import sys 
A = [64, 25, 12, 22, 11] 
B = [65, 34, 88, 24, 82]
C = [69, 420, 89, 2, 45]

def selectionSort(arr):  
    # Traverse through all array elements 
    for i in range(len(A)): 
      
    # Find the minimum element in remaining  
    # unsorted array 
        min_idx = i 
        for j in range(i+1, len(A)): 
            if A[min_idx] > A[j]: 
                min_idx = j 
              
    # Swap the found minimum element with  
    # the first element         
        A[i], A[min_idx] = A[min_idx], A[i] 
  
# Driver code to test above 
print ("Sorted array A") 
print(A)

print ("Sorted array B") 
print(B)

print ("Sorted array C") 
print(C)


#for i in range(len(A)): 
 #   print("%d" %A[i]),
