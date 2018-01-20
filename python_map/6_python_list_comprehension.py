def s(x):
    return x * x


nums = [1, 2, 3, 4, 5]

ns = [s(n) for n in nums]

for n in ns:
    print(n)
