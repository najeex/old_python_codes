a = [1, 2, 3]
b = ['a', 'b', 'c']

c = [str(i) + j for i in a for j in b]
print(c)
