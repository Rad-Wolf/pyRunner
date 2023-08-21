try:
    print("나누기")
    num1 = int(input("나눌값 : "))
    num2 = int(input("나누는 값 : "))
    print(f"{num1}/{num2} = {int(num1/num2)}")
except ValueError:
    print("잘못된 값을 입력하였습니다.")
except ZeroDivisionError:
    print("0 에러")
# 등등등의 에러를 표시할 수 있다.