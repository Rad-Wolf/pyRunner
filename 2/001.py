print("I eat %d apples" % 5) # 이런식으로 하면 문자열에서 숫자만 바꾸는 것도 가능하다.

a = 50

print("I eat %d apples" % a)

a = "기다려!"

# 문자열 위지 보간방법
print("%10s" % a) # 10칸 우측기준
print("%-10s" % a) # 10칸 좌측 기준
print("%10s %-10s" % a % a) # 2개의 문자열은 이런식으로 -> 안쓰기는 하는데 이것을 소수점에서도 적용이 가능하다. 문자열을 이쁘게 만듬

# 포멧팅 방법

a = "I eat {0} apples".format(10)
a = "I eat {0} apples. {1}".format(10,"day")
a = "I eat {number} apples. {string}".format(number =10,string = "day") # 지정 포멧팅

# 문자열 정렬
a = "{0:<10}".format("hi") # 좌정렬
print(a)
a = "{0:>10}".format("hi") # 우정렬
print(a)
a = "{0:^10}".format("hi") # 중앙정렬
print(a)
a = "{0:*^10}".format("hi") # 중앙정렬 + 빈곳은 * 로 체움 (등)

# 파이썬 3.6 f 문자열 포멧팅

name = "홍길동"
age = 10
a = f'나의 이름은 {name}입니다. 나이는 {age}살 입니다.' # 변수명이 아니라 연산도 되기는 한다.
