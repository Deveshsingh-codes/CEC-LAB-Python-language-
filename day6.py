#num = int(input("Enter the Number = "))
#num = float(input("Enter the Number = "))
#if num>0:
#    print("Positive number.")
#elif num<0:
#    print("Negative number.")
#else:
#    print("Number is zero.")
#    

# <---- BY USING OPERATORS ---->

#Students_Marks = int(input("Enter the Marks of Subject: "))
#
#if Students_Marks >= 90:
#    print("Excellent.")
#
#elif Students_Marks >= 75:
#    print("PASS.")
#
#elif Students_Marks >= 40:
#    print("Needs to improve.")
#
#else:
#    print("FAIL.")
#
##<--- BY USING AND AND OR --->
#
#Students_Marks = int(input("Enter the Marks of Subject: "))
#
#if Students_Marks >= 90 and Students_Marks <= 100:
#    print("Excellent.")
#
#elif Students_Marks >= 75 and Students_Marks < 90:
#    print("PASS.")
#
#elif Students_Marks >= 40 and Students_Marks < 75:
#    print("Needs to improve.")
#
#else:
#    print("FAIL.")

Student_Name=str(input("Enter your Name :"))
Student_marks=int(input("Enter the Marks :"))
if Student_marks<0 or Student_marks>100:
    print("Invalid Marks")
elif Student_marks >= 90 and Student_marks <= 100:
    print("Excellent.")

elif Student_marks >= 75 and Student_marks < 90:
    print("PASS.")

elif Student_marks >= 40 and Student_marks < 75:
    print("Needs to improve.")

else:
    print("FAIL.")