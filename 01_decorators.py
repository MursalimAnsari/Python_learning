import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result =func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper


# Decorator example 
@timer
def execute_timer(n):
    time.sleep(n)


execute_timer(2)    