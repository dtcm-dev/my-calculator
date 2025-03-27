import operations

def main():
    print("Welcome to the Dorxata Calculator!")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
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
            print("Multiplication feature not implemented yet.")
        elif choice == 4:
            # Division function will be implemented in a feature branch
            print("Division feature not implemented yet.")
        else:
            print("Invalid operation number.")

if __name__ == "__main__":
    main()