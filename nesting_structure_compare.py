from typing import List


def same_structure_as(original, other):
    same_length = check_length(original, other)
    # print('-'*40)
    ret_final = True
    if same_length:
        for ori_item, other_item in zip(original, other):
            if check_structure(ori_item, other_item):
                # check if List
                #  do nothing if not list because we only want to compare structure
                if isinstance(ori_item, List):
                    # compare length
                    if check_length(ori_item, other_item):
                        # TODO how to repeat process until item is no longer a list ????
                        # print(f'{ori_item} vs {other_item}')
                        hasil = slice_list(ori_item, other_item)
                        if hasil == False:
                            ret_final = False
                    else:
                        return False
            else:
                # structure is diffrent, return false
                return False

        if ret_final:
            return True
        else:
            return False
    else:
        return False


def check_length(array_one, array_two):
    # compare length (len) between original & other
    if isinstance(array_one, List) and isinstance(array_two, List):
        if len(array_one) != len(array_two):
            return False
        else:
            return True
    else:
        return False


def check_structure(array_one, array_two):
    if isinstance(array_one, List) == isinstance(array_two, List):
        return True
    else:
        return False


def slice_list(array_one, array_two):
    for ori_one, other_two in zip(array_one, array_two):
        if check_structure(ori_one, other_two):
            if isinstance(ori_one, List):
                if check_length(ori_one, other_two):
                    # print(f'{ori_one} vs {other_two}')
                    slice_list(ori_one, other_two)
                else:
                    return False
        else:
            return False


# from best result
def same_structure_as2(original, other):
    if isinstance(original, list) and isinstance(other, list) and len(original) == len(other):
        for o1, o2 in zip(original, other):
            if not same_structure_as(o1, o2):
                return False
        else:
            return True
    else:
        return not isinstance(original, list) and not isinstance(other, list)


def same_structure_as3(original, other):
    if type(original) == list == type(other):
        return len(original) == len(other) and all(map(same_structure_as, original, other))
    else:
        return type(original) != list != type(other)


def same_structure_as4(a, b):
    return (False if not (isinstance(a, list) and isinstance(b, list)) or len(a) != len(b)
            else all(same_structure_as(c, d) for c, d in zip(a, b) if isinstance(c, list)))


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
