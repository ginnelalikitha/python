#5 programs for each map,filter and reduce() methods

#map
"""n=[2,4,6,8,10]  #1
power=list(map(lambda x:x**2,n))
print(power)"""

"""def even (n):  #2
    return n%2==0

nums=[2,3,4,56,7,8,9]
even=list(map(lambda x:x%2==0,nums))
print(even)"""

"""def odd(n):  #3
    return n%2!=0

nums=[2,3,4,56,7,8,9]
odd=list(map(lambda x:x%2!=0,nums))
print(odd)"""

"""word=["roam","scream","slap","hit"]  #4
starts_with=list(map(lambda x:x.startswith("s"),word))
print(starts_with)"""

"""nums=[8,2,3,5,1] #5
greater=list(map(lambda x: x>2,nums))
print(greater)"""   

"""x=[2,3,4] #6
y=[5,6,7]
add=list(map(lambda x,y: x+y,x,y))
print(add)"""

"""x=[2,3,4] #7
y=[5,6,7]
power=list(map(lambda x,y: x**y,x,y))
print(power)"""

#filter
"""word=["likitha","jack","gill","elena"] #1
starts=list(filter(lambda x:x.startswith("j"),word))
print(starts)"""

"""n=[2,1,3,6,4,8,5,9,7] #2
even=list(filter(lambda x:x%2==0,n))
print(even)"""

"""words=["sri","sai","likitha","saroja","elena"]  #3
length=list(filter(lambda x: len(x)>4,words))
print(length)"""

"""n=[2,1,3,6,4,8,5,9,7,3,3,5,3,3]  #4
count=list(filter(lambda x: x==3,n))
print(count)"""

"""n=[2,1,3,6,4,8,5,9,7]
power=list(filter(lambda x:x>3,n))
print(power)"""

#reduce 
"""from functools import reduce #1
def sum(n,y):
    return n+y
n=[2,1,3,6,4,8,5,9,7] 
sum=reduce(sum,n)
print(sum)"""


"""from functools import reduce #2
def mul(n,y):
    return n*y
n=[2,1,3,6,4,8,5,9,7] 
mul=reduce(mul,n)
print(mul)"""


"""from functools import reduce #3
word=["likitha"," ","hi"," ","!"] 
conactenate=reduce(lambda x,y: x+y,word)
print(conactenate)"""

"""from functools import reduce #4
num=[2,5,9,3,7,5]
greater=reduce(lambda x,y: x if x>y else y,num)
print(greater)"""

"""from functools import reduce #5
def add(x,y):
    return x+y
n=[8,9,4,2,7,5,5]
add=reduce(add,n)
print(add)"""



