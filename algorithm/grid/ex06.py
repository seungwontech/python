n = int(input())

cnt = 0
a = str(3)
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if str(i).find(a) > -1 or str(j).find(a) > -1 or str(k).find(a) > -1:
            # if '3' in str(i) + str(j) + str(k):
            # 문자열 끼리 더해서 처리하는 방법
                cnt += 1

print(cnt)
