# 표준 입출력

# print("Python", "Java", sep=",") # 빈 공간을 어떤식으로 처리할지에 대한 방법 (여러 문자열 등에 쓰기 가능)
# print("Python", "Java", sep=",",end="?\n") # 마지막을 어떤식으로 처리할지에 대한 방법

# import sys
# print("메시지",file=sys.stdout) # 표준출력
# print("메시지",file=sys.stderr) # 에러출력
# # 위의 코드는 vscode 에서는 아무런 이상 없이 출력이 되나 환경에 따라서 에러를 출력해야할 경우에 의미있는 동작을 한다.

# scores = {"수학":10,"영어":20,"코딩":50}
# for subject,score in scores.items():
#     print(subject.ljust(3),str(score).rjust(3),sep=":")

# for num in range(1,21):
#     print("대기번호 : "+str(num).zfill(3)) # 빈공간 0으로 채워줘

# answer = input("아무 숫자 입력 : ") # 이런식으로 입력을 받으면 항상 문자열 형식으로 값을 얻게됨
# print(f"입력한 값은 {answer} 입니다.")
