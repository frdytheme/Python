print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
peoples = int(input("How many people to split the bill?"))
tips = bill / 100 * percentage
pay = (bill + tips) / peoples
result = round(pay, 2)
result = "{:.2f}".format(pay) # 형식 함수를 이용해 소수점 두 번째 자리까지 나오게 처리.
print(f"Each person should pay: ${result}")

# 총 금액과 팁 비율을 입력 받아 팁 금액을 포함한 총 금액 계산
# 인원수에 따라 총 금액 나누기 후 두 번째 자리까지 반올림 후 반환.
