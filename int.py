a = 23
print(a, type(a))
print(isinstance(a,int))

b = 0b1101
c = 0o23
d = 0x23


print(b)
print(c)
print(d)

# 3.x 에서는 int. long 합쳐졌다. 따라서 int의 표현범위가 무한대다.

e = 2**1024

print(e)
print(type(e))
print(e.bit_length())


# 변환함수
print(oct(38))
