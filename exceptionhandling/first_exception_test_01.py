
x = 10
y= 0


print("entring the values... ")

try:
    print("try executing...")
    print(x/y)
    print("not reachable")
except ZeroDivisionError as msg:
    print("exception occured", msg)
    print("except excuted")
finally:
    print("finally executed in each scenario")    


