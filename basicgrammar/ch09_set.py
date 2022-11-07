# 중복안됨, 순서보장하지않음
a_set = {1, 2, 3}
b_set = {3, 4, 5, 6}

# 공통 데이터 교집합
print(a_set.intersection(b_set))
# 결과: {3}

# 모두 데이터 합집합
print(a_set.union(b_set))
# 결과: {1, 2, 3, 4, 5, 6}

# a_set만 차집합
print(a_set.difference(b_set))
# 결과: {1, 2}

# 값 추가
a_set.add(4)
print(a_set)
# 결과: {1, 2, 3, 4}

# 값 삭제
a_set.remove(1)
print(a_set)
# 결과: {2, 3, 4}

# 모든값 삭제
a_set.clear()
print(a_set)
# 결과: set()
