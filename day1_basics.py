# Day 1 programs
# Day 1: Python Basics
# Author: Aslim Shaikh
# Goal: Practice core Python syntax and concepts

# 1. Hello World Program
print("Hello World")

# 2. Add Two Numbers
#taking variables
num1 = int(input("Enter your 1st no:"))
num2 = int(input("Enter your 2nd no:"))
sum = num1+num2
print("sum of two numbers:",sum)

# 3. Area of a Rectangle
length = float(input("Enter length of rectangle:"))
width = float(input("Enter width of rectangle:"))
area = length*width
print("area of rectangle:",area)

# 4. celcius to fahrenheit coversion
celsius= float(input("Enter temperature in celsius:"))
fahrenheit =(celsius*9/5)+32
print("termperature in fahrenheit:",fahrenheit)


# 5. voting eligible?
age= int(input("Enter your age:"))
if age>=18:
    print("eligible")

# 6. Swapping two nos
a= int(input("Enter 1st no:"))
b =int(input("Enter 2nd no:"))
a,b=b,a
print ("after swapping a=",a , "b=",b)

# 7. Avg of 5 subjects
a=int(input("enter marks of subject1:"))
b=int(input("Enter marks of subject2:"))
c=int(input("Enter marks of subject3:"))
d=int(input("Enter marks of subject4:"))
e=int(input("Enter marks of subject5:"))
average = (a+b+c+d+e)/5
print(" Avg of 5 subjects:",average)

# 8. Consonant in alphabets?
x=str(input("enter a alphabet:"))
if x!="a" and x!="e" and x!="i" and x!="o" and  x!="u":
  print("it is a consonant")

# 9. vowel in alphabets?
x=str(input("enter an alphabet:"))
if x=="a" or x=="e" or x=="i" or x=="o" or x=="u" :
 print(" it is a vowel")

# 10. Simple Interest Calculator
p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time (years): "))

si = (p * r * t) / 100
print(f"Simple Interest = {si}")


# 11. Mini project simple calculator
print("\nSimple Calculator")
a=float(input("enter 1st no:"))
b=float(input("enter 2nd no:"))
c=input("Enter the operator:")
if c=="+":
  print("result:", a+b)

elif c=="-":
  print("result:", a-b)

elif c == "*":
  print("result:",a*b)
 
elif c == "/":
   if b!=0:
    print("result:", a/b)
   else:
    print("error: divisible by zero,invalid operation")

elif c=="//":
 print("result:", a//b)

elif c=="%":
 print("result:", a%b)

elif c=="**":
  print("result:", a**b)

