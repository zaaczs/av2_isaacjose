import unittest

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
        resposta_banco = solicitar_aprovacao_pagamento_banco(detalhes_cartao, valor_pagamento, conta_corrente)

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

def solicitar_aprovacao_pagamento_banco(detalhes_cartao, valor_pagamento, conta_corrente):
    # Simula a solicitação de aprovação do pagamento ao banco
    if valor_pagamento <= user_to_account(conta_corrente)['saldo']:
        return "aprovado"
    else:
        return "rejeitado"

# Função lambda para fechar uma transação
close_transaction = lambda: None  # Aqui você pode adicionar a lógica de fechamento da transação

# Classe de Teste
class TestFluxos(unittest.TestCase):
    
    # Teste para processar pagamento em dinheiro
    def test_pagamento_dinheiro(self):
        resultado = processar_pagamento("dinheiro", 50.00, "conta1")
        self.assertTrue(resultado())

    # Teste para processar pagamento com cartão de crédito aprovado
    def test_pagamento_cartao_aprovado(self):
        resultado = processar_pagamento("cartao_de_credito", 100.00, "conta2")
        self.assertTrue(resultado())

    # Teste para processar pagamento com cartão de crédito não aprovado
    def test_pagamento_cartao_nao_aprovado(self):
        resultado = processar_pagamento("cartao_de_credito", 1500.00, "conta3")
        self.assertFalse(resultado())

# Execução dos testes
if __name__ == '__main__':
    unittest.main()
