python ='파이썬'
java ='자바'

print('오늘은 {}과 {} 공부할게요'.format(python,java))
# 결과: 오늘은 파이썬과 자바 공부할게요
print('오늘은 {1}과 {0} 공부할게요'.format(python,java))
# 결과: 오늘은 자바과 파이썬 공부할게요
print(f'오늘은 {python}과 {java} 공부할게요')
# 결과: 오늘은 파이썬과 자바 공부할게요
# 파이썬 버전 3.6 이상