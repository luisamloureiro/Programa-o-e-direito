
a = 10
b = 5
c = 2

print(a+b)
print(b-c)
print(a*b)
print(a/c)

soma = a+b
print(soma)

# Definindo variáveis booleanas
tem_sol = True
tem_chuva = False

# Exemplo de operador 'or'
if tem_sol or tem_chuva:
    print("Vou levar guarda-chuva.")

# Exemplo de operador 'and'
if tem_sol and not tem_chuva:
    print("Vou usar protetor solar.")

# Exemplo de operador 'not'
#if not tem_chuva:
    #print("Não está chovendo.")
    
    #A ordem de precedência dos operadores lógicos em Python, do maior para o menor, é a seguinte:

# 1. `not`
# 2. `and`
# 3. `or`

# Isso significa que o operador `not` tem a maior precedência, seguido pelo `and` e, por último, pelo `or`. Quando você tem expressões lógicas com vários operadores, o Python avaliará primeiro o `not`, depois o `and` e, por fim, o `or`. 

# Por exemplo, na expressão `A or B and not C`, o `not` será avaliado primeiro, seguido pelo `and` e depois pelo `or`. 

# Você também pode usar parênteses para alterar a ordem de avaliação e tornar a expressão mais clara, assim como em expressões aritméticas.#

# Definindo variáveis booleanas

tem_sol = True
tem_chuva = False

# Exemplo com ordem modificada de operadores lógicos

if tem_sol or tem_chuva and not tem_sol:
    print("Condição verdadeira com ordem modificada.")
else:
    print("Condição falsa com ordem modificada.")
