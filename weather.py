# Simple Weather Clothing Advisor

# Get temperature from user
temperature = float(input("What is the temperature in Celsius? "))

# Use if-elif-else to recommend clothing
if temperature < 10:
    print("It's cold! Wear a warm coat and scarf.")
elif 10 <= temperature <= 25:
    print("It's mild! A light jacket will do.")
else:
    print("It's hot! A T-shirt would be perfect.")
