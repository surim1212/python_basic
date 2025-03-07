a = [1, 2, 3, ['a', 'b', [1, 3, 5], 'c']]

jumin = '000212-4111111'

print(jumin.split('-'))  # ['000212', '4111111']
j = jumin.split('-')
print(j[1][0])

b = [1,2,3]
c = [4,5,6,7]

print(b+c) 

d = [1,2,3]
print(d*3)

print(len(jumin))        # 14 (문자 개수)
print(len(a))            # 4 (리스트 a의 길이)
print(a[3])              # ['a', 'b', [1, 3, 5], 'c']
print(len(a[3]))          # 4 (a[3]의 길이)
print(len(a[3][3]))
print(len(a[3][0]))      # 1 ('a'의 길이)

a[3][0]= 'hi'
print(a)

del a
# print(a)

a = [1,2,3]
a.append(4)
a.append('qqq')
a.append([4,5,6])
print(a)

a.insert(0,'aaa')
print(a)
a = [1,4,3,2]
a.sort(reverse=True)
print(a)
a = [1,4,3,2]
a.reverse()
print(a)

a = ['a','b','c','b']
a.remove('b')
print(a)

a = ['a','b','c','b']
print(a.pop(a.index('b')))
print(a)

t1 = (1, 2, 'a', 'b')
# t1[0] = 0
# del t1[0]

    
    