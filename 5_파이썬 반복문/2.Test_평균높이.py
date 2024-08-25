student_heights = input("What is their heights?: ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n]) # 배열의 각 값을 int로 변환

avg = sum(student_heights) / len(student_heights)
print(round(avg, 2))
