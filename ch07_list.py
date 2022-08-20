a_list = ['a', 'b', 'c']
print(a_list[0]);
# 결과: a
# 중복 허용, 순서 보장
print(a_list[0:2]);
# 결과: ['a', 'b']

# 추가
a_list.append('d')
print(a_list)
# 결과: ['a', 'b', 'c', 'd']

# 삭제
a_list.remove('a')
print(a_list)
# 결과: ['b', 'c', 'd']

b_list = ['y', 'z']
# 리스트 확장
a_list.extend(b_list)
print(a_list)
# 결과: ['b', 'c', 'd', 'y', 'z']

# 원하는 위치에 값 추가
a_list.insert(0, 'k')
print(a_list)
# 결과: ['k', 'b', 'c', 'd', 'y', 'z']

# 원하는 위치 또는 마지막의 값 삭제
# 원하는 위치
a_list.pop(0)
print(a_list)
# 결과: ['b', 'c', 'd', 'y', 'z']

# 마지막의 값 삭제
a_list.pop()
print(a_list)
# 결과: ['b', 'c', 'd', 'y']

# 모든 값 삭제
a_list.clear()
print(a_list)
# 결과: []

# 값의 순서대로 정렬
c_list = ['b', 'a', 'c', 'a']
c_list.sort()
print(c_list)
# 결과: ['a', 'a', 'b', 'c']

# 순서 뒤집기
c_list.reverse()
print(c_list)
# 결과: ['c', 'b', 'a', 'a']
# 어떤 값이 몇개 있는지
print(c_list.count('a'))
# 결과: 2

# 어떤 값이 어디에 위치했는지
print(c_list.index('b'))
# 결과: 1

# 리스트복사
a_list = c_list.copy()
print(a_list)
# 결과: ['c', 'b', 'a', 'a']
