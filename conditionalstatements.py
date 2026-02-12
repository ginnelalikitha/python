#if else
"""price=input("enter a value:")

if price=="150":   #else statement
    print("go to movie")
else:              #if+else statement
    print("Go to sleep")    
print("Have a good day") """
 
 #elif
"""weather=input("enter a string:")

if weather=="sunny":
    print("I will play cricket")
elif weather=="rainy":
    print("I will play sudoko")
elif weather=="cloudy":
    print("sauna")    
else:
     print("goto sleep)"""


n1=int(input("give 1st n"))
n2=int(input("give 2nd n"))
operator=input("give any operator")

if operator=="+":
    print(f"addition:{n1+n2}")
elif operator=="-":
    print(f"subtraction:{n1-n2}") 
elif operator=="*":
    print(f"multiplication:{n1*n2}") 
else:
    print(f"division:{n1/n2}")      
