# 함수

# def Test_Open_Account(): # 정의
#     print("새로운 계좌가 생성되었습니다.")
  
# Test_Open_Account() # 사용

# def Test_Account_Deposit(Balance:int, Money:int): # 인자
#     print(f"입금이 완료되었습니다. 잔액은 {Balance+Money}원 입니다.")
#     return Balance+Money # 반환
  
# money = Test_Account_Deposit(20000,1000)
# print(money)

# def Test_return(money):
#     commission = money / 0.1 if 5000 > money else 500
#     return commission,money

# from random import *

# commission,money = Test_return(randrange(1,21) * 500)
# print(f"수수료 : {commission}\n출금액 : {money}")

# 기본값

# def profile(name:str, age:int = 17, main_lang:str = "파이썬") :
#     print(f"이름 : {name}\t나이 : {age}\t주 사용 언어 : {main_lang}")

# profile("유재석",20,"파이썬") # 일반적
# profile("김태호")
# profile("강호동")

# 키워드 이용 함수 호출 # 동일한 값이 가능

# def profile(name:str, age:int,main_lang:str):
#     print(name,age,main_lang)
# profile(name="유재석",main_lang="파이썬",age=20)
# profile(age=30,main_lang="자바",name="강호동")

# 가변인자

# 일반적인 방법 :
# def numbering(num1:int,num2:int,num3:int):
#    print(f"{num1:3},{num2:3},{num3:3}",end="     ")
# def numbering(*num:int):
#     len = 1
#     for count in num:
#       print(f"{count :3}",end=" ")
#       len
#     print("")

# numbering(50,20,10)
# numbering(10,20)

# 지역변수 전역변수

# gun = 10

# def checkpoint(soldiers): # 경계근무
#     global gun # 전역 공간에 있는(위에 있는) gun 을 사용할 수 있음
#     gun = gun - soldiers # 오류 -> 여기서 사용하는 것은 지역에서만 사용 가능한 gun임!
#                          #         이전에 사용할 수 있는 변수를 따로 만들어줘야함
#     print("함수 내 남은 총 {0}".format(gun))

# def checkpoint_return(gun, soldiers): # 가장 이상적인 방법? 전역변수는 가급적 적게 쓰는게 좋음
#     gun = gun - soldiers
#     print(f"함수 내 남은 총 : {gun}")
#     return gun

# print(f"전체 총 : {gun}")
# checkpoint(2) # 2명이 근무를 나감
# print(f"전체 총 : {gun}")
# gun = checkpoint_return(gun,2) # 2명 복귀
# print(f"전체 총 : {gun}")

# 문제 : 표준체중
# 남 : 키(m)X 키(m) X 22
# 여 : 키(m)X 키(m) X 21
# 함수명 : std_weight(height,sex)
# 표준 체중은 소수점 둘재자리까지

def std_seight(height:int,sex:str):
    if sex == "남":
        print(f"남성 키 {height}cm에 따른 표준 체중 : {height * 0.01 * height * 0.01 * 21:.2f}kg")
    elif sex == "여":
        print(f"여성 키 {height}cm에 따른 표준 체중 : {height * 0.01 * height * 0.01 * 21:.2f}kg")
# 소수점 표현방식
# 1. round(수,자리수)
# 2. 포멧팅 :.2f (두자리 수까지)

std_seight(177,"남")
std_seight(152,"여")
std_seight(162,"남")