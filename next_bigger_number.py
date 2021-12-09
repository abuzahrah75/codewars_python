def next_bigger(n):
    list_of_digits = [int(x) for x in str(n)]
    list_of_digits.sort(reverse=True)
    new_n2 = ''.join(str(xx) for xx in list_of_digits)
    if n >= int(new_n2):
        return -1
    else:
        n_collect = check_isin_v2(list_of_digits, n)
    return n_collect


def check_isin_v2(list_of_digits, n):
    ret_n = False
    xcount = n
    while ret_n == False:
        xcount += 1
        if all(str(x) in str(xcount) for x in list_of_digits):
            if sum([int(xcount) for xcount in str(xcount)]) == sum(list_of_digits):
                ret_n = xcount

    return ret_n


def check_x_isin(list_of_digits, new_n2, n):
    n_collect = []
    for nx in range(n, int(new_n2)+1, 1):
        if all(str(x) in str(nx) for x in list_of_digits):
            if sum([int(xn) for xn in str(nx)]) == sum(list_of_digits):
                n_collect.append(nx)
    return n_collect[1]


def check_repeated(item, mylist, list_of_digits):
    if str(item) in str(mylist):
        return True
    else:
        return False


#  test value
# print(next_bigger(12))  # 21
# print(next_bigger(513))  # 531
# print(next_bigger(2017))  # 2071
# print(next_bigger(414))  # 441
# print(next_bigger(144))  # 414
# print(next_bigger(9))  # nil
# print(next_bigger(111))  # nil
# print(next_bigger(531))  # nil


# from attemp
# 598 848484 59934 should equal 598 848484 83559
print(next_bigger(59884848459934))
# 94014207339738 should equal 94014207339792
# 74452036 should equal 74452072
# 834527319 should equal 834527922
# 74238669 should equal 74238678
# 5867 should equal 5885
# 7369230171 should equal 7369230216
# 29857006788 should equal 29857006797
# 852216344 should equal 852231455
# 62640652158657 should equal 62640652158684
