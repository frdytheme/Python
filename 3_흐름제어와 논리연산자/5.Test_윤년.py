year = int(input("input year"))
is_leap = False
if year % 4:
  is_leap = False
else:
  if year % 100:
    if year % 400:
      is_leap = False
    else:
      is_leap = True
  else:
    is_leap = True

if is_leap:
  print("Leap")
else:
  print("Not Leap")
  