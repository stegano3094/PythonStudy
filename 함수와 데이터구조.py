# 자료형 변환
data1 = '1'
# data2 = data1 + 1  # 문자열 + 숫자는 에러 발생
data2 = int(data1) + 1  # int() 함수를 통해서 int형 타입으로 변환해주어야 함
print(data2)

# 사용자 함수
def func1(data1):
    return data1 * data1

def func2(data1, data2):
    print(data1 - data2)

print(func1(3))
func2(3, 4)

# 리스트
data3 = [1, 2, 3, 4]  # 데이터가 있는 리스트 생성
data4 = list()  # 데이터가 없는 리스트 생성

print(data3)  # 읽기
print(data3[3])  # 특정 위치 읽기
data3.append(5)  # 삽입
del data3[3]  # 특정 위치 삭제
data3[1] = 'tiger'  # 수정

print(data3)


# 리스트 반복
for item in data3:
    print(item)
