weight = float(input("Введите свой вес в килограммах: "))
height = float(input("Введите свой рост в метрах: "))

bmi = round((weight / (height**2)), 1)

if bmi < 18.5:
    print(f"Ваш BMI: {bmi} (Недостаточный вес)")
elif bmi <= 24.9:
    print(f"Ваш BMI: {bmi} (Норма) ")
elif bmi <= 29.9:
    print(f"Ваш BMI: {bmi} (Избыточный вес)")
elif bmi >= 30:
    print(f"Ваш BMI: {bmi} (Ожирение)")
