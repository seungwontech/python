def a(num):
    if num < 2:
        print(num, end='')
    else:
        a(num // 2)
        print(num % 2, end='')


a(20)
print()

print(20 % 2)
print(10 % 2)
print(5 % 2)
print(2 % 2)
print(1 % 2)
