from collections import Counter

test_list = ['a', 'b', 'c', 'a']

print(Counter(test_list))
# 결과: Counter({'a': 2, 'b': 1, 'c': 1})

test_count = Counter('Hello python')
print(test_count)
# 결과: Counter({'l': 2, 'o': 2, 'H': 1, 'e': 1, ' ': 1, 'p': 1, 'y': 1, 't': 1, 'h': 1, 'n': 1})

print(test_count.most_common(3))
# [('l', 2), ('o', 2), ('H', 1)]

print(test_count['o'])