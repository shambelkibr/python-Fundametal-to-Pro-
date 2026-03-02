fact=1
n = int(input("enter the number:= "))
for i in range(1,n+1):
    if i==0:
      fact=1
    else:
     fact=fact*i
    
print(fact)