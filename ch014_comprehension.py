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
# 첫번째 i는 i + 1를 넣게 되면 결과 값이 [5, 6, 7]
# 아무 조건도 넣지 않으면 그대로 사용

# 해석: b_list 에서 3보다 큰 값들만 그대로 사용하여 new_b_list로 만들어줘

print(new_b_list)
# 결과: [4, 5, 6]
