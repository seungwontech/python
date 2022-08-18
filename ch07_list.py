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
