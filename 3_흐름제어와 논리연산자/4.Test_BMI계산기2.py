height = float(input("what is your height"))
weight = int(input("what is your weight"))

bmi = round(weight / (height / 100) ** 2, 1)
state = ""
if bmi < 18.5:
  state = "underweight"
elif bmi < 25:
    state = "normal weight"
elif bmi < 30:
        state = "slightly overweight"
elif bmi < 35:
      state = "obese"
else:
      state = "clinically obese"


print(f"Your BMI is {bmi}, you are {state}")