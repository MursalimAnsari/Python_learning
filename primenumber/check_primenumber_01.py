
def is_prime(num):
   
   if num <= 1: 
      return False
   
   for i in range(2, int(num**0.5 )+1): 
      if num % i == 0:
         return False     
   return True

def check_is_prime(val):

    if is_prime(val):
       print(val, "is a prime number")
    else:
          
       print(val, "is not a prime number")

check_is_prime(41)