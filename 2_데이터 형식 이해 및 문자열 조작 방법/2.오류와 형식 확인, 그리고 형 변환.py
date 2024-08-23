# num_char = len(input("What is your name?"))
# print("Your name has " + num_char + " characters.")

# len은 int 형식이기 때문에 문자열과 + 연산이 안 되어 오류.

# print(type(num_char))

# type으로 데이터 타입을 확인하면 int 형식

# new_num_char = str(num_char)

# print("Your name has " + new_num_char + " characters.")

# str함수를 사용해 데이터 형 변환 후 출력하면 정상 작동

# a = 123
# print(type(a))

# str, int, float으로 형 변환 가능

print(70 + float("100.5")) # 170.5
print(str(70) + str(100)) # 70100