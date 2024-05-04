
#1
def imprimir_info(nome, idade, cidade, sep=' - ', end='\n'):
    print(f"Nome: {nome}{sep}Idade: {idade}{sep}Cidade: {cidade}{end}", end='')
# Exemplo de uso:
imprimir_info("Alice", 25, "São Paulo")

#2
def calcular():
    # Solicita ao usuário os dois números e a operação desejada
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação desejada (+, -, *, /): ")

    # Verifica a operação e realiza o cálculo
    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        # Verifica se o segundo número é diferente de zero para evitar divisão por zero
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Erro: divisão por zero!")
            return
    else:
        print("Operação inválida!")
        return

    # Imprime o resultado da operação
    print(f"Resultado: {resultado}")

# Exemplo de uso da função
calcular()

#3
def lista_de_compras():
    # Solicita ao usuário para digitar os itens da lista de compras
    itens = input("Digite os itens da lista de compras, separados por vírgula: ")

    # Separa os itens com base na vírgula e remove espaços em branco
    lista = [item.strip() for item in itens.split(',')]

    # Imprime os itens usando um loop
    for i, item in enumerate(lista, start=1):
        print(f"Item {i}: {item}")

# Exemplo de uso da função
lista_de_compras()


def celsius_para_fahrenheit():
    # Solicita ao usuário a temperatura em Celsius
    celsius = float(input("Digite a temperatura em graus Celsius: "))

    # Converte a temperatura para Fahrenheit usando a fórmula de conversão
    fahrenheit = (celsius * 9/5) + 32

    # Imprime o resultado da conversão
    print(f"A temperatura em Fahrenheit é: {fahrenheit}°F")

# Exemplo de uso da função
celsius_para_fahrenheit()


def pedir_nomes():
    nomes = []  # Inicializa uma lista vazia para armazenar os nomes
    while True:
        nome = input("Digite um nome (ou 'sair' para sair): ")
        if nome.lower() == 'sair':
            break  # Sai do loop se 'sair' for digitado
        nomes.append(nome)  # Adiciona o nome à lista

    # Imprime todos os nomes digitados, cada um em uma linha
    for nome in nomes:
        print(nome)

# Exemplo de uso da função
pedir_nomes()