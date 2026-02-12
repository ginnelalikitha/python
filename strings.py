s="Iam likitha" #slicing
#[start:stop:step]
print(s[1])
print(s[1:5])
print(s[1:-1])
print(s[2:])
print(s[:-1])
print(s[::2])
print(s[1::2])
print(s[::-2])

#string concatenation(+)
"""a="suresh"
b="ramesh"
print("suresh"+" "+"ramesh")"""

#string length
"""string="helloworld"
print(len(string))"""

#string methods(converting ,upper to lower,replace)
"""s="likitha"
print(s.upper())
print(s.lower())
print(s.replace('t','s'))
print(s.strip())
print('abracadabra'.count('a'))"""

#escape strings

"""print("hello\'s world")
print("hello\"s world")
print("hello\ns world")"""  

#examples

"""name=input("enter any name:")
n1 =name.upper()
a =n1.count('A')
e =n1.count('E')
i =n1.count('I')
o =n1.count('O')
u =n1.count('U')

print(f"Number of vowels: {a+e+i+o+u}")"""

#grade calculator
"""math=int(input("marks in math:"))
science=int(input("marks in science:"))
english=int(input("marks in english:"))
totalmarks=math+science+english
average=totalmarks/3
percentage=(totalmarks/300)*100
Grade=" "

if percentage>90:
        Grade="A"
elif percentage >80 and percentage <=90: 
        Grade="B"
elif percentage >70 and percentage <=80: 
        Grade="C"
else:
        Grade="P"                    

print(f"totalmarks:{totalmarks} \n average:{average} \n Grade:{Grade}")"""

#palindrome
"""string=input("enter a name:")
reverse=string[::-1]

if reverse==string:
    print("It is a palindrome")
else:
    print("It is not a palindrome") """

#example
"""a,b,c=(input("enter three numbers:")).split(",")
x=int(a)  
y=int(b)  
z=int(c)  

if x>y and x>z:
    print(f"The largest number is:{x}")
elif y>x and y>z:
    print(f"The largest number is:{y}")
elif z>x and z>y:
    print(f"The largest number is:{z}")
else:
    print("all numebers are equal") """

#leap year
"""year=int(input("enter a year:"))

if (year%400==0) or ((year%100!=0) and (year%4==0)):
    print("It is a leap year")
else:
    print("not a leap year")"""

#temperature converter 
"""temp=int(input("enter any temp:"))
units=input("enter any units k or f or c:")

if units=='c':  
  f=(temp*(9/5)+32)
  k=273.15+temp
  print(f"Temperature in fahrenheit:{f}") 
  print(f"Temperature in kelvin:{k}") 
elif units=='k':
  f=((temp-273.15)*9/5+32)
  c=temp-273.15 
  print(f"Temperature in fahrenheit:{f}") 
  print(f"Temperature in celsius:{c}") 
elif units=='f':
   c=(temp-32)*5/9
   k=((temp-32)*5/9+273.15)
   print(f"Temperature in celsius:{c}") 
   print(f"Temperature in kelvin:{k}") 
else:
  print("invalid input")"""     





