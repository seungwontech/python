a = 'Hello world'

print("소문자: " + a.lower())
# 결과: hello world
print("대문자: " + a.upper())
# 결과: HELLO WORLD
print("대소문자: " + a.swapcase())
# 결과: hELLO WORLD
print("o는 몇개인가?: " + str(a.count('o')))
# 결과: 2
b = 'cat dog'
print("첫글자만 대문자: " + b.capitalize())
# 결과: Cat dog
print("각단어의 첫글자만 대문자: " + b.title())
# 결과: Cat Dog

c = 'Hi Python'
print("Hi로 시작하는지?: " + str(c.startswith('Hi')))
# 결과: True
print("Hi로 끝나는지?: " + str(c.endswith('Hi')))
# 결과: False
print("Hi로 끝나는지?: " + str(c.endswith('Python')))
# 결과: True
print("문자열 일부 변경: " + c.replace('Python', 'JAVA'))
# 결과: Hi JAVA
print("특정위치 찾기: " + str(c.find('P')))
# 결과: 3 (index 기준)

d = '.Hi Python.'
print("앞뒤로 특정문자 제거: " + d.strip('.'))
# 결과: Hi Python
