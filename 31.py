#write a python code to find a largest element in an array

def find_largest_element(arr):
    if not arr:
        return "array is empty"
    
    #Initialize first element as the largest
    largest_element = arr[0]

    #Iterate through the array top find the largest element
    for element in arr:
        if element > largest_element:
            largest_element = element

    return largest_element

my_array = [10,20,99,30]
result = find_largest_element(my_array)
print(f"The largest element in the array is:{result}")