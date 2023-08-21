# 여러 모듈을 모아놓은 집합체

# travel 폴더
#    __init__.py
#    thailand.py
#    vietnam.py


# thailend.py

class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕,파타야 여행")

if __name__ == "__main__": # 모듈 확인용으로 사용 할 수 있는 직접 모듈 실행법
    print("Thailand 모듈 직접 실행")
    print("이 문장은 모듈을 직접 실행할 대만 실행됩니다.")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("Thailand 외부에서 모듈 호출")

#  vietnam.py
class VietnamPackage:
    def detail(self):
        print("[베트남 패키지 3박 5일] 다낭 효도 여행")


#패키지 자체를 쓰는 파일

# import travel.thailand # 클래스나 함수는 직접 임포트가 불가능함 파일을 불러오게끔만 가능함 
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage # 이런식으로도 가능
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam # 이것도 가
# trip_to = vietanm.VietnamPackage()
# trip_to.detail()

from travel import * # 이 별은 travel이라는 폴더 내에서 모든 것을 가져온다는 말인데
trip_to = vietnam.VietnamPackage() # 기본적으로는 안됨
# 이유 : 원한는건 공개로 원하지 않는 것은 비공개로 -> __init__.py 에서 바꿔줘야함

# __init__.py 
__all__=["vietnam","thailand"] # 특정 모듈만 공개 할 수 있음 -> 이렇게 하면 위쪽 구문이 사용이 가능해짐


# 패키지, 모듈의 위치를 알 수 있는 방법

import inspect
import random
print(inspect.getfile(random)) # 이렇게 하면 random 이라는 패키지가 어디있는지 알 수 있다. 파이선 라이브러리에 옯겨놔도 경로를 찾을 수 있다면 어디서든 쓸 수 있다는 이야기가 된다.