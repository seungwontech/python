# def 함수명():
def price():
    print('1000원 입니다.')

print('이건 얼마인가요?')
price()
# 결과
# 이건 얼마인가요?
# 1000원 입니다.

def test_function():
    print('호출')

test_function()
# 결과: 호출

def test_function(i):
    print(i, '번째 호출')

for i in range(5):
    test_function(i + 1)


# 사용하지 않은 예제
def test_sum(a, b):
    a + b


print(test_sum(1, 2))
# 결과: None

# 사용한 예제
def test_sum(a, b):
    return a + b

print(test_sum(1, 2))
# 결과: 3


# 기본값 설정
def test_function(a=0):
    if a != 0:
        return a
    else:
        return a

a = 100
print(test_function(a));
# 결과: 100
print(test_function());
# 결과: 0
