def zero(kira=False):  # your code here
    if kira:
        if kira[0] == "plus":
            return 0 + kira[1]
        if kira[0] == "minus":
            return 0 - kira[1]
        if kira[0] == "times":
            return 0 * kira[1]
        if kira[0] == "divide":
            return 0 / kira[1]
        # return True
    else:
        return 0


def one(kira=False):  # your code here
    if kira:
        if kira[0] == "plus":
            return 1 + kira[1]
        if kira[0] == "minus":
            return 1 - kira[1]
        if kira[0] == "times":
            return 1 * kira[1]
        if kira[0] == "divide":
            return 1 / kira[1]
    else:
        return 1


def two(kira=False):  # your code here
    if kira:
        if kira[0] == "plus":
            return 2 + kira[1]
        if kira[0] == "minus":
            return 2 - kira[1]
        if kira[0] == "times":
            return 2 * kira[1]
        if kira[0] == "divide":
            return 2 / kira[1]
    else:
        return 2


def three(kira=False):  # your code here
    if kira:
        if kira[0] == "plus":
            return 3 + kira[1]
        if kira[0] == "minus":
            return 3 - kira[1]
        if kira[0] == "times":
            return 3 * kira[1]
        if kira[0] == "divide":
            return 3 / kira[1]
    else:
        return 3


def four(kira=False):  # your code here
    if kira:
        if kira[0] == "plus":
            return 4 + kira[1]
        if kira[0] == "minus":
            return 4 - kira[1]
        if kira[0] == "times":
            return 4 * kira[1]
        if kira[0] == "divide":
            return 4 / kira[1]
    else:
        return 4


def five(kira=False):  # your code here
    if kira:
        if kira[0] == "plus":
            return 5 + kira[1]
        if kira[0] == "minus":
            return 5 - kira[1]
        if kira[0] == "times":
            return 5 * kira[1]
        if kira[0] == "divide":
            return 5 / kira[1]
    else:
        return 5


def six(kira=False):  # your code here
    if kira:
        if kira[0] == "plus":
            return 6 + kira[1]
        if kira[0] == "minus":
            return 6 - kira[1]
        if kira[0] == "times":
            return 6 * kira[1]
        if kira[0] == "divide":
            return 6 / kira[1]
    else:
        return 6


def seven(kira=False):  # your code here
    if kira:
        if kira[0] == "plus":
            return 7 + kira[1]
        if kira[0] == "minus":
            return 7 - kira[1]
        if kira[0] == "times":
            return 7 * kira[1]
        if kira[0] == "divide":
            return 7 / kira[1]
    else:
        return 7


def eight(kira=False):  # your code here
    if kira:
        if kira[0] == "plus":
            return 8 + kira[1]
        if kira[0] == "minus":
            return 8 - kira[1]
        if kira[0] == "times":
            return 8 * kira[1]
        if kira[0] == "divide":
            return 8 / kira[1]
    else:
        return 8


def nine(kira=False):  # your code here
    if kira:
        if kira[0] == "plus":
            return 9 + kira[1]
        if kira[0] == "minus":
            return 9 - kira[1]
        if kira[0] == "times":
            return 9 * kira[1]
        if kira[0] == "divide":
            return 9 / kira[1]
    else:
        return 9


def plus(value):  # your code here
    return ["plus", value]


def minus(value):  # your code here
    return ["minus", value]


def times(value):  # your code here
    return ["times", value]


def divided_by(value):  # your code here
    return ["divide", value]


print(seven(times(five())))
# print(plus(two()))
