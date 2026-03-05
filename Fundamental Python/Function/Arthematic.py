# add two number 
def add(num1):
    num=23
    return num+ num1
print (add(234))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))


def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

def Difference(x,y):
   return x-y
print(f"the Difference of 2 and 5 is : { Difference(2 ,5)}")

def product(x,y,z):
    return x*y*z
multiple=product(23,3,4)
print(f"the product of three number is 23 ,3 and 4 products is : {multiple}")
