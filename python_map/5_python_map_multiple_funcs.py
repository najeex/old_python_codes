def add(x):
    return x + x


def square(x):
    return x * x


n = [1, 2, 3, 4, 5]

for i in n:
    vals = list(map(lambda x: x(i), (add, square)))
    print(vals)
