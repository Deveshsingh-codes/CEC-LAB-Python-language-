print("Hellow world!")
name = 12334
print(name)
name2 = "74647"
print(name2)

num = 9651
print("num",num)

print(type(name2))
print(type(name))
print(type(num))

a_b="abcd"
print(a_b)

a="abcd"
A="efgh"
print(a,A)

name= "Devesh Singh"
age=19
print("This is the name:", name, "\nAge:", age)

a=1
b=2
c=3
a,b,c=1,2,3
print(a)
print(a,b,c)

a=b=c=d=1
print(a,"\n",b,c,d)


import keyword
print(keyword.kwlist) # by this we can see all the keywords in python

num=1234
name="avgs"
dec=129.098
place=True
print(type(num))
print(type(name))
print(type(dec))
print(type(place)) #by using type we can see the data type of the variable


#Typecasting

age="19"
#print(age+5) #this will give error because age is string and 5 is integer
print(int(age)+5) #this will give 24 because we have converted age into integer

age2=19
print(str(age2)+ " is my age") #this will give 19 is my age