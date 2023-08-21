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

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("숫자 입력 :"))
    num2 = int(input("숫자 입력 :"))
    
    if num1 >= 10 or num2 >= 10:
        raise ValueError # 강제 에러 발생
    
    print(f"{num1} / {num2} = {int(num1/num2)}")
except ValueError:
    print("잘못된 값을 입력하였습니다.")