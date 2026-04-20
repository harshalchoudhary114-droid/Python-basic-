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










