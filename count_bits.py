def count_bits(n):
    return [char for char in str(bin(n))[2:]].count('1')


print(count_bits(0))
print(count_bits(4))
print(count_bits(7))
print(count_bits(9))
print(count_bits(10))

quote = "How can mirrors be real if our eyes aren't real"
print(quote.title())
