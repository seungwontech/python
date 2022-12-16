N, K = map(int, input().split())
result = 0

while True:
    if N % K == 0:
        N //= K
    else:
        N -= 1

    if N < K:
        result += N
        break

    result += 1

print(result)
