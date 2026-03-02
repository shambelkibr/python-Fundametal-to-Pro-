sum1=0
for i in range(10+1):
        sum1+=i  
print(f"the sum of first ten integers is {sum1}")  


sum2=0
for num2 in range(0,101,5):
    print(num2)
    sum2+=num2
print(f"the sum of 1 up to 100 the multiple of 5 is:= {sum2}")
    
count_even=0
sum3=0
i=1
for i in range(11):
    if i % 2==0:
        count_even=count_even+1
        sum3+=i
print(f"the frist {count_even} number between 1 and 10 sum  is {sum3}") 