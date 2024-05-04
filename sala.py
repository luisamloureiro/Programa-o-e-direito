print("Olá", "mundo", sep="-") # Saída: Olá-mundo

print("Olá", "Python", end="!\n") # Saída: Olá Python!


print("18", "04", "2023", sep="/")
print("nome", "sobrenome", "email", sep="; ")


print("Loading", end=" ")
print("[OK]")# Saída: Loading [OK]


#nome = input("Digite seu nome: ")
#print("Olá", nome)


#itens = input("Digite itens separados por vírgula: ").split(',')

#print("Itens:", itens)


# Convertendo a entrada para inteiro
#idade = int(input("Digite sua idade: "))
#print("Daqui a cinco anos, você terá", idade + 5, "anos.")


# Convertendo a entrada para float
#altura = float(input("Digite sua altura em metros: "))
#print("Sua altura é", altura, "metros.")

def trinta_por_cento():
    print("Digite números para adicionar à lista (digite 'done' para terminar):")
    numeros = []
    while True:
        entrada = input()
        if entrada.lower() == 'done':
            break
        else:
            numeros.append(int(entrada))
    print("Números coletados:", numeros)
    
    
trinta_por_cento()
    
