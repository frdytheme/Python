print("보물섬 프로젝트에 오신 걸 환영합니다. 여행을 떠나보세요")
choose = input("왼쪽 / 오른쪽? ")
if choose == "왼쪽":
  choose = input("수영하기 / 기다리기? ")
  if choose == "기다리기":
    choose = input("어느 문으로? 빨강 / 노랑 / 파랑? ")
    if choose == "노랑":
      print("축하합니다 보물을 발견했습니다!")
    else:
      print("게임 오버")
  else:
    print("게임 오버")
else:
  print("게임 오버")