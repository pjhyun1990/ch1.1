# 생성
d = {'basketball': 5, 'baseball': 9}
print(d, type(d))

d2 = dict()
print(d2, type(d2))

# 인덱스 대신에 key로 접근한다.
print(d['baseball'])

# 연결을 지원하지 않는다.
# d + {'valleyball': 6}   예외 발생

# 반복(*) 지원 X
# d2 = d * 2 예외 발생

# 크기
print(len(d))

# in, not in 키만 가능
print('soccer' not in d)
print('baseball' in d)

d3 = dict(one = 1, two = 2, three =3, five = 5)
print(d3)

dict([('one', 1)]),('two', 2), ('three', 3), ('five', 5)

# 다양한 타입의 키를 사용할 수 있다.
d = {}
print(d)

d['tewnty'] = 20
d[True] = 'true'

# 객체함수

k = d.keys()
print(k, type(k))

for key in k:
    print(key, d[key])


v = d.values()
print(v, type(v))

i = d.items()
print(i)

for t in i:
    print(t)

phones = {'둘리': '000-0000-0000', '도우넛': '111-1111-1111', '또치': '222-22222-22222'}
phones['마이콜'] = '777-7777-7777'

print(phones)

print(phones.get('마이콜'))

# print(phones['길동']) 에러
# get()을 사용하는 이유 : 없는 경우에는 none
print(phones.get('길동'))


# set default :
print(phones.setdefault('길동', '555-555-555'))
print(phones)

# pop()
name = phones.pop('둘리')
print(name)
print(phones)

# 조회

d = {'c': 3, 'a': 1, 'b': 2}

for key in d:
    print(key, end=' ')
else:
    print('', end='\n')


for key in d.keys():
    print(key, end=' ')
else:
    print('', end='\n')


for key, value in d.items():
    print(key, value, end=' ')
else:
    print('', end='\n')
