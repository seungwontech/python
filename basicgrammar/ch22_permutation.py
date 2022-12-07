from itertools import permutations

test_list = ['A', 'B', 'C']

result = list(permutations(test_list, 2))
print(result)
# 결과: [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
