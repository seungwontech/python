H, M = map(int, input().split())
A = int(input())
hap = M + A

H += hap // 60
M = hap % 60

if H > 23:
    H -= 24

print(H, M)
