import operations

def main():
    print("Welcome to the Dorxata Calculator!")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Square Root (√)")
    print("7. Modulo (%)")
    print("8. Average (avg)")
    print("9. Maximum (max)")
    print("10. Minimum (min)")
    # More operations will be added by team members
    
    while True:
        choice = input("\nEnter operation number (or 'q' to quit): ")
        
        if choice.lower() == 'q':
            print("Thank you for using the Dorxata Calculator!")
            break
            
        choice = int(choice)
            
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == 1:
            # Addition function will be implemented in a feature branch
            print(f"{num1} + {num2} = {operations.add(num1, num2)}")
        elif choice == 2:
            # Subtraction function will be implemented in a feature branch
             print(f"{num1} - {num2} = {operations.subtract(num1, num2)}")
        elif choice == 3:
            # Multiplication function will be implemented in a feature branch
            print(f"{num1} * {num2} = {operations.multiply(num1, num2)}")
        elif choice == 4:
            # Division function will be implemented in a feature branch
            print(f"{num1} / {num2} = {operations.divide(num1, num2)}")
        elif choice == 5:
            # Power function will be implemented in a feature branch
            print(f"{num1} ^ {num2} = {operations.power(num1, num2)}")
        elif choice == 6:
            # Square Root function will be implemented in a feature branch
            print(f"Square Root of {num1} is {operations.sqrt(num1)}")
        elif choice == 7:
            # Modulo function will be implemented in a feature branch
            print(f"{num1} % {num2} = {operations.modulo(num1, num2)}")
        elif choice == 8:
            # Average function will be implemented in a feature branch
            print(f"Average of {num1} and {num2} is {operations.average(num1, num2)}")
        elif choice == 9:
            # Maximum function will be implemented in a feature branch
            print(f"Maximum of {num1} and {num2} is {operations.maximum(num1, num2)}")
        elif choice == 10:
            # Minimum function will be implemented in a feature branch
            print(f"Minimum of {num1} and {num2} is {operations.minimum(num1, num2)}")
        else:
            print("Invalid operation number.")

if __name__ == "__main__":
    main()