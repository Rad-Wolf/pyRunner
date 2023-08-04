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