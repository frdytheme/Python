height = input("What is your height?")
weight = input("What is your weight")

num_height = int(height) / 100
num_weight = int(weight)

bmi = num_weight / num_height ** 2
new_bmi = int(bmi)

print("your BMI is " + str(new_bmi))

# input의 값을 정수로 바꾸고 cm 단위를 m로 바꾸기 위해 100 나누기
# bmi 계산 수식 넣고 int로 정수 변환 후 str로 문자열과 더해서 출력
