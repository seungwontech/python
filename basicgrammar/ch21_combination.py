from itertools import combinations

test_list = ['A','B', 'C']

result = list(combinations(test_list, 2))
print(result)
# 결과: [('A', 'B'), ('A', 'C'), ('B', 'C')]