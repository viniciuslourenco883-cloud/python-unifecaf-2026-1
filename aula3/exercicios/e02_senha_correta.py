# Peça a senha ao usuário e continue pedindo até ele digitar: unifecaf
# - estrutura do while: while condição:
# - use input para ler a senha

SENHA_USUARIO= "unifecaf"

conexao_sistema= False
tentativas= 0

while(not conexao_sistema and tentativas<5):
    
    senha_digitada= str(input("Digite a Senha:"))
    
    if(senha_digitada==SENHA_USUARIO):
        print(" Acesso concedido!")
        conexao_sistema=True
        
    else:
        tentativas+= 1
        print(f"falha na conexão; tentativas: {tentativas}")