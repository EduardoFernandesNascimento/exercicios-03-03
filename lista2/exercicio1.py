# exercicio_1
frutas= ["maçã", "banana", "laranja"]
print(frutas[1])

# exercicio_2
frutas.append("uva")
print(frutas)
frutas.pop(1)
print(frutas)

# exercicio_3
numeros= []

for i in range(1,11):
    numeros.append(i)

print(f'A lista números contém: {len(numeros)} itens')

# exercicio_4

def verificaçao(n):
    if n in numeros:
        return 'está na lista'
    else:
        return 'nao está na lista'
    
print(verificaçao(7))

# exercicio_5

print(numeros[0:3])

# exercicio_6

notas = [8.5, 7.0, 9.5, 6.0]
notas.sort(reverse=True)
print(notas)

# exercicio 7

a=0

for i in  numeros:
    if i == 5:
        a+=1

print(f'o numero 5 aparece {a} vez(s) na lista numeros')

# exercicio 8

print(numeros[::-1])
