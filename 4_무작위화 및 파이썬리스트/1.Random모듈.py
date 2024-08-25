import random
import my_module # 같은 폴더 내 다른 py를 임포트해서 모듈처럼 사용 가능

random_integer = random.randint(1, 3) # 1~3의 난수 반환
random_float = random.random()
# print(my_module.pi) # 3.14159246
print(random_float * 5) # 0~5의 소수 난수 반환



