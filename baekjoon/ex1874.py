n = int(input())
stack = []
k = 1
for i in range(n):
    value = int(input())
    while k <= value:
        stack.append(k)
        print('+')
        k += 1

    if stack[-1] == value:
        stack.pop()
        print('-')
    else:
        print('NO')
        break



# 8
# 4
# 3
# 6
# 8
# 7
# 5
# 2
# 1