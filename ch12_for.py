# i 는 변수
# range(10) 0~9
# 0 이상 10 미만
for i in range(10):
    print(i + 1)

# range(start, stop, step)
# start 이상 stop 미만 step 만큼 증가
# 1 이상 10 미만 2만큼 증가
for i in range(1, 10, 2):
    print(i)
# 결과: 1, 3, 5, 7, 9

for i in range(1, 10, 3):
    print(i)
# 결과: 1, 4, 7
