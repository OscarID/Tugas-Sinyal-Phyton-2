# Function to perform convolution of two 1-dimensional arrays
def convolution(arr1, arr2):
    # Get the lengths of the input arrays
    len_arr1 = len(arr1)
    len_arr2 = len(arr2)
    
    # Initialize the result array with zeros
    result = [0] * (len_arr1 + len_arr2 - 1)
    
    # Perform convolution
    for i in range(len_arr1):
        for j in range(len_arr2):
            result[i + j] += arr1[i] * arr2[j]
    
    return result

# Example input arrays
arr1 = [2, 1, 3, 6]
arr2 = [1, 2]



# Print the results
print ("Naive Implementation of Convolution")
print ("Clearesta Frederika Oscar")
print(5009211064)

print (convolution(arr1, arr2))


