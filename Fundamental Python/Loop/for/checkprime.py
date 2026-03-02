num=int(input("enter your check number :"))
counts=0
for i in range(1,num+1):
   if num%i==0:
       counts=counts+1
       print(i)
if counts >2:
    print(f"the number {num} is multiples {counts} so it is not prime")
else:  
    print(f" the number {num} is  prime ")
    
    
