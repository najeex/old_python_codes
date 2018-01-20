def f():
    ''' this function print a message'''
    print("Today it is cloudy day")


print(isinstance(f, object))
print(id(f))

print(f.__doc__)
print(f.__name__)
