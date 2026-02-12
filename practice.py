#swap 
"""l=[1,2,3,4,5,6]
l[0],l[-1]=l[-1],l[0]
print(l)"""
#print elements reverse
"""l=[1,2,3,4,5,6]
rev=l[::-1] #or l.reverse()
print(rev)"""
#remove duplicate values

"""inp=input().split(",")

l=[int(items) for items in inp]
   
newl=[]

for i in l:
    if i not in newl:
       newl.append(i)
print(newl)"""

#fibanocci series
"""i=int(input(""))
a=0
b=1
fib=[]

for i in range(i):
    fib.append(a)
    a,b=b,a+b
print(fib)"""

#prime number check
"""n=int(input(""))

if n<1:
    print("not a prime")
else:
    for i in range(2,n):
        if n%i==0:
                print("not a prime")
                break
        else:
             print("prime number")"""

#lcm and gcd
"""import math

s=math.lcm(12,18)#for lcm
print(s)

s=math.gcd(12,18) #for gcd
print(s)"""

#random number guessing

"""import random

num=random.randint(0,100)
count=0

while True:
    guess=int(input("guess a num"))
    count+=1
    if guess<num:
        print("too low")
    elif guess>num:
        print("too high")
    else:
        print("correct guess")
        break """

#vowels in string

"""n=("likitha")
n.lower()
a=n.count('a')
e=n.count('e')
i=n.count('i')
o=n.count('o')
u=n.count('u')
print(f"num of vowels:{a+e+i+o+u}")"""

#consonants in a string using loops
""""n=input("enter:")
 
vowels="aeiouAEIOU"
consonant_count=0 

for char in n:
    if char.isalpha() and char not in vowels:
        consonant_count+=1

print(f"conosananta: {consonant_count}")"""

#vowels in a string using loops
"""n=input("enter:")
 
vowels="aeiouAEIOU"
vowels_count=0 

for char in n:
    if char.isalpha() and char  in vowels:
        vowels_count+=1

print(f"vowels: {vowels_count}")"""   

#anagram checker

"""n=("race")
anagram=input("enter")


if sorted(n) == sorted(anagram):
        print("both are same")
else:
        print("both are not same")"""

#decimal to binary
"""b=int(input("enter"))
print(bin(b)[2:]) """ #print(int(b,2)) for binary to decimal

#sum
"""a="hi"
b="world"
print(a+b)
print(a,b)""" #in strings we can place two words side by side using "+" and ",""

#trying
"""n="likitha089"
s=n.isalnum()
print(s)"""

"""text="Hey, I am learning GenAI and Agentic AI, I love GenAI"
print(text.find("am"))"""

#remove duplicate values
"""n=[1,2,2,3,4,5]
print(list(set(n)))"""

#factorial
"""def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

print(factorial(5))"""

#swap
"""i1=int(input())
i2=int(input())
i2=i2+i1
i1=i2-i1
i2=i2-i1"""

"""(i1,i2)=(i2,i1)""" #for strings
"""print(i1)
print(i2)"""

#count
"""m=[1,2,3,2,5,6]
count_2=m.count(2)
print(count_2)"""

#practice

"""for i in range(7,1,-1): #1
            print("*" *i)
   
for i in range(1,8): #2
            print("*" *i)"""

"""table=9 #3
for i in range(1,11):
    print(table,"x", i ,"=" ,table*i)"""

"""l=["likitha","madhu","shirisha","sagar","kushi"] #4
l.append("kiwi")   
print(l)"""

"""l={"name":"likitha","rollno":17,"gender":"female","nationality":"indian"} #5
l.update({"name":"hitha"})
print(l)
print(l.values())
print(l.keys())"""

"""for i in range(7):
    print(i)"""

"""count=0
while count<6:
        print(count)
        count+=1"""

"""print("operations \n")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")

choice=input("enter any operation")
num1=int(input("enter first num:"))
num2=int(input("enter second num:"))

add=num1+num2
subtract=num1-num2
multiply=num1*num2
divide=num1/num2

if choice=="1":
    print(f"the addition of:{add}")
elif choice=="2":
    print(f"the subtraction  of:{subtract}")
elif choice=="3":
     print(f"the subtraction  of:{multiply}")
elif choice=="4":
     print(f"the subtraction  of:{divide}")
else:
     print("invalid operation")"""


"""#defining the function 
def greet(name):
    return f"Hello,{name}!"
#calling the function
print(greet("Alice")) """


"""def greet(age):
    return f"My age:{age}"
print(greet(45))"""


"""num=int(input("enter a number:"))
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print(f"the factorial of{num} if {factorial(num)}") """   
    
#interest
"""principle=500
rate=5
time=3
interest=(principle*rate*time)/100
print(f"the interest is:{interest}")"""

#average
"""a=50
b=20
c=70
average=(a+b+c)/3
print(f"the average is:{average}")"""

#area of a triangle
"""h=10
b=5
area=(0.5*h*b)
print(f"area is:{area}")"""

#kilometers to miles
"""km=8
km_conversion=0.621
n=(km*km_conversion)
print(f"kilometers to miles:{n}")"""

#calculate square root
"""n=4
square_root=(n*n)
print(f"square root of {n} is {square_root}")
 #or
n=81
square_root=n^0.5
print(f"square root of {n} is {square_root}")"""

#power of a number
"""um=int(input("enter a num:"))
for i in range (1,9):
    power=num**i
    print(f"the powers of{num} is{power}")
#or
n=int(input("enter a num:"))
num=0
while num<9:
    num+=1
    power=n**num
    print(f"the powers of{n} is{power}")"""

#check if the number is positive or negative
"""n=int(input("enter a num:"))
if n>0:
    print("positive number")
elif n<0:
     print("negative number")
else:
     print("zero") """

#check if its even or odd
"""n=int(input("enter a num:"))
if n%2==0:
    print("even number")
else:
    print("odd number")  """

#finding  the largest number
"""n1=int(input("enter a num:"))
n2=int(input("enter a num:"))
n3=int(input("enter a num:"))

if n1>n2 and n1>n3:
    print(f"the largest num is:{n1}")
elif n2>n1 and n2>n3:
       print(f"the largest num is:{n2}")  
else:
         print(f"the largest num is:{n3}")"""

#check leap year
"""n=int(input("enter a num:"))

if n%400==0 or((n%100!=0) and (n%4==0)):
    print("is a leap year")
else:
    print("not a leap year")"""

#prime number
n=int(input("enter a num:"))
if n>1:
    for i in range(2,n):
     if n%i==0:
      print("Its not a prime")
      break
    else:
           print("its a prime")
else:
    print("Its not a prime")









