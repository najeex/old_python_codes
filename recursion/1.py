def sum(list):
    sum = 0

    for i in range(0, len(list)):
        #print(range(0, len(list)))
        sum = sum + list[i]

    return sum


#print(sum([1, 2, 3, 4, 5]))


f = lambda a,b : a if (a>b) else b
reduce(f, [2])
