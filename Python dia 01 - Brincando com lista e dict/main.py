import os

# Inicializa a lista de mensagens
mesagens = []

os.system("cls")

nome = input("Nome: ")

# Inicia um loop infinito para o chat
while True:
    
    os.system("cls")
    
    # Verifica se a lista de mensagens tem algum item
    if (0 < len(mesagens)):
        # Caso tenha, imprime todas as mensagens
        for msg in mesagens:
            print(msg['nome'] + ": " + msg['mensagem'])
            
    
    texto = input("Digite uma mensagem: ")
    
    if (texto == 'sair'):
        print("Saindo...", mesagens)
        break
    
    # Adiciona a mensagem digitada na lista de mensagens
    mesagens.append({
        'nome': nome, 
        'mensagem': texto
    })
    