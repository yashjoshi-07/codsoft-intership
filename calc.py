def calculator():
    while True:
        print("/n-------CALCULATOR--------")
        print("1. ADDITION")
        print("2. SUBTRACTOIN")
        print("3. DIVISION")
        print("4. MULTIPLICATION")
        print("5. FLOOR DIVISION")
        print("6. EXIT")

        choice = input("Enter your choice(1-6):")
        if choice == '6':
            break
        try:
            a = float(input("Enter first number:"))
            b = float(input("Enter second number:"))
            if choice == '1':
                print(a+b)
            elif choice == '2':
                print(a-b)
            elif choice == '3':
                if b != 0:
                    print(a/b)
                else: 
                    print("division by 0")
            elif choice == '4':
                print(a*b)
            elif choice == '5':
                if b != 0:
                    print(a//b)
                else: 
                    print("division by 0")

        except ValueError:
            print("Invalid Input")
calculator()



