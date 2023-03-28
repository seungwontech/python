# 기본
stack = []
stack.append(1)
stack.append(6)
stack.append(3)
stack.append(2)
stack.pop()
stack.append(9)
stack.append(8)
stack.pop()
print('최하단: ', stack)
print('최상단: ', stack[::-1])
