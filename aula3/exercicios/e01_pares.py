# Imprima todos os número de 0 a n que sejam pares
# n é um número informado pelo usuário
# dicas:
# - estrutura do for: for i in range(inicio, fim-1)
# - use input para ler o número n
# - % retorna o resto de uma divisão ( 9 % 3 == 0)

valor_n= int(input("Digite o Valor Limite:"))

for i in range(0, valor_n):
    if(i%2==0):
        print(i)
    
    
