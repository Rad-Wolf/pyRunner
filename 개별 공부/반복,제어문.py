# if

# weather = input("오늘 날씨는 어때요?")
# if weather =="비":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물이 필요 없어요")

# for

# temp = 0
# for day in range(1,5):
#     temp = int(input(f"{day}일차 기온은 어때요? "))
#     if 30 <= temp :
#         print("쪄죽을 수 있어요. 조심하세요")
#     elif 20 <= temp :
#         print("돌아다니기 좋은 날씨에요")
#     elif 0 <= temp :
#         print("쌀쌀 하네요 외투나 겉옷을 챙기세요")
#     else:
#         print("이불 밖은 위험 할 수 있어요 따듯한 곳을 찾으세요")


# while

# customer = "토르"
# index = 5
# while index >= 1:
#     print(f"{customer}님, 커피가 준비되었습니다.")
#     index -= 1
#     if index == 0:
#         print(f"{customer}님의 커피는 폐기 됩니다.")

# continu, brack

# absent = [2,5] # 결석한 번호
# no_book = [7] # 책이 없음
# for student in range(1,11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print(f"오늘 수업은 여기까지. {student}은(는) 교무시로 따라와!")
#         break
#     print(f"{student}, 책 읽어봐")

# 한줄로 끝내는 for문

# 출석번호가 1,2,3,4..... 앞에 100을 붙이기로 함
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# students = ["아이언맨","토르","그루트"]
# students = [len(i) for i in students]
# print(students)

# 문제

# 50명의 승객과 매칭
# 승객은 5분 ~ 50분 사이의 난수 -> 소요시간
# 15분 미만의 승객만 매칭해야함
# 탑승한 승객의 수를 구하라

# 개인 답
# import random
# count = 0
# total_time = 0

# for customer in range(50):
#     time = random.randrange(5,50)
#     if time >= 15 :
#         print(f"[ ] {customer+1:2}번째 손님 (소요시간 : {time:2})")
#     else:
#         print(f"[O] {customer+1:2}번째 손님 (소요시간 : {time:2})")
#         count += 1
#         total_time += time
# print(f"{count}명의 승객 탑승, 총 소요시간 {time}분")

# 지은이 답

from random import * # 이렇게 하면 타자 수를 줄일 수 있음 전부 불러옴
cnt = 0
for i in range(1,51):
    time = randrange(5,51) # 5 ~ 50
    if 5 <= time <= 15: # 5 ~ 15 분 이내의 손님
        print(print(f"[O] {i:2}번째 손님 (소요시간 : {time:2})"))
        cnt += 1 # 탑승 승객 증가
    else:
        print(print(f"[ ] {i:2}번째 손님 (소요시간 : {time:2})"))

print(f"총 탑승 승객 수 :{cnt}")