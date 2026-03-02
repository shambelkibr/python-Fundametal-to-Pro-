x=input("enter the number: ")
x=int (x)
if x>0:
    print(f"the number {x} is postive ")
elif x<0:
        print(f"the number {x} is negative ")
else:
    print(f"the number {x} is zero ")

# to calculate the electricity bill

r=float(input("enter resister"))
v=float(input("enter voltage"))
I=r/v
if I<150:
    print(f"enter the {150}  birr balace FOR {I} WATT")
elif I>300:
    print(f"enter the {300} birr balance  FOR {I} WATT")
elif I>600|I<900:
    print(f"enter the {600} birr balance FOR {I} WATT")
else:
    print(f"enter the {900} birr ballance FOR {I} WATT ")
    