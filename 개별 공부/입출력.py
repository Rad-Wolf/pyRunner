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

# 출력 포멧

# 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# teststr = "I win"
# print(f"{teststr: >10}")

# 양수일 때는 + 표시, 음수일 때는 - 표시
# print(f"{-500: >+10}") 
# print(f"{+500: >+10}") # 반드시 + 표시

# 왼쪽 정렬, 빈칸 _로 채움
# print(f"{-500:_<10}")

# 3자리 콤마
# print(f"{1000000000:,} $") # 10억
# print(f"{1000000000:+,}") # 부호
# print(f"{1000000000: >+30,}") # -> 포멧에는 순서가 있음

# 소수점
# print(f"{100000.123:f}") # 기본 6자리
# print(f"{10.123:.1f}") # 자리수 지정 -> 기본적인 코드방식 때문에 이상한 값이 나올 수는 있음 (프로그래밍 소수에 대한 이해 필요)

# 파일 입출력

# 파일의 위치는 상대적이며 절대값으로 바꿀 수도 있다.
# score_file = open("score.txt","a",encoding="utf8") # w 덮어쓰기 a 추가기입 등등

# print("수학 : 50",file=score_file)
# print("영어 : 50",file=score_file,end="")

# score_file.write("가나다라마바사아\n\n방식은 이렇다")

# score_file.close()

# load_file = open("loader.txt","r",encoding="utf8")
#print(load_file.read()) # 전체 읽기 -> readline 등은 알아서 해볼것 + print는 자동으로 줄바꿈 한다는 것을 기억

# while True: # 반복문을 이용한 모르는 데이터 불러오기 1
#     line = load_file.readline()
#     if not line : break
#     print(line,end="")

# lines = load_file.readlines() # 반복문을 이용한 모르는 데이터 불러오기 2
# for line in lines: print(line,end="")

# load_file.close();

# pickle 피클 라이브러리

import pickle

# 쓰기
# profile_file = open("profile.pickle","wb") # 파일 생성  b : 바이너리

# profile = {"이름":"남씨","나이":31,"취미":["코딩","골프"]}

# print(profile) # 단순 출력
# pickle.dump(profile,profile_file) #profile에 있는 정보를 file에 저장

# profile_file.close()

# 읽기
profile_file = open("profile.pickle","rb")

profile = pickle.load(profile_file) # 파일 내부 정보를 객체에 저장
print(profile)

profile_file.close()