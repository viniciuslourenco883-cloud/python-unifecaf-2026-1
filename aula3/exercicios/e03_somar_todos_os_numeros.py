# Enquanto o usuário não digitar 0 continue somando todos os números digitados
# n é um número informado pelo usuário
# dicas:
# - estrutura do while: while condição:
# - use input para ler o número n

trava_de_segurança= False
contador=0

while(not trava_de_segurança):
    
    numero_digitado= int(input("Digite o Valor n:"))
    
    if(numero_digitado!=0):
     soma= contador+numero_digitado
     contador=soma
     print(f"Resultado da soma:{soma}")
    
    else:
       print("Finalização da Operação!")
       trava_de_segurança= True
        
    
