def safe_addition():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 + num2
            print(f"The sum of {num1} and {num2} is {result:.2f}")
        except ValueError:
            print("Oops! That doesn't look like a valid number. Please try again.")
            continue

        another_calculation = input("Do you want to perform another addition? (yes/no): ").lower()
        if another_calculation != "yes":
            print("Thank you for using our friendly calculator. Have a great day!")
            break

safe_addition()
