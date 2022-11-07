# 읽기 전용 리스트 수정불가능
a_tuple = (1, 2, 3)
# 어떤값이 몇개 있는지
print(a_tuple.count(2))
# 결과: 1
# 어떤값이 어디에 잇는지
print(a_tuple.index(1))
# 결과: 0

# 패킹
b_tuple = ('a', 'b', 'c')
# 언패킹
# b_tuple에 있는 값들을 각각 변수에 담는 코드와 같다
(one, two, three) = b_tuple
print(one, two, three);
# 결과: a b c

(a, *others) = a_tuple
print(a)
# 결과: 1
# *others 는 튜플이 아닌 리스트 형태로 된다
print(others)
# 결과: [2, 3]

# others는 리스트형태로 보여준다해도 list 메서드의 종류의 append, pop등을 사용할 수 없는거 같다.
# 사용하려면 list()로 형변환 해주면 사용이 된다.
# list형을 튜플로 형변환하는 메서드는 tuple()이다.
others_list = list(others)
others_list.append(4)
print(others_list)
# 결과: [2, 3, 4]
