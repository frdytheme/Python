num = 8 / 3
print(num) # 2.6666666666666665
print(int(num)) # 2 -> 소수점 삭제
print(round(num)) # 3 -> 반올림 후 반환
print(round(num, 2)) # 2.67 -> 반올림 할 자리수 지정 가능
print(round(num, 5)) # 2.66667

new_num = 8 // 3
print(new_num) # int 변환 대신 //를 쓰면 소수점 버림.
print(type(new_num)) # int 반환.

result = 4 / 2 # 2.0
result /= 2 # 연산 후 바로 변수 대입
print(result) # 1.0

score = 0

# User scores a point
score += 1
print(score) # 1

# f-String, 문자열과 다양한 데이터 타입을 혼합할 때 유용.
print("이전에는 이렇게" + str(score) + "썼다면")

score = 0
height = 1.8
isWinnig = True

print(f"your score is {score}") # your score is 0
print(f"your height is {height}, you are winning is {isWinnig}")
# 다양한 데이터 타입을 모두 문자열과 혼합 가능. 편하다


