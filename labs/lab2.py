#lab2.py

# Starter code for lab 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.
# Please see the README in this repository for the requirements of this lab exercise

# Jay Chan
# jayc10@uci.edu
# 54907952

def add(a, b):
    return  a + b

def sub(a, b):
    return  a - b

def div(a, b):
    return  a / b

def mul(a, b):
    return  a * b

def run():
    a = input("Enter left operand: ")
    b = input("Enter right operand: ")
    operator = input("What type of calculation would you like to perform (+, -, x, /)? ")
    
    r = 0

    if operator == "+":
        try:
            r = add(int(a),int(b))
        except:
            r = "ValueError, values must be integers."
            
    elif operator == "-":
        try:
            r = sub(int(a),int(b))
        except:
            r = "ValueError, values must be integers."
    elif operator == "x":
        try:
            r = mul(int(a),int(b))
        except:
            r = "ValueError, values must be integers."
    elif operator == "/":
        try:
            r = div(int(a),int(b))
        except ZeroDivisionError:
            r = "ZeroDivisionError, cannot divide by zero."
        except ValueError:
            r = "ValueError, values must be integers."
    else:
        r = "Unable to perform the desired calculation, please try again."
    
    print(r)
    
    if input("Run another calculation (y/n)? ") == "y":
        run()


if __name__ == "__main__":
    print("Welcome to PyCalc!")
    run()
