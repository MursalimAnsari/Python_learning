
# print the numbers in row
"""
  * * * *
  * * *
  * *
  *
"""

n = int(input("enter number of rows: "))


for i in range(1, n+1):
    # for j in range(1, n-i+2)
    for j in range(i,n+1):   
        print('*', end='')
    print()    