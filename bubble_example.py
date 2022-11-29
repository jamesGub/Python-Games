def bubbleSort(arr):
     
    n = len(arr)
 
    # For loop to traverse through all
    # element in an array
    for i in range(n):
        for j in range(0, n - i - 1):
             
            # Range of the array is from 0 to n-i-1
            # Swap the elements if the element found
            #is greater than the adjacent element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                 
# Driver code
 
# Example to test the above code
arr = [ 4, 3, 20, 35, 64, 103, 88, 14, 430, 48, 1, 5, 34, 82, 26, 28, 800 ]
 
bubbleSort(arr)
 
