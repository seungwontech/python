def test_sum(a, b):
    return a + b


print(test_sum(1, 2))
# 결과: 3
print((lambda a, b: a + b)(3, 4))


# 결과: 7


def test_calc(x):
    return x * x


for i in range(1, 5):
    print(test_calc(i))

# 1
# 4
# 9
# 16

print(list(map(test_calc, range(1, 5))))
# 결과: [1, 4, 9, 16]
print(list(map(lambda x: x * x, range(1, 5))))
# 결과: [1, 4, 9, 16]


menu_array = [('햄김치볶음밥', 7500), ('참치볶음밥', 6800), ('햄치즈볶음밥', 7000)]


def order_money(x):
    return x[1]


print(sorted(menu_array, key=order_money))
# 결과: [('참치볶음밥', 6800), ('햄치즈볶음밥', 7000), ('햄김치볶음밥', 7500)]
print(sorted(menu_array, key=lambda x: x[1]))
# 결과: [('참치볶음밥', 6800), ('햄치즈볶음밥', 7000), ('햄김치볶음밥', 7500)]
