def test_sum(a, b):
    return a + b


print(test_sum(1, 2))
# 결과: 3
print((lambda a, b: a + b)(3, 4))
# 결과: 7