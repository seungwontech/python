n, k = map(int, input().split())
list_a = list(map(int, input().split()))
list_a.sort(reverse=True)
print(list_a[k-1])

# 5 2
# 100 76 85 93 98
# 결과: 98