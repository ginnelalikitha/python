#local variable-can only accessed inside a specific block of code or a function
def greet():
    n="hello,world!" #local variable
    print(n)
greet() 

#global variable-can be accesssed inside  and outside the function
n="hello,world"
def greet():
    print(n)
greet()   
print(n) 