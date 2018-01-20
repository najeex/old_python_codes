name = "najeeb"


def f():
    global name
    name = "Khan"
    print("within function", name)


print("Outside function", name)
f()
print("Outside function", name)
