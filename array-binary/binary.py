

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
 
   
    return -1
 
 

# arr = [ 2, 3, 4, 10, 40 ]
# x = 10
 
final= binary_search([4, 8, 15, 16, 23, 42], 15)

if final != -1:
    print("Element is present at index", str(final))
else:
    print("Element is not present in array")









