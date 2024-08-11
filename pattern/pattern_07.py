# print the numbers in row
"""
      *
    * * *
  * * * * *
* * * * * * *
"""

n = int(input("enter number of rows: "))


for i in range(n):
    for j in range(i, n):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    for j in range(i+1):
        print('*', end='')        
    print()    