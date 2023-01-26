n, mony = map(int, input().split())
value_list = []
for i in range(n):
    value = int(input())
    value_list.append(value)

count = 0
value_list.sort(reverse=True)

# reversed 요소를 뒤집을때 사용
# value_list.reverse()
# for val in reversed(value_list)

for val in value_list:
    count += mony // val
    if count > 0:
        mony %= val

print(count)

# 10 4200
# 1
# 5
# 10
# 50
# 100
# 500
# 1000
# 5000
# 10000
# 50000
