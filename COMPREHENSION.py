results = []

for num in [1, 2, 3, 4, 5, 6, 7, 8]:
    result = num * num
    results.append(result)

print(results)

results = [ num * num for num in [1, 2, 3, 4, 5, 6, 7, 8] ]
print(results)


string = ['a', 'as', 'bat', 'car', 'dove', 'python']
strings = [ s + '!' for s in string if len(s) <= 2]
print(strings)


# 1~ 100 사이에 3,6,9 가 있는 수 리스트 만들기
result = [ num for num in range(1,101) if num % 10 == 3 ]

print(result)
print("asdfaefawefwaef")









# 1 ~ 100 사이의 짝수 리스트
evens = [ i for i in range(1,101) if i % 2 == 0]
print(evens)

# set comprehension
string = ['a', 'as', 'bat', 'car', 'dove', 'python']
strings = { s + '!' for s in string if len(s) <= 2}


