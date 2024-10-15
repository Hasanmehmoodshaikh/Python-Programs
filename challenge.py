def reverse_array(arr):
    left = 0
    right = len(arr) - 1
    while left<right:
        arr[left],arr[right] = arr[right],arr[left]
        left += 1
        right -= 1
    return arr    
N = int(input("Enter number of elements (1-1000) - "))
arr =[]
for i in range(N):
    num = int(input(f"Enter element {i+1} - "))
    arr.append(num)
print("Original Array-",arr)
reversed_arr = reverse_array(arr)
print("Reversed Array-",reversed_arr)           