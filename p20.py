weight = float(input("Enter weight in kg: "))
height_cm = float(input("Enter height in cm: "))

height_m = height_cm / 100
bmi = round(weight / (height_m ** 2), 1)

print("BMI:", bmi)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")