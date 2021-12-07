
def DNA_strand(dna):
    return_string = ""
    for item in dna:
        if item == "T":
            return_string = return_string + "A"
        if item == "A":
            return_string = return_string + "T"
        if item == "G":
            return_string = return_string + "C"
        if item == "C":
            return_string = return_string + "G"

    return return_string

    # return dna.translate(string.maketrans("ATCG", "TAGC"))


print(DNA_strand("TTAA"))
