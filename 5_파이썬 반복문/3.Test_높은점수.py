student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

highest_score = 0

for score in student_scores:
  if score > highest_score:
    highest_score = score

print(f"가장 높은 점수는 {highest_score}입니다.")