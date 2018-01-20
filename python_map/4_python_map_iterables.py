def multiply(x, y):
    return x * y


n1 = [1, 2, 3, 4, 5]
n2 = [6, 7, 8, 9, 10]

m = map(multiply, n1, n2)

for num in m:
    print(num)
