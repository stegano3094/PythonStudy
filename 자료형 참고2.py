import time

start_time = time.time()  # 측정 시작

# 정수형 =============================================================
a = 123  # 양의 정수
print(a)

a = -123  # 음의 정수
print(a)


# 실수형 =============================================================
a = 157.93  # 양의 실수
print(a)

a = -1837.2  # 음의 실수
print(a)

a = -13.  # 소수부가 0일 때 생략 가능
print(a)

a = .3  # 정수부가 0일 때 생략 가능
print(a)

# 지수 표현
# 1e9 => 1*10^9 => 10의 9제곱
a = 1e9  # <- 실수형으로 저장됨
print(a)

a = int(1e9)  # <- 정수형으로 변환되어 저장
print(a)

a = 75.25e9
print(a)

a = 3954e-3
print(a)

a = 0.3 + 0.6  # 0.89에 가깝게 저장되어 0.9랑 값이 다름(표현상의 한계)
print(a)
if a == 0.9:
    print(True)
else:
    print(False)
    
a = round(a, 2)  # round함수, 반올림을 통해서 표현하는 것을 권장함
print(a)

# 수의 연산 =========================================================
a, b = 7, 3

print(a / b)  # 나누기
print(a % b)  # 나머지
print(a // b)  # 몫
print(a ** b)  # 거듭 제곱
print(a ** 0.5)  #거듭 제곱근


# 리스트 자료형 =====================================================
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(a[3])  # 배열(리스트)은 0번부터 시작함, 3은 4번째 값을 읽어오면 4가 출력됨

n = 10
a = [0] * n
print(a)

a[1] = 3  # 리스트의 특정 원소에 접근하는 것을 인덱싱이라고 함
a[9] = 5
print(a)
print(a[1])
print(a[-1])
print(a[1:4])  # 1~3번째 수를 가져옴

a.append(10)
print(a)

a = [i for i in range(10)]  # 리스트 컴프리헨션
print(a)

a = [i for i in range(20) if i % 2 == 1]  # 0 ~ 19 수 중에서 홀수만
print(a)

a = [i*i for i in range(1, 10)]  # 1 ~ 9 수들의 제곱 값
print(a)

# 리스트 정렬 메서드
a = [6, 2, 4, 3, 2, 7, 2, 8]
a.append(1)  # O(1)
print(a)

a.sort()  # 오름차순 정렬, O(N*logN)
print(a)

a.sort(reverse = True)  # 내림차순 정렬, O(N*logN)
print(a)

a.reverse()  # 배열을 반대로 뒤집어 놓음, O(N)
print(a)

a.insert(3, 100)  # (a, b) a번째에 b를 삽입, O(N*logN)
print(a)

print(a.count(2))  # (a) a를 가지고 있는 데이터 개수를 셀 때 O(N)

a.remove(2)  # (a) a를 제거함, 단 여러 개면 하나만 제거, O(N)
print(a)

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}
result = [i for i in a if i not in remove_set]
print(result)


# 문자열, 튜플  자료형 =====================================================
a = 'aaaaaa'
print(a)

b = 'bbbb'  # 문자열, 문자 슬라이싱은 가능하지만 특정 문자만 바꾸는건 안 됨
print(a + b)
print(a * 3)
print(a[2:4])  # 문자열 슬라이싱
# a[0] = 'c' 문자열은 이렇게 사용하지 못함

a = (1, 2, 3, 4, 5)  # 튜플, 변경 불가능한 객체
print(a[0])
print(a[1:4])
# a[0] = 3 튜플은 이렇게 사용하지 못함


# 사전, 집합 자료형 =====================================================
a = dict()
a['사과'] = 'Apple'
a['바나나'] = 'Banana'
a['코코넛'] = 'Coconut'
print(a)

if '사과' in a:
    print("'사과' 라는 키가 존재 합니다.")

b = {'사과': 'Apple', '바나나': 'Banana', '코코넛': 'Coconut'}
print(b)
print(b['사과'])

if '바나나' in b:
    print("'바나나' 라는 키가 존재 합니다.")

key = b.keys()
value = b.values()
print(key, value)


a = set([1, 2, 3, 3, 3, 4, 4])  # 집합 자료형 초기화 방법 1
print(a)  # 집합 자료형은 중복 허용 안 함

a = {1, 1, 2, 2, 3, 3, 3, 4}  # 집합 자료형 초기화 방법 2
print(a)

a.add(4)  # 새로운 원소 추가
print(a)

a.update([5, 6, 7])  # 여러 개 추가 가능
print(a)

a.remove(3)  # 원소 제거
print(a)


print('변수 타입 : ', type(a))  # 변수의 타입을 확인할 수 있다



end_time = time.time()  # 측정 종료
print("time : ", end_time - start_time)  # 수행 시간 출력
