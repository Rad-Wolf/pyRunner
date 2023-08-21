# try:
#     print("나누기")
#     num1 = int(input("나눌값 : "))
#     num2 = int(input("나누는 값 : "))
#     print(f"{num1}/{num2} = {int(num1/num2)}")
# except ValueError:
#     print("잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err: # 변수로 나오게 할 수도 있음
#     print(f"{err} 0 에러")
# except :
#     print("알 수 없는 에러가 발생했습니다.") # 나머지 예외들
# except Exception as err:
#     print(f"{알 수 없는 에러가 발생했습니다. {err}}") # 나머지 예외를 이런식으로도 가능
# # 등등등의 에러를 표시할 수 있다.

# 의도적 에러 발생

# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("숫자 입력 :"))
#     num2 = int(input("숫자 입력 :"))
    
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError # 강제 에러 발생
    
#     print(f"{num1} / {num2} = {int(num1/num2)}")
# except ValueError:
#     print("잘못된 값을 입력하였습니다.")

# 사용자 정의 예외 처리

# class BigNumberError(Exception):
#     # pass # 이렇게 해서 그냥 에러만 만들 수도 있고
#     def __init__(self,msg : str) :
#         self.msg = msg
#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("숫자 입력 :"))
#     num2 = int(input("숫자 입력 :"))
    
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError(f"입력값 1 {num1}, 2 {num2}") # 강제 에러 발생
    
#     print(f"{num1} / {num2} = {int(num1/num2)}")
# except ValueError:
#     print("잘못된 값을 입력하였습니다.")
# except BigNumberError as err:
#     print("한자리 숫자만 입력해주세요.")
#     print(f"{err}")

# # 최종

# finally: # try 문이 실행되고 예외처리가 되던 말던 실행하는 마지막 구문
#     print("계산기를 이용해 주셔서 감사합니다.")

# 문제

# 치킨집
# 조건 1 : 1보다 작거나 숫자가 아닐경우 ValueError로 처리 msg : "잘못된 값을 입력하였습니다."
# 조건 2 : 총 치킨은 10마리로 한정, 치킨 소진시 SoldOutError를 발생 msg : "재고가 소진되어 더 이상 주문을 받지 않습니다."

# 제공 코드

# chicken = 10
# waiting = 1

# while(True):
#     print(f"남은 치킨 : {chicken}")
#     order = int(input("치킨을 몇 마리 주문하시겠습니까? : "))
    
#     if oder > chicken: # 주문 수량보다 현재 재고가 적을 경우
#         print("재료가 부족합니다.")
#     else:
#         print(f"[대기번호{waiting}] : {oder}마리 주문이 완료되었습니다.")
#         waiting +=1
#         chicken -= oder

# 제공 코드 끝

# 문제에 대한 강의 답

class SoldOutError(Exception):
    pass

chicken = 10
waiting = 1

while(True):
    try:
        print(f"남은 치킨 : {chicken}")
        order = int(input("치킨을 몇 마리 주문하시겠습니까? : "))
    
        if oder > chicken: # 주문 수량보다 현재 재고가 적을 경우
            print("주문보다 재료가 부족합니다.")
        elif oder <= 0:
            raise ValueError
        else:
            print(f"[대기번호{waiting}] : {oder}마리 주문이 완료되었습니다.")
            waiting +=1
            chicken -= oder
        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break




