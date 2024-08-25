target = int(input("Enter a number between 0 and 100: "))

if target < 0 or target > 100:
  print("!!! Wrong number please enter between 0 and 100")
else:  
  total = 0
  for num in range(2, target+1, 2):
    total += num

  print(total)