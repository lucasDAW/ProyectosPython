import re
# https://www.mclibre.org/consultar/python/otros/python-uso.html

print('Hola Mundo')
exit()

number = "0123456789"
print(number[::2])
name = 'Lizz'
print(name[0:2])

str2= "How much wood would a woodchuck chuck, if a woodchuck could chuck wood?"
matches = re.findall(r"woo", str2)

print(matches)

tuple = (1,4,5,3,5,5.6,True,'Hola')
print(tuple)


A  = (0,1,2,3)
print(A[-1])
B = ["a","b","c"]
B.extend(["d","e"])
B.append(["F","G"])
print(B[1:])
i = True
print(i)

A='1234567'
print(A[1::2])
A=((11,12),[21,22])
print(A[1])
print('1,2,3,4'.split(','))
for n in range(3):

    print(n)
