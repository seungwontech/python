# list
list = [1, 2, 4]
list_sum_result = sum(list)
print(list_sum_result)
# 결과: 7

# tuple
tuple = (1, 3, 6)
tuple_sum_result = sum(tuple)
print(tuple_sum_result)
# 결과: 10

# set
set = {1, 2, 5}
set_sum_result = sum(set)
print(set_sum_result)
# 결과: 8

# dictionary
dictionary = {1: 2, 13: 4}
dictionary_keys_sum_result = sum(dictionary.keys())
print(dictionary_keys_sum_result)
# 결과: 14
dictionary_values_sum_result = sum(dictionary.values())
print(dictionary_values_sum_result)
# 결과: 6

# min(), max()
min_result = min(3, 1, 2)
print(min_result)
# 결과: 1
max_result = max(3, 1, 2)
print(max_result)
# 결과: 3

# eval()
a = "1+4*2"
print(eval(a))

# sorted()
sorted_result = sorted([5, 34, 2, 6, 78, 1])
print(sorted_result)
# 결과: [1, 2, 5, 6, 34, 78]
sorted_reverse_result = sorted([5, 34, 2, 6, 78, 1], reverse=True)
# 결과: [78, 34, 6, 5, 2, 1]
print(sorted_reverse_result)
