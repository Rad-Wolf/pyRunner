class Unit:
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp
    def Move(self,location):
        print("[유닛 이동]")

class GraundUnit(Unit):
    def __init__(self,name,hp,move_speed):
        Unit.__init__(self,name,hp)
        self.move_speed = move_speed
    def Move(self,location): # 재정의
        Unit.Move(self,location)
        print(f"{self.name} : {location} 방향으로 지상 이동")

class FlyableUnit(Unit):
    def __init__ (self,name,hp,Flying_speed):
        Unit.__init__(self,name,hp)
        self.Flying_speed
    def Move(self,location): # 재정의
        Unit.Move(self,location)
        print(f"{self.name} : {location} 방향으로 공중 이동")