# Get weight and height from user
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

# Calculate BMI
bmi = weight / (height ** 2)

# Determine the category
if bmi < 18.5:
    print("Underweight")
elif bmi < 24.9:
    print("Normal weight")
elif bmi < 29.9:
    print("Overweight")
else:
    print("Obesity")
