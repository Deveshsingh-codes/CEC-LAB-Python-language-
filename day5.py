num = 35
if num >49:
    print("PASS")
    
Num2=int(input("Enter the number = "))
if Num2 < 20:
    print("WOW! u guess the number less than 20.")
elif Num2 > 20:
    print("WOW! u guess the number greater than 20.")

Age = int(input("Enter your age :"))
if Age > 18:
    print("Congractulations🎉! You are eligible for this post.")
elif Age == 18:
    print(" Wait for the completion of your AGE.")
else:
    print("ooops🫠! Soory, u are not eligible for this post.")


Num1=int(input("Enter Num1:"))
Num2=int(input("Enter Num2:"))
Num3=int(input("Enter Num3:"))
if Num1 > (Num2 and Num3):
    print("Num1 is greater than All.")
if Num2 > (Num1 and Num3):
    print("Num2 is greater than All.")
if Num3 > (Num2 and Num1):
    print("Num3 is greater than All.")
