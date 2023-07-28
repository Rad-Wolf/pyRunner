print("I eat %d apples" % 5) # 이런식으로 하면 문자열에서 숫자만 바꾸는 것도 가능하다.

a = 50

print("I eat %d apples" % a)

a = "기다려!"

# 문자열 위지 보간방법
print("%10s" % a) # 10칸 우측기준
print("%-10s" % a) # 10칸 좌측 기준
print("%10s %-10s" % a % a) # 2개의 문자열은 이런식으로
