def add( *args):
    sum = 0
    print(args)
    for n in args:
        sum += n
    return sum


a = 1, 2, 3
print(add(a))