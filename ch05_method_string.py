a = 'Hello world'

print("소문자: " + a.lower())
# 결과: hello world
print("대문자:" + a.upper())
# 결과: HELLO WORLD
print("대소문자: " + a.swapcase())
# 결과: hELLO WORLD

b = 'cat dog'
print("첫글자만 대문자: " + b.capitalize())
# 결과: Cat dog
print("각단어의 첫글자만 대문자: " + b.title())
# 결과: Cat Dog