x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

even_elements = x[::2]

even_elements_reversed = even_elements[::-1]

x[::2] = even_elements_reversed

print(x)

#test

#[8, 1, 6, 3, 4, 5, 2, 7, 0, 9]