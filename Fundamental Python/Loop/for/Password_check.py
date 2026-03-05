password="data"



for trial in range(1,5):
    if (trial==4):
        print("only one trial left")
    enter_password=input("enter your password : ")
    if(password==enter_password):
        print("Welcame to python course")
        
        break

    else:
        print("Wrong password")