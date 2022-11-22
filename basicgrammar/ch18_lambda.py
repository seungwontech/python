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
# [1, 4, 9, 16]
print(list(map(lambda x: x * x, range(1, 5))))
# [1, 4, 9, 16]
