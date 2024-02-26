# lab1.py

# Starter code for lab 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.
# Please see the README in this repository for the requirements of this lab exercise

# Jay Chan
# jayc10@uci.edu
# 54907952

def calculate(x, y, z):
    if z == '+':
        return x + y
    elif z == '-':
        return x - y
    else:
        return x * y


if __name__ == '__main__':
    print('Welcome to ICS 32 PyCalc!\n')
    first = int(input('Enter your first operand: '))
    second = int(input('Enter your second operand: '))
    operator = input('Enter your desired operator (+, -, or x): ')
    print('The result of your calculation is: ' + str(calculate(first, second, operator)))
