# Definindo a função lambda users
users = lambda id, name, email, endereco: {'id': id, 'nome': name, 'email': email, 'endereco': endereco}

# Definindo a função lambda accounts
accounts = lambda user, saldo: {'usuario': user, 'saldo': saldo}

# Dicionário de usuários
usuarios = {
    "usuario1": users("usuario1", "João", "joao@email.com", "Rua A, 123"),
    "usuario2": users("usuario2", "Maria", "maria@email.com", "Rua B, 456"),
    "usuario3": users("usuario3", "Carlos", "carlos@email.com", "Rua C, 789"),
}

# Dicionário de contas correntes
contas_correntes = {
    "conta1": accounts(usuarios["usuario1"], 500.00),
    "conta2": accounts(usuarios["usuario2"], 1000.00),
    "conta3": accounts(usuarios["usuario3"], 750.00),
}

# Dicionário mapeando ID/login do usuário à conta corrente
user_to_account = lambda user_id: contas_correntes[user_id]

# Função lambda para atualizar o saldo da conta corrente de um usuário
update_account_balance = lambda user_id, new_balance: contas_correntes[user_id].update({'saldo': new_balance})

# Função lambda para realizar um saque em uma conta corrente
cash_withdrawal = lambda user_id, amount: update_account_balance(user_id, user_to_account(user_id)['saldo'] - amount)

# Abstração da atividade "Receive Cash"
receive_cash = lambda user_id, amount: cash_withdrawal(user_id, amount)

def processar_pagamento(tipo_pagamento, valor_pagamento, conta_corrente):
    if tipo_pagamento == "dinheiro":
        # Recebe o pagamento em dinheiro
        # Imprime o recibo
        # Retorna o pagamento
        # Completa a transação
        return lambda: True

    elif tipo_pagamento == "cartao_de_credito":
        # Solicita os detalhes do cartão de crédito ao cliente
        detalhes_cartao = solicitar_detalhes_cartao_de_credito()

        # Solicita a aprovação do pagamento ao banco
        resposta_banco = solicitar_aprovacao_pagamento_banco(detalhes_cartao, valor_pagamento)

        # Verifica a resposta do banco
        if resposta_banco == "aprovado":
            # Atualiza o saldo da conta corrente
            update_account_balance(conta_corrente, user_to_account(conta_corrente)['saldo'] - valor_pagamento)
            # Confirma o pagamento
            # Fecha a transação
            return lambda: True
        else:
            # Cancela a transação
            return lambda: False

    else:
        # Tipo de pagamento inválido
        return lambda: False

def solicitar_detalhes_cartao_de_credito():
    # Simula a solicitação dos detalhes do cartão de crédito ao cliente
    return {"numero_cartao": "1234567890123456", "cvv": "123", "data_validade": "12/25"}

def solicitar_aprovacao_pagamento_banco(detalhes_cartao, valor_pagamento):
    # Simula a solicitação de aprovação do pagamento ao banco
    return "aprovado"

# Função lambda para fechar uma transação
close_transaction = lambda: None  # Aqui você pode adicionar a lógica de fechamento da transação

# Exemplo de uso
tipo_pagamento = "cartao_de_credito"
valor_pagamento = 100.00
conta_corrente = "conta1"  # Escolha a conta corrente correspondente

resultado_pagamento = processar_pagamento(tipo_pagamento, valor_pagamento, conta_corrente)

if resultado_pagamento():
    print("Pagamento processado com sucesso!")
else:
    print("Falha no processamento do pagamento.")

# Exemplo de saque em conta corrente
saque_valor = 50.00
conta_saque = "conta1"  # Conta corrente para o saque
receive_cash(conta_saque, saque_valor)  # Realizando o saque em conta corrente

# Fechar a transação após o pagamento e o saque
close_transaction()

print(usuarios)
print(contas_correntes)
