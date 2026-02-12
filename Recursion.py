# A function calling itself is called "Recursion"
#factorial
"""def factorial(n):
 if n==0 or n==1:
  return 1
 else:
  return n*factorial(n-1)
 
print(factorial(5))"""

#fibonacci series
#f(0)=0
#f(1)=1
#f(2)=f(0)+f(1)
#f(n)=f(n-1)+f(n-2)

"""def fibonacci(n):

 if n==0:
    return 0
 elif n==1:
    return 1
 else:
     return fibonacci(n-1)+fibonacci(n-2)
 

n=6
for i in range(n):
   print(fibonacci(i),end="")"""

#sum of first n natural numbers
"""5=5+4+3+2+1
n=n+sum(n-1)
5=5+sum(4)    #logic
5=5+4+sum(3)
5=5+4+3+sum(2)
5=5+4+3+2+sum(1)"""

"""def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)
    
print(sum(5))"""

#reverese a string
"""def string(n):
    if len(n)==0:
        return n
    else:
      return  n[-1] + string(n[:-1])

print(string("python"))  """

#palindrome
"""def palindrome(n):
    if len(n)<=1:
        return True
    if n[0]!=n[-1]:
        return False
    else:
        return palindrome(n[1:-1])
    
print(palindrome("mom"))"""

#binary search
"""def binary_search(arr, low, high, target):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, low, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, high, target)

arr = [1, 3, 5, 7, 9]
print(binary_search(arr, 0, len(arr)-1, 7))"""

#list sum
"""def list(n):
    if not n:
        return 0
    return n[0]+list(n[1:])
print(list([1,2,3,4])) """

a=5
b=2.5
a//=b
print(a)



