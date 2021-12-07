def same_structure_as(original, other):
    # try to compare each element recursively

    return True


# should return True
print(same_structure_as([1, 1, 1], [2, 2, 2]))
print(same_structure_as([1, [1, 1]], [2, [2, 2]]))

# should return False
print(same_structure_as([1, [1, 1]], [[2, 2], 2]))
print(same_structure_as([1, [1, 1]], [[2], 2]))

# should return True
print(same_structure_as([[[], []]], [[[], []]]))

# should return False
print(same_structure_as([[[], []]], [[1, 1]]))
