# theater_module.py

# 일반 가격
# def price(people):
#     print(f"{people}명 가격은 {people*10000}원 입니다.")
# def price_morning(people):
#     print(f"{people}명 조조 할인 가격은 {people*6000}원 입니다.")
# def price_soldier(people):
#     print(f"{people}명 군인 할인 가격은 {people*5000}원 입니다.")

# 다른 py파일에서 사용할때
# 같은 경로에 있거나 파이썬 라이브러리들이 모여있는 패키지에서 가능

# 1번
# import theater_module # 풀네임으로 불러와야함
# theater_module.price(3)
# theater_module.price_morning(3)
# theater_module.price_soldier(3)

# 2번
# import theater_module as mv # 애칭 부여
# mv.price(3)
# mv.price_morning(3)
# mv.price_soldier(3)

# 3번
# import theater_module import * # 그냥 쓸 수 있게
# price(3)
# price_morning(3)
# price_soldier(3)

# 4번
# import theater_module import price,price_morning # 특수한 메서드만 쓸 수 있게
# price(3)
# price_morning(3)
# price_soldier(3) # 이놈은 못불러옴

# 5번
import theater_module import price_soldier as price # 특수한 메서드를 이름만 바꿔서 사용이 가능
price(3)
# 이런식으로 사용이 가능해진다.