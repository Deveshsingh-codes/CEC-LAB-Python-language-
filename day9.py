Name = "Rahul"
Age = 25
print("My Name is " + Name)
print("My Age is " + str(Age)) # Printing the age as a string ... Output-My Age is 25

Name = "Rahul"
Age = "25"
print("My Name is " + Name)
print("My Age is " + Age) # Output- My Age is 25
print("My Age is"+"  "+ Age) # Output- My Age is  25 ..."  " This quotation Add space between these.



Name = "Rahul"
Age = 25
Email = "Zero2march@gmail.com"
Mobile_no = 9651309504
Cgpa = 9.8
print("My Name is {} My Age is {}".format(Name, Age))
print(" My Name is {}\n My Age is {}\n My Email is {}\n My Mobile No is {}\n My Cgpa is {}".format(Name, Age, Email, Mobile_no, Cgpa))

Name = "Rahul"
Age = 25
Email = "Zero2march@gmail.com"
Mobile_no = 9651309504
Cgpa = 9.8
print("My Name is {Name}\n My Age is {Age}\n My Email is {Email}\n My Mobile No is {Mobile_no}\n My Cgpa is {Cgpa}".format(Name=Name, Age=Age, Email=Email, Mobile_no=Mobile_no, Cgpa=Cgpa)) 