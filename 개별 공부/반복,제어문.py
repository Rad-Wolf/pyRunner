# if

# weather = input("���� ������ ���?")
# if weather =="��":
#     print("����� ì�⼼��")
# elif weather == "�̼�����":
#     print("����ũ�� ì�⼼��")
# else:
#     print("�غ��� �ʿ� �����")

# for

# temp = 0
# for day in range(1,5):
#     temp = int(input(f"{day}���� ����� ���? "))
#     if 30 <= temp :
#         print("������ �� �־��. �����ϼ���")
#     elif 20 <= temp :
#         print("���ƴٴϱ� ���� ��������")
#     elif 0 <= temp :
#         print("�ҽ� �ϳ׿� ������ �ѿ��� ì�⼼��")
#     else:
#         print("�̺� ���� ���� �� �� �־�� ������ ���� ã������")


# while

# customer = "�丣"
# index = 5
# while index >= 1:
#     print(f"{customer}��, Ŀ�ǰ� �غ�Ǿ����ϴ�.")
#     index -= 1
#     if index == 0:
#         print(f"{customer}���� Ŀ�Ǵ� ��� �˴ϴ�.")

# continu, brack

# absent = [2,5] # �Ἦ�� ��ȣ
# no_book = [7] # å�� ����
# for student in range(1,11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print(f"���� ������ �������. {student}��(��) �����÷� �����!")
#         break
#     print(f"{student}, å �о��")

# ���ٷ� ������ for��

# �⼮��ȣ�� 1,2,3,4..... �տ� 100�� ���̱�� ��
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# students = ["���̾��","�丣","�׷�Ʈ"]
# students = [len(i) for i in students]
# print(students)

# ����

# 50���� �°��� ��Ī
# �°��� 5�� ~ 50�� ������ ���� -> �ҿ�ð�
# 15�� �̸��� �°��� ��Ī�ؾ���
# ž���� �°��� ���� ���϶�

# ���� ��
# import random
# count = 0
# total_time = 0

# for customer in range(50):
#     time = random.randrange(5,50)
#     if time >= 15 :
#         print(f"[ ] {customer+1:2}��° �մ� (�ҿ�ð� : {time:2})")
#     else:
#         print(f"[O] {customer+1:2}��° �մ� (�ҿ�ð� : {time:2})")
#         count += 1
#         total_time += time
# print(f"{count}���� �°� ž��, �� �ҿ�ð� {time}��")

# ������ ��

from random import * # �̷��� �ϸ� Ÿ�� ���� ���� �� ���� ���� �ҷ���
cnt = 0
for i in range(1,51):
    time = randrange(5,51) # 5 ~ 50
    if 5 <= time <= 15: # 5 ~ 15 �� �̳��� �մ�
        print(print(f"[O] {i:2}��° �մ� (�ҿ�ð� : {time:2})"))
        cnt += 1 # ž�� �°� ����
    else:
        print(print(f"[ ] {i:2}��° �մ� (�ҿ�ð� : {time:2})"))

print(f"�� ž�� �°� �� :{cnt}")