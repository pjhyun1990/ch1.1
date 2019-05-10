# 생성

t = ()
t = (1)
print(t, type(t))
t = (1,)
print(t, type(t))

t = (1, 2, 3)
print(t, type(t))

# 시퀀스 연산

print(t[-3], t[-2], t[-1], t[0], t[1], t[2])


# 슬라이싱
print(t[1:3])
print(t[:])

# 반복
t2 = t * 2
print(t2)

# 연결
t3 = t + (4, 5, 6)
print(t3)

# 길이
print(len(t))

# in, not in
print(5 in t3)

# 튜플은 변경 불가능하다
# t = ('apple', 'banana', 10, 20)
# t[2] = 90



# 튜플을 이용해서 여러개의 값을 대입할 수 있다.
x, y, z = 10, 20, 30

# 튜플을 이용해서 여러개의 값을 치환할 수 있다.

x, y = 10, 20
print(x,y)
x,y = y, x
print(x,y)

# 객체 함수 : immutable 때문에 객체 함수가 많지가 않다.

t = (20, 30, 40, 50, 20)
print(t.index(30))
print(t.count(20))

s = set(t)
