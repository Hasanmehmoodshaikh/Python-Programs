def find_max_min(list):
    max_element = min_element = list[0]
    for num in list:
        if num > max_element:
            max_element = num
        elif num < min_element:
            min_element = num
    return max_element,min_element
N = int(input("Enter number of elements(1-1000) - "))

list = []
for i in range(N):
    num = int(input(f"Enter element {i+1} - "))
    list.append(num)
print("First list -",list)
max_element,min_element = find_max_min(list) 
print("Maximum element -",max_element)
print("Minimum element -",min_element)    
            