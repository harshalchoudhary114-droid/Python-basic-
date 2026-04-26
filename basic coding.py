# Basic Algebraic equations using variables
a=input("enter first number:  ")
b=input("enter second number: ")
a=int(a)
b=int(b)
print(a+b)
print(a-b)
print(a%b)
print(a**b)
print(a/b)
print(a*b)
print(a>b)
print(a<b)
print(a==b)
print(a!=b)
print(a!=a)
#Average of Two numbers:-)
a1 = input("give number: ")
a2=input("give another number: ")
a1=int(a1)
a2=int(a2)
print((a1+a2)//2)
a="harshal"
print(a[:7:])
print(len(a))
print(a.endswith("l"))
print(a.count("a"))
print(a.find("a"))
print(a.index("a"))
print(a.lower())
print(a.upper())
print(a.swapcase())
print(a.title())
print(a.isalnum())
print(a.capitalize())
print(a.replace("harshal","harshu"))
me="harshal started studying \t :-). \nshe is good in studies. \nshe will be going to rich very soon ."
print(me)
name=input()
print("Good Afternoon:-)", name)
letter = ('''          Dear <NAME>
          you are selected
          Date:<Date>''' )
NAME=input( "enter your name: ")
Date=input("enter your date: ")
letter = letter.replace( "<NAME>", NAME )
letter=letter.replace( "<Date>", Date )
print(letter)
# list slicing
fruits=input("enter 7 fruits ")
fruitslist=fruits.split(" ")
print(fruitslist)
Marks=input("Enter your Marks: ")
listmarks=Marks.split()
print(listmarks)
listmarks.sort()
print(listmarks)
# Dictionary & Sets
myDict = {"pankha": "Fan", "Pagal": "Stupid", "Vastu": "Thing"}
print("options are ", myDict.keys())
a=input("enter the word: ")
# print("the meaning of your word is:",myDict[a]) (it will give the error )
print("the meaning of your word is:",myDict.get(a)) # it will not give the error
num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
num3=int(input("enter the third number"))
num4=int(input("enter the fourth number"))
num5=int(input("enter the fifth number"))
num6=int(input("enter the sixth number"))
num7=int(input("enter the seventh number"))
num8=int(input("enter the eighth number"))
s ={num1,num2,num3,num4,num5,num6,num7}
print(s)
s = {18,"18"} # both are different values
print(s)
s=set()
s.add(20)
s.add(20.0)
s.add("40")
print(s)
print(len(s))
s={}
print(type(s))
s=set()
print(type(s))
s1=set()
s1.add(input("tell your fav language harshal "))
s1.add(input("tell your fav language janvi "))
s1.add(input("tell your fav language reshma "))
s1.add(input("tell your fav language neelam "))
print(s1)
# conditional , logical & relational expression
age=input("enter your age ")
age=int(age)
if age>=18:
 print("yes")
else:
    print("no")
if age>18 and age<65:
    print("yes")
else:
    print("no")
    if age>18 or age<65:
     print("yes")
    else :
            print("no")
num1=int(input("enter a number "))
num2=int(input("enter another number "))
num3=int(input("enter another number "))
num4=int(input("enter another number "))
if num1>num2 and num1>num3 and num1>num4:
    print("the greatest number is ",num1)
elif num2>num1 and num2>num3 and num2>num4:
    print("the greater number is ",num2)
elif num3>num1 and num3>num2 and num3>num4:
    print("the greatest number is ",num3)
elif num4>num1 and num4>num2 and num4>num3:
    print("the greatest number is ",num4)
else :
        print("all are equal  ")
username = input("Enter your username: ")
print(len(username))
if len(username) <= 10:
    print("Your username is valid")
else:
    print("Your username is invalid")
marks=int(input("enter your marks:"))
if marks>=90:
    grade="A"
elif marks>=80:
        grade="B"
elif marks>=70:
        grade="C"
elif marks>=60:
            grade="D"
else:
            grade="F"
print(grade)
# loops
i=0
while i<5:
    print(i)
    i=i+1
    if i==5:
        break
fruits = ["apple", "banana", "cherry"]
i=0
while i<len(fruits):
    print(fruits[i])
    i=i+1
for fruit in fruits:
    print(fruit)
num=int(input("enter the number "))
for i in range(1,11):
    # print( str(num) + "X" + str(i) + "=" + str((i)*num))
    print(f"{num}*{i}={num*i}")
num = int(input("enter the number "))
prime= True
for i in range(2,num):
    if num%i==0:
        prime = False
        break
if prime:
  print("the number is prime")
else:
 print("the number is not prime")
num=int(input("enter the number "))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
    print(f"factorial of {num} is {factorial}")
n = int(input("Enter a number: "))
sum = 0
sum =( (n*(n+1))/2)
sum=int(sum)
print(sum)
n=int(input())
for i in range(n):
  print(" "*(n-i-1),end="")
  print("*"*(2*i+1),end="")
  print(" "*(n-i-1))
# Functions & Recursions
n=int(input())
def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product

print(factorial_iter(n))
# n! = n*(n-1)*n!
n=int(input())
def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n-1)
print(factorial_recursive(n))
def farh(celsius):
    return celsius * 9 / 5 + 32
print(farh(45))
print("Hello ",end="")
print("how",end=" ")
print("are",end=" ")
print("you?",end=" ")
# sum(n) = sum(n-1)+n
n=int(input())
def recur_sum(n):
    # Base case: if n is 1 or 0, return n
    if n <= 1:
        return n
    else:
        # Recursive step: n + sum of (n-1)
        return n + recur_sum(n - 1)
n=int(input())
for i in range(n):
    print("*"*(n-i))


