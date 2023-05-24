import copy

"""
How does copying work in Python?

When we create a variable, the list is stored in the memory. The
assignment operation will us the same location in memory, meaning that 
in the case below A and B are the same.
"""
A = [1, 2, 3]
B = A

print(id(A) == id(B))  # True
print(id(A[0]) == id(B[0]))  # True

"""
Alternatively, we can make a shallow copy, in which the list object itself
has a distinct location, but the objects inside the list remain the same.
"""
B = copy.copy(A)
# B = A[:] achieves the same
# B = list(A)

print(id(A) == id(B))  # False
print(id(A[0]) == id(B[0]))  # True


"""
Finally, we are also able to make a deep copy, where the objects within the list 
are also copied and have distinct memory locations 
"""
B = copy.deepcopy(A)

print(id(A) == id(B))  # False
print(id(A[0]) == id(B[0]))  # False

"""
Rotating a list.

Say we want to cycle our list, i.e. from 1, 2, 3 to 2, 3, 1. We can do
this in the following way.
"""
print(A[1:] + A[:1])
