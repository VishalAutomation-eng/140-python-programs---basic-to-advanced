#Write code to find sum of elements in an array

def sum_of_array(arr):
    total = 0
    
    for element in arr:
        total = total + element
    return total

array = [1,3,2]
result = sum_of_array(array)
print("sum of array :", result)