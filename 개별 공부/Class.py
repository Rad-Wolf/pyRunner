# 1. 기초사옹법

# 기존 코드 = 개별 변수 -> 이름만 다른 캐릭터를 만드려면 변수의 이름들이 중복될 경우 복잡한 변수이름이 됨
# name = "마린"
# hitpoint = 40
# damage = 5
# ...
# gost_name = "고스트"
# gost_hitpoint = 60
# gost_damage = 8
# 하나만 있다면 상관이 없지만 무수히 많은 변수들이 만들어질 수 있는 이상한 코드가 될 것이다.

# class Unit:
#     # 생성자
#     def __init__(self,name,hitpoint,damage):
#         self.name=name # 맴버 변수 1 => 들어온 인자와 다른 이름이어도 상관은 없음. 기본 public?
#         self.hitpoint=hitpoint
#         self.damage=damage
#         print("유닛이 생성되었습니다.")
#         print(f"이름 {self.name} 체력 {self.hitpoint} 공력력 {self.damage}")

#     def Attack(self, location): # 일반 매서드
#         print(f"{self.name} : {location} 방향으로 공격을 합니다. 데미지 {self.damage}")

# marine = Unit("마린",40,5)
# marine.Attack("3시")
# gost = Unit("고스트",60,8)
# gost.clocking = True # 클래스 외부에서 추가 확장이 가능함. 이것만 바뀜!
# gost.Attack("1시")