# 생성
l1 = []
l1 = [1, True, 'python', 3.14]

# 인덱싱
print(l1[0], l1[1], l1[2], l1[3])
print(l1[-4], l1[-3], l1[-2], l1[-1])

# slicing
print(l1[1:3])
print(l1[2:4])
print(l1[3::-1])
print(l1[len(l1)-1::-1])

# 연결
l2 = l1 + [1, 2, 3]
print(l2)

# 길이
print(len(l1))

# in, not in 확인
print(5 not in l2)
print('python' in l2)

a = [1, 2, 3, 4, 5, 6]

print(a)

a[1:2] = [100]
print(a)

a[2:3] = [200, 300]
print(a)

# 슬라이싱을 사용한 삭제
a = [1, 12, 123, 1234]

a[1:2] = []
print(a)

a[0:] = []
print(a)
"""
# 슬라이싱을 사용한 삽입

a = [1, 12, 123, 1234]

# 중간 삽입
a[1:1] = ['a']
print(a)

# 마지막에 삽입
a[5:] = [12345]
print(a)
a[len(a):len(a)+1] = [000000]
print(a)

# 처음에 삽입
a[:0] = [0]
print(a)

# 여러개 삽입
a[2:2] = [-12, -1, 0]
print(a)
"""
# 객체함수 뒤에 삽입
a.append(5)
print(a)

# 앞에 삽입
a.insert(0, 0)
print(a)

# reverse
a.reverse()
print(a)

# 제거(값으로 삭제)
a.remove(0)
print(a)


# queue 사용하기
q = [1, 2]
q.append(3)
q.append(4)
q.append(5)
q.append(6)

print(q)
print(q.pop(0))
print(q.pop(0))

print(q)


# stack 사용하기

s = []
s.append(10)
s.append(20)
s.append(30)

print(s)

print(s.pop())
print(s)



# sort 내장된 정렬 알고리즘에 따라 정렬

l = [1, 5, 3, 9, 8, 20]
l.sort()
print(l)

l.sort(reverse=True)
print(l)

l = [10, 2, 22, 9, 8, 33, 4, 11]
l.sort(key = str)
print(l)

l.sort(key=int)
print(l)

# 전역함수 sorted
l = [19, 46, 37, 28, 91, 55, 64]
l2 = sorted(l)
print(l2)

l = [19, 46, 37, 28, 91, 55, 64]

def f(i):
    return i % 10


print(f(12))

l2 = sorted(l, key=f, reverse=True)
print(l2)

l2 = sorted(l, key=f, reverse=False)
print(l2)