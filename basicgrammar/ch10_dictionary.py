# key value
# key 중복안됨
# 파이썬 3.7 이상 순서보장

person = {'이름': '홍길동', '키': 160}
print(person['이름'], person['키'])
# 결과: 홍길도 160

# 키값이 없으면 추가
person['나이'] = 20
print(person)
# 결과: {'이름': '홍길동', '키': 160, '나이': 20}

# 키값이 이미 있으면 수정
person['키'] = 170
print(person)
# 결과: {'이름': '홍길동', '키': 170, '나이': 20}

# 여러 key들의 값을 변경
person.update({'이름': '이순신', '나이': 30, '직업': '해군'})
print(person)
# 결과: {'이름': '이순신', '키': 170, '나이': 30, '직업': '해군'}

# 특정값 삭제
person.pop('키')
print(person)
# 결과: {'이름': '이순신', '나이': 30, '직업': '해군'}

# 어떤 key들이 있는지 확인
print(person.keys())
# 결과: dict_keys(['이름', '나이', '직업'])

# 어떤 value들이 있는지 확인
print(person.values())
# 결과: dict_values(['이순신', 30, '해군'])

# 어떤 key,value들이 있는지 확인
print(person.items())
# 결과: dict_items([('이름', '이순신'), ('나이', 30), ('직업', '해군')])

# 마지막으로 추가된 데이터 삭제
person.popitem()
print(person)
# 결과: {'이름': '이순신', '나이': 30}

# 모든 데이터 삭제
person.clear()
print(person)
# 결과: {}
