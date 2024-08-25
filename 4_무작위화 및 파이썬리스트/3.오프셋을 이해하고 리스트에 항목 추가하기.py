a = 3
b = "hello"
# 변수 하나에 하나의 데이터 저장

fruits = ["apple", "banana", "cherry", "kiwi"]

print(fruits[0]) # apple, 0부터 시작 순차적으로
print(fruits[-1]) # kiwi, 음수는 역순으로

fruits[0] = "mango" # mango, 특정 인덱스의 데이터를 재할당 가능
print(fruits[0])

fruits.append("orange")
print(fruits[-1]) # orange, append 함수는 맨 뒤에 추가

fruits.extend(["a", "b", "c"])
print(fruits) # extend 함수로 뒤에 데이터 추가 이 때 매개변수는 배열로 전달

