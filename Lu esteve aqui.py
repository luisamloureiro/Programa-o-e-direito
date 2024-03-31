def soma(a, b):
    return a + b

def quadrado(a):
    return a**2

def hipotenusa(cateto1, cateto2):
    return soma(quadrado(cateto1), quadrado(cateto2)) ** (1/2)


#pythontutor

def simples(cor):
    if cor == 'azul': 
        return 'Escolheu bem'
    
def medio(cor):
    if cor =='azul':
        return 'Escolheu certo'
    else: 
        return 'Tente outra cor'
    
def completo(cor):
        if cor == 'azul':
            return 'Escolheu certo'
        elif cor == 'marrom':
            return 'Não tem salvação'
        else:
            return 'Tente outra cor'
        
#listas

numeros = [1, 2, 3, 4, 5]
print(numeros[0])
print(numeros[-1])

numeros[0] = 'banana'
print(numeros[0])

#laços de repetição

contador = 0 
while contador < 10:
    print(contador)
    contador += 1
    
for i in range(10):
    print(i)
    
for item in [1, 45, 78, 'a', [3, 5]]:
    print(item)
    
for letra in 'minha string':
    print(letra)
    
#triângulo

def sequencia_asteriscos(num_linhas):
    for i in range(1, num_linhas + 1):
        print('*' * i)
        

sequencia_asteriscos(5)
    