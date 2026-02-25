#write 5 programs using loop on yield
""""def even(limit): #1
    n=0
    while n<=limit:
        yield n
        n+=2  

for num in even(20):
   print(num) """


"""def fibanocci(): #2

  a,b=0,1
  while True:
   yield a
   a,b =b,a+b
gen_object=fibanocci()
for i in range(6):
    print(next(gen_object)) """


"""def sum(a,b):  #3
    yield a+b
gen_object=sum(5,6)
print(next(gen_object))  """

"""def sub(a,b): #4
    yield a-b
gen_object=sub(8,9)
print(next(gen_object))   """

def positive(n):
    if n>0:
            print("positive")
            yield n
    else:
        print("negative")
gen_object=positive(6)
for value in gen_object:
     print(value)
