try:
    print("나누기")
    num1 = int(input("나눌값 : "))
    num2 = int(input("나누는 값 : "))
    print(f"{num1}/{num2} = {int(num1/num2)}")
except ValueError:
    print("잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err: # 변수로 나오게 할 수도 있음
    print(f"{err} 0 에러")
except :
    print("알 수 없는 에러가 발생했습니다.")
# 등등등의 에러를 표시할 수 있다.