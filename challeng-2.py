def find_max_min(arr):
    max_element = min_element = arr[0]
    for num in arr:
        if num > max_element:
            max_element = num
        elif num < min_element:
            min_element = num
        
    return max_element,min_element
arr = [12,3,45,7,89,2]
print("First arr -",arr)        

max_element,min_element = find_max_min(arr)

print("Maximum element -",max_element)
print("Minimum element -",min_element)        