a_list = [1, 2, 3, 4, 5, 6]
new_a_list = []
for i in a_list:
    if i > 2:
        new_a_list.append(i)

print(new_a_list)
# 결과: [3, 4, 5, 6]

# list comprehension 사용
b_list = [1, 2, 3, 4, 5, 6]
new_b_list = [i for i in b_list if i > 3]

print(new_b_list)
# 결과: [4, 5, 6]
