# Iterative 

# def fib(n):
#     if n<0:
#         print("numers are negative")

#     if n <= 1:
#         print(n)

#     a,b=0,1
#     print(a, end=' ')
#     for _ in range(2,n+1):
#      print(b, end=' ')
#      c = a+b
#      a=b
#      b=c
#      print(end=' ')   


# fib(15)     


# Recursive

# def fib(n):
#     if n<=0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)


# def printFib(n, current=0):
#     if current<n:
#         print(fib(current), end=' ')
#         printFib(n,current+1)
#     else:
#         print(end=' ')    

# printFib(15)