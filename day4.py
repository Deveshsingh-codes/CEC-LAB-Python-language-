Name = input("What is your name=")
print(Name)
print(type(Name))


num1=input("Enter your first number=")
num2=input("Enter your second number=")
result=num1+num2
print(result)


num1=int(input("Enter your first number="))
num2=int(input("Enter your second number="))
result=num1+num2
print(result)
print(type(num1)) #<class 'int'>

name = input("Full Name :")
age = input("Age :")
email = input("Email Address:")
print(name)
print(age)
print(email)

Num1=int(input("Enter the Num1="))
Num2=int(input("Enter the Num2="))
Total=Num1 + Num2
print(Total)
print(type(Num1))


print("a","m","a","n")
print("a","m","a","n",sep="-")
print("a","m","a","n",sep="\n")
print("a","m","a","n",end=",")
print("a","m","a","n",end=".")

Subject_1=float(input("Subject 1 :"))
Subject_2=float(input("Subject 2 :"))
Subject_3=float(input("Subject 3 :"))
Subject_4=float(input("Subject 4 :"))
Subject_5=float(input("Subject 5 :"))
print(Subject_1, Subject_2, Subject_3, Subject_4, Subject_5, sep="\n" )

Total=Subject_1 + Subject_2 + Subject_3 + Subject_4 + Subject_5
percentage=(Total/500)*100
print("The total of all subjects is = ",Total)
print("The percentage of all subjects is = ",percentage)


num1=int(input("Enter Number:"))
num2=int(input("Enter Number:"))

sum=num1 + num2
subrtact=num1-num2
multiply=num1*num2
divide=num1/num2
print("the Sum is= ",sum,("subrtact",subrtact),("multiply",multiply),("divide",divide), sep="\n")