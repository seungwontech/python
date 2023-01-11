n = int(input())

n_list = list(map(int, input().split()))
n_list.sort()

result = 0
count = 0

for i in n_list:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)
