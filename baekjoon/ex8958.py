n = int(input())
result = []
for _ in range(n):
    num_list = list(input())
    sum_count = 0
    count = 0
    for i in num_list:
        if i == 'O':
            count += 1
        else:
            count = 0
        sum_count += count
    result.append(sum_count)

for i in result:
    print(i)
