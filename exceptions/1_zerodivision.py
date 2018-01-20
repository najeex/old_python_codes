def input_number():

    a = float(input("Enter first number:"))
    b = float(input("Enter second number:"))
    return a, b


x, y = input_number()

# print("{0} / {1} is {2}".format(x, y, x / y))

# while True:
#   if y != 0:
#print("{0}/{1}is{2}".format(x, y, x / y))
#     break
# else:
#    print("cannot divide by zero")
#   x, y = input_number()

while True:
    try:
        print("{0}/{1} is {2}".format(x, y, x / y))
        break

    except ZeroDivisionError:

        print("Cannot divide by zero")
        x, y = input_number()
        
