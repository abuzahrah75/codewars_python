import string

pangram = "The quick, brown fox jumps over the lazy dog!"


def is_pangram(pangram):
    return True if all(x in pangram.lower()
                       for x in string.ascii_lowercase) else False
    # if all(x in pangram.lower() for x in string.ascii_lowercase):
    #     pangram_status = True
    # else:
    #     pangram_status = False

    # return pangram_status


# pangram = "The quick, brown fox jumps over the lazy dog!"
# pangram = "The quick, brown fox jumps over the lazy dog!"
# print(pangram.lower())
print(is_pangram(pangram))
# print(string.ascii_lowercase)
