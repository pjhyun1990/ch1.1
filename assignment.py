# 치환문

a = 1
b = a + 1
print(a, b, sep = ':')

#  변수 할당값 오류

# 1 + a = c
# e = 3.5: f = 5.3
# print(e, f)


# 여러개를 한번에 치환
e, f = 3.5, 5.5
print(e, f)

# 같은 값을 여러 번수에 할당

x = y = z = 10
print(x,y,z)

# c 스타일은 지원 x

# x = ( y = 10)
x = 1
y = 2
print(x, y)
temp = x
x = y
y = temp
print(x, y)
x, y = y, x
print(x, y)

# 동적 타이핑

a = 1
print(type(a))

a = 'hello'
print(type(a))

# 확장 치환문

a = 10
a += 10 # a = a + 10
print(a)

a -= 3
print(a)