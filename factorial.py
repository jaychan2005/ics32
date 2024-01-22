
def factorial(n):
    if n == 0:
        return 0        
    elif n == 1: #1) The base case
        return 1
    elif n < 0:
        raise TypeError("Number must be positive!")
    else: #2) The recursive case
        return n * factorial(n-1)
    
if __name__ == '__main__':
    try:
        value = factorial(-1)
    except TypeError as e:
        print(e)
    else:
        print(value)