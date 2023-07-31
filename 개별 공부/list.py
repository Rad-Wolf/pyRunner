# subway = ["유재석","강호동","신동엽"]

# print(subway)
# print(subway.pop())
# print(subway)

# # 정렬
# numlist = [5,6,1,2,3,4]

# numlist.sort()
# print(numlist)
# numlist.reverse()
# print(numlist)

# # 지우기

# numlist.clear()
# print(numlist)

# 다양한 자료형이 가능

mix_list = ["남상익", 20 ,0x1f]
num_list = [5,6,7,2,4,3,1]

# mix_list.sort() # 이 경우에는 정렬은 기준 값이 없음 -> 안됨
print(mix_list)
num_list.sort()
print(num_list)
num_list.extend(mix_list) # 합산도 가능
print(num_list)