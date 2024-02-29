try:
    age = int(input('What is your age: '))
    weight = float(input("What is your weight in Kilogram?: "))
    height = float(input("What's your height in meters?: "))

    if age < 18:
        print("You are less than 18, your BMI can't be calculated")
    else:
        bmi = weight / (height * height)
        if bmi < 18.5:
            print("You are Underweight")
        elif bmi >= 18.5 and bmi <= 24.9:
            print("You have a normal weight")
        elif bmi >= 25 and bmi <= 29.9:
            print("You are overweight")
        elif bmi >= 30.0:
            print("You are obese")
except ValueError:
    print('Try again, you entered an inaccurate value')
