lista= [1,2,3,4,5,6]
res= len(lista)

print(res)
print(lista[3])

for i in range(len(lista)):
    print(i,lista[i])

for i,j in enumerate(lista):
    print(i,j)

lista.insert(0,555)
print(lista)
lista.clear()
lista1=[1,2,3]
lista1.remove(3)
lista2=[6,3,2]
lista1.extend(lista2)
print(lista1)

lista1.sort()
print(lista1)


