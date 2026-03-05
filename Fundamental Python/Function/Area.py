
def circle_Area():
   PI=3.14
   radius=float(input("enter the radius of the circle : "))
   return PI*radius**2
print(f"the area of circle is {circle_Area()}")



def functinal_country(country="Ethiopia"):
   print("your natinal is : "+country) 
countrys=input("Enter your country : ")
functinal_country(countrys)  
functinal_country()


def Avarage(a,b,c,d,e):
   return (a+b+c+d+e)/5
print("the Avarage sum of 1,2,3,4,5 is ",Avarage(1,2,3,4,5))

def add_two_num(num1,num2):  # 1
    return  num1+num2
print(add_two_num(23,24))

def area_of_circle (r):
    return r**2*3.14
print(f"the area of circle with radius 10 is : {area_of_circle(10)}")

def add_aa(*number):
    sum=0
    for i in number:
        if isinstance(i,(float,int)):
           sum=sum+i 
    print(sum )      
add_aa(23,23,"hello",24,2345,"abse",25)


def conver_to_celciuse_to_firanet(celcies): # 4
    Firainet = celcies*(9/5)+32
    return Firainet
print(conver_to_celciuse_to_firanet(-40))
 
        