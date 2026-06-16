"""
Here are some NumPy practice questions arranged from easy to slightly challenging.

Level 1: Basics

Q1. Create an array

Create a NumPy array containing:

[10, 20, 30, 40, 50]

Print the array.
"""
"""
import numpy as np

arr = [10, 20, 30, 40, 50]
print(arr)
"""


"""
Q2. Access Elements

Using:

arr = np.array([5, 10, 15, 20, 25])

Print:

* First element
* Last element
* Third element
"""
"""
import numpy as np

arr = np.array([5, 10, 15, 20, 25])

# First element
print("First element:", arr[0])

# Last element
print("Last element:", arr[-1])

# Third element
print("Third element:", arr[2])
"""


"""
Q3. Modify Elements

Using:

arr = np.array([1, 2, 3, 4, 5])

Change 3 to 100.
"""
"""
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Change 3 to 100
arr[2] = 100

print(arr)
"""


"""
Q4. Array Length

Print the number of elements in:

arr = np.array([11, 22, 33, 44, 55])
"""
"""
import numpy as np

arr = np.array([11, 22, 33, 44, 55])

print(len(arr))
"""


# Level 2: Mathematical Operations

"""
Q5. Add 10

Using:

arr = np.array([1, 2, 3, 4, 5])

Add 10 to every element.

Expected:

[11 12 13 14 15]

"""
"""
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Add 10 to each element
result = arr + 10

print(result)
"""


"""
Q6. Multiply

Multiply every element by 5.

arr = np.array([2, 4, 6, 8])
"""
"""
import numpy as np

arr = np.array([2, 4, 6, 8])

# Multiply each element by 5
result = arr * 5

print(result)
"""


"""
Q7. Square Numbers

Convert:

[1, 2, 3, 4, 5]

into:

[1, 4, 9, 16, 25]
"""
"""
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Square each element
result = arr ** 2

print(result)
"""