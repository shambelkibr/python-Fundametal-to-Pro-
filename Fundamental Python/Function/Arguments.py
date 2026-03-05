def print_args(*args):
    for i in args:
        print(i,end=" ")
    print()
print_args(1,2,3,4,5)


def printargas(**kwargs):
    for key,value in kwargs.items():
        print(f'{key}:{value} ')
printargas(a=2,b=3,c=4)