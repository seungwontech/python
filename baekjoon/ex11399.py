n = int(input())
v_list = list(map(int, input().split()))
v_list.sort()
cnt = 0
sum_cnt = 0
for i in v_list:
    cnt += i
    sum_cnt += cnt

print(sum_cnt)
