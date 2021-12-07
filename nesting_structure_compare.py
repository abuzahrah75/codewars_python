from typing import List


def same_structure_as(original, other):
    # try to compare each element recursively
    # compare length (len) between original & other
    if len(original) != len(other):
        return False
    for ix in original:
        if isinstance(ix, List):
            retstr = f'{ix} adalah list / array'
        else:
            retstr = f'{ix} bukan lah list / array'

    return retstr


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
