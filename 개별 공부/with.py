# with

# with 는 내부에서 활용하는 객체(?)를 내부에서만 활용 가능하게 해주는 기능이다. c#의 using과 동일하다

# import pickle # 피클 읽기 활용법
# with open("save.pickle","rb") as profile:
#     print(pickle.load(profile)) # close 과정이 없음. -> 자동정리

with open("save.pickle","a", encoding="utf8") as profile:
    profile.write("파이썬 : 30\n")
    print("이렇게도 활용 가능함",file=profile)
