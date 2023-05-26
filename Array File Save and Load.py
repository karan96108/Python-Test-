'''import numpy as np

# Create an array
arr = np.array([1, 2, 3, 4, 5])

# Save the array to a file
np.save('array.npy', arr)'''
import numpy as np

# Load the array from the file
loaded_arr = np.load('array.npy')

print(loaded_arr)
