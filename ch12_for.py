# i 는 변수
# range(10) 0~9
# 0 이상 10 미만
for i in range(10):
    print(i + 1, end=' ')

# range(start, stop, step)
# start 이상 stop 미만 step 만큼 증가
# 1 이상 10 미만 2만큼 증가
for i in range(1, 10, 2):
    print(i, end=' ')
# 결과: 1 3 5 7 9

for i in range(1, 10, 3):
    print(i, end=' ')
# 결과: 1 4 7

list = [1, 2, 3, 4, 5, 9]
for i in list:
    print(i, end=' ')
# 결과: 1 2 3 4 5 9

tuple = (1, 3, 4, 10)
for i in tuple:
    print(i, end=' ')
# 결과: 1 3 4 10

dictionary = {'하나': 1, '둘': 2}
for i in dictionary.values():
    print(i, end=' ')
# 결과: 1 2

for i in dictionary.keys():
    print(i, end=' ')
# 결과: 하나 둘

for i, j in dictionary.items():
    print(i, '=', j, end=' ')
# 결과: 하나 = 1 둘 = 2

a = 'python'
for i in a:
    print(i, end=' ')
# 결과: p y t h o n


# 반복문 탈출 break
a_list = ['첫째', '둘째', '셋째', '넷째']
for i in a_list:
    print(i)
    if i == '둘째':
        print('break')
        break

# 반복문 건너뛰기 continue
for i in a_list:
    print(i)
    if i == '셋째':
        print('continue')
        continue