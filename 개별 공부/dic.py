cabinet = {3:"유재석",20:"남상익"}

# 1번 방법
print(cabinet[3])
# 2번 방법
print(cabinet.get(3))

# 키가 없을 경우 오류가 남
# print(cabinet[5])

# get을 사용시 오류는 나지 않음
print(cabinet.get(5))
print(cabinet.get(5,"사용가능")) # 이렇게 하면 none 이 아닌 원하는 값이 나옴

print( 3 in cabinet) # True 반환
print (5 in cabinet) # False 반환

# 키 값은 int 가 아니라 string 값이 될 수 있음

# 추가 / 수정
cabinet[3] = "박노성"
cabinet[30] = "남상수"

print(cabinet)

# 제거
del cabinet[3]
print(cabinet)

# 키 출력
print(cabinet.keys())
# 값 출력
print(cabinet.values())
# 전체 출력
print(cabinet.items())
