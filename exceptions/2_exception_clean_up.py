try:
    x = float(input("your number must be float: "))
    invers = 1.0 / x
except ValueError:
    print("float number plz...!!!")
except ZeroDivisionError:
    print('Infinity')
finally:
    print('good')
