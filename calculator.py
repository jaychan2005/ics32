
def main():
    print("Welcome to multiplication calculator, I will multiply two integers for you!!!!")
    while True:    
        try:
            first_number = int(input("Enter first number: "))
            second_number = int(input("Enter second number: ")) 
            print("Hello World!")
            break
        except:
            print("Those aren't numbers you stupid fucking idiot\n")
            continue
    
    
if __name__ == '__main__':
    main()
