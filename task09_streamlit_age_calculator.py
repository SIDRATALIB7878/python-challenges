import streamlit as st
from datetime import datetime, timedelta

# Fixed current date as per the task requirement
CURRENT_DATE = datetime(2025, 3, 13, 0, 0, 0)  # Includes hours, minutes, seconds

def calculate_age(birth_date):
    # Convert date to datetime (set time to midnight)
    birth_date = datetime.combine(birth_date, datetime.min.time())

    if birth_date > CURRENT_DATE:
        return "Invalid birthdate! You haven't been born yet. 🚨", None, None, None, None, None
    
    age_years = CURRENT_DATE.year - birth_date.year
    if (CURRENT_DATE.month, CURRENT_DATE.day) < (birth_date.month, birth_date.day):
        age_years -= 1  # Adjust age if birthday hasn't occurred yet

    # Calculate exact time difference
    time_difference = CURRENT_DATE - birth_date
    age_days = time_difference.days
    age_hours = age_days * 24
    age_minutes = age_hours * 60
    age_seconds = age_minutes * 60

    years_until_100 = 100 - age_years
    return f"You are {age_years} years old. 🎉", age_days, age_hours, age_minutes, age_seconds, years_until_100

# Streamlit UI
st.title("🎂 Enhanced Age Calculator 📅")
st.write("Enter your birthdate to calculate your exact age with days, hours, minutes, and seconds!")

birth_date_input = st.date_input("Select your birthdate:", min_value=datetime(1900, 1, 1).date(), max_value=CURRENT_DATE.date())

if st.button("Calculate Age"):
    age_message, age_days, age_hours, age_minutes, age_seconds, years_until_100 = calculate_age(birth_date_input)
    
    st.success(age_message)
    st.write(f"🗓️ You have lived **{age_days:,} days**.")
    st.write(f"⏳ That’s **{age_hours:,} hours**.")
    st.write(f"⏰ Which is **{age_minutes:,} minutes**.")
    st.write(f"⏲️ And **{age_seconds:,} seconds**.")

    if years_until_100 is not None:
        if years_until_100 > 0:
            st.info(f"🎯 You will turn **100** in **{years_until_100} years**.")
        else:
            st.warning("Wow! 🎊 You are 100 years old or older!")

