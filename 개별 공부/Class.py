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

# 상속

# 일반 유닛
# class Unit:
#     def __init__(self,name,hp):
#         self.name = name
#         self.hp = hp

# 공격 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp,damage):
#         Unit.__init__(self,name,hp) # 이런식으로 초기화가 가능
#         # super().__init__(name, hp) # 자동생성
#         self.damage = damage

# 다중 상속

# class Unit:
#     def __init__(self,name,hp):
#         self.name = name
#         self.hp = hp

# class Flayable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
    
#     def fly(self,name,location):
#         print(f"{name} : {location} 방향으로 날아갑니다. {self.flying_speed}")

# class FlyableUnit(Unit,Flayable):
#     def __init__ (self, name, hp, flying_speed):
#         Unit.__init__(self,name,hp)
#         Flayable.__init__(self,flying_speed)

# pass super

# class Unit:
#     def __init__(self,name,hp):
#         self.name = name
#         self.hp = hp
#     def Move(self,location):
#         print("[유닛 이동]")

# class GraundUnit(Unit):
#     def __init__(self,name,hp,move_speed):
#         Unit.__init__(self,name,hp)
#         self.move_speed = move_speed
#     def Move(self,location):
#         Unit.Move(self,location)
#         print(f"{self.name} : {location} 방향으로 지상 이동")

# class FlyableUnit(Unit):
#     def __init__ (self,name,hp,Flying_speed):
#         Unit.__init__(self,name,hp)
#         self.Flying_speed
#     def Move(self,location):
#         Unit.Move(self,location)
#         print(f"{self.name} : {location} 방향으로 공중 이동")

# # pass
# class building_Uni(Unit):
#     def __init__(self,name,hp,location):
#         pass # 우선 넘어감 -> 매서드를 바로 return 시킴?
#     def Move(self,location):
#         super().move(location) # Unit 대신 super로 바꿧는데 상위 클래스의 메서드 등을 쓸 수 있게 함
#         print("super()") # 다중상속의 경우 super를 썼다면? : 마지막에 써있는 상속 클레스를 의미하게 됨 # 다중 상속시 명시를 하는게 좋다.
        
# 퀴즈 주어진 코드를 사용하여 부동산 프로그램을 작성하시오.

# 3개의 매물 
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

#[코드]
# class House:
#     # 매물 초기화
#     def __init__(self,location,house_type,deal_type,price,completion_year):
#         pass
#     # 매물 정보 표시
#     def show_detail(self):
#         pass

class House:
    def __init__(self,location,house_type,deal_type,price,completion_year):
        self.location : str = location
        self.house_type : str = house_type
        self.deal_type : str = deal_type
        self.price : str = price
        self.completion_year : str = completion_year
        print("매물 등록 완료")

    def show_detail(self):
        string = self.deal_type.ljust(6)+"\n"+ \
                 "[위치 : " + self.location.rjust(10) + "] [주거형태 : " + self.house_type.rjust(5)+"] [가격 : " + self.price.rjust(10) + "] [준공년도 : " + self.completion_year.rjust(5)+"]"
        print(string)

houses = []
houses.append(House("강남","아파트","매매","10억","2010년"))
houses.append(House("마포","오피스텔","전세","5억","2007년"))
houses.append(House("송파","빌라","월세","500/50","2000년"))

print(f"총 {str(len(houses)).rjust(3)}대의 매물이 있습니다.")
for house in houses:
    house.show_detail()
