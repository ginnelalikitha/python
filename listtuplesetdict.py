#list[]-ordered and mutable(allows duplicate values and mixed dadta types)
#tuple()-ordered and immutable
#set{}-unordered and mutable(doesn't allow duplicate values)
#dict{}-unordered and key-value pairs(doesn't allow duplicate values)


#list1
"""l=[10,20,30,40,50]
sum=0
for i in range(10,60,10):
    sum=sum+i

for i in l:
    sum=sum+i
i=0
length=len(l)
while i<length:
    sum=sum+l[i]
    i+=1
print(sum)"""

#list2
"""l=[15,2,7,25,10]
max_val=l[0]
min_val=l[0]"""

"""for i in l:
    if i>max_val:
        max_val=i
    if i<min_val:
        min_val=i
print("maximum",max_val)
print("minimum",min_val)"""

"""l.sort()
print(l[-1],l[0])"""

"""i=0
length=len(l)
while i<length:
    if l[i]>max_val:
        max_val=l[i]
    if l[i]<min_val:
        min_val=l[i]
    i+=1
print("maximum",max_val)
print("minimum",min_val)"""

#list3
"""inp=input().split(",")

l=[int(item) for item in inp]"""

"""newl=[]

for i in l:
    if i in newl:
        continue
    else:
        newl.append(i)
        print(newl)"""
"""s=set(l)
newl=list(s)
print(newl)"""

#list4

"""inp=input().split(",")

l=[int(items) for items in inp]
   
newl=[]
c=0
for i in l:
    if i==2:
     c+=1
    else:
       continue

print(c)


n=int(input())
c=l.count(n)
print(c)"""

#set1
"""set1={1,2,3,4,5}
set2={4,5,6,7,8}"""
"""n=set1.union(set2)
print(n)"""

"""int=set1.intersection(set2)
print(int)
print(set1|set2)"""

#dict
"""my_dict={"name":"likitha","age":21,"status":"fresher"}"""

"""my_dict["name"]="swaroop"
print(my_dict["name"])"""

"""for i,j in my_dict.items():
    print(i,j)"""

"""my_dict={}
name=input("enter:")
age=int(input("age:"))
city=input("city:")
 
my_dict["name"]=name 
my_dict["age"]=age 
my_dict["city"]=city


print(my_dict)"""


#methods in list
"""fruits=["apple","banana","orange","pear","orange"]
fruits.index("banana")
print(fruits)"""

#concatenation in list
"""l1=[1,2,3,4]
l2=[5,6,7,8]
l=l1+l2
print(l)"""

#list comprehension
"""new_list=[x for x in i]
i=input
x=expression"""


      





