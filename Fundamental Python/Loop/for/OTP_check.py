OTP="123"

for trial in range (1,5):
    if (trial==4):
        print("one trial left")
        
    enter_OTP=input("Enter OTP : ")
    if (enter_OTP!=OTP):
        print("try again")
        continue
    else:
        name=input("Enter your name : ")
        age=int(input("Enter your age : "))
        break