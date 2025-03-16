from datetime import datetime

def calculate_age():
    try:
        birth_date_str = input("Enter your birthdate (DD/MM/YYYY): ")
        birth_date = datetime.strptime(birth_date_str, "%d/%m/%Y")
        current_date = datetime(2025, 3, 16)  # Fixed date for task requirement

        if birth_date > current_date:
            print("Invalid birthdate! You haven't been born yet. 🚨")
            return

        age_years = current_date.year - birth_date.year
        if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
            age_years -= 1  # Adjust age if birthday hasn't occurred yet

        print(f"You are {age_years} years old. 🎉")

        years_until_100 = 100 - age_years
        if years_until_100 > 0:
            print(f"You will turn 100 in {years_until_100} years. 🎂")
        else:
            print("Wow! You are 100 years old or older! 🎊")

    except ValueError:
        print("Invalid input! Please enter a valid birthdate in DD/MM/YYYY format.")

calculate_age()
