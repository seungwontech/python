print('서울시 서초구'.find('특')) # 결과: -1
# print('서울시 서초구'.index('특') # 결과: ValueError: substring not found
print('서울시 서초구'.find('서')) # 결과: 0
print('서울시 서초구'.rfind('서')) # 결과: 4

print('서울시 서초구'.find('서', 1)) # 결과: 4
print('서울시 서초구'.find('시', 1 ,4)) # 결과: 2
print('서울시 서초구'.find('서', 1 ,4)) # 결과: -1
print('서울시 서초구'.find(' ', 1 ,4)) # 결과: 3
print('서울시 서초구'.find('울', 1 ,4)) # 결과: 1
