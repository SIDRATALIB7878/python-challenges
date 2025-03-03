while True:
    try:
        num = input("Enter a number (or type 'exit' to quit): ")
        
        if num.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break  # Exit the loop properly

        num = int(num)  # Convert input to integer

        if num % 2 == 0:
            print(num, "is an even number")
        else:
            print(num, "is an odd number")

    except ValueError:
        print("Invalid Input! Please enter a valid number.")
