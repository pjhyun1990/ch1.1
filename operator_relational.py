# 객체의 대소비교
print(1 > 3)
print(2 < 4)

print(1 >= 3)
print(2 <= 4)

print(1 == 3)
print(2 != 4)

# 복합 관계식 지원
a = 6
print(0 < a and a < 10)
print(0 < a < 10)

# 수치형 이외의 다른 타입의 객체 비교 가능
print('abcd' > 'abc')
print('~~~~~~~~~~~~~~~~~~~')
print((1, 2, 3) > (1, 2, 4))
print([1, 2, 3] > [1, 2, 2])

# 동질성 비교 : ==
# 동일성 비교 : is

a = 10
b = 20
c = a

print(a == b)
print(a is b)

print(a == c)
print(a is c)

# 논리식의 계싼순서
print(True or 'logical')
print(False or 'logical')
print([] or 'logical')
print([10, 20] or 'logical')
print('operator' or 'logicla')

s = 'Hello World'
s and print(s)

s = ''
s and print(s)





