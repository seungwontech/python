A, B = map(int, input().split())


def f(n):
    start = n // 4 * 4
    answer = 0
    for i in range(start, n + 1):
        answer ^= i

    print(answer)
    return answer


print(f(A - 1) ^ f(B))
