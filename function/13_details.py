def display(**details):
    for i in details:
        print("{0}:{1}".format(i, details[i]))


display(name="Larry", age=43, sex="M")
