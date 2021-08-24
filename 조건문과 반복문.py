# 조건문 ==========================================================
score = 45

if score >= 70:
    print('성적이 70점 이상입니다.')

    if score >= 90:
        print("우수한 성적입니다.")
elif score >= 40:
    print('성적이 40점 이상 70점 미만입니다.')
    
else:
    print('성적이 40점 미만입니다.\n조금 더 분발하세요.')

print('조건문이 끝났습니다.')


if True or False:
    print('Yes')


if True:
    pass  # 아무것도 실행하지않고 그냥 지나감
else:
    print('No')

score = 85

if score >= 80: result = 'Wow'  # <- 문장 안이 한 줄이라면 간략하게 쓸 수 있음
else: result = 'Fail'
print('result :', result)

result = "Success" if score >= 80 else 'Fail'  # <- 간략하게 쓸 수도 있음
print('result :', result)

if 60 < score < 90:
    print(f'score is {score}.')


# 반복문 ==========================================================
i = 0
result = 0

while i <= 9:
    if i % 2 == 1:  # 홀수
        result += i
    i += 1
print(result)


a = [1, 2, 3, 4, 5, 5]
b = (1, 2, 3, 4, 5, 5)
for prt in a:
    print(prt)

print("")
for prt in b:
    print(prt)

print('for i in range(1, 10):')
for i in range(1, 10): # 1~9까지
    if i % 2 == 0:
        continue
    print(i)


print('for i in range(10):')
for i in range(10): # 0~9까지
    print(i)
    
i = 0
while True:
    print("현재 i 값 : ", i)
    if i == 5:
        break
    i += 1

# 특정 리스트만 제외하고 출력할 때
scores = [90, 85, 77, 65, 97]
cheating_student_list = {2, 4}

for i in range(5):
    if i + 1 in cheating_student_list:
        continue
    if scores[i] >= 80:
        print(i+1, '번 학생은 합격입니다.')
