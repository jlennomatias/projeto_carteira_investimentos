App CarteiraInvestimentos
app para controle de ativos

Functionalidades:
    . Qualquer pessoa poderá acompanhar o preço atual dos ativos
    . Qualquer pessoa poderá cadastrar as compras e vendas dos ativos
    . Usuario:
        . atributos:
            . username
            . password
        . descrição:
            O usuario é criado ao cadastrar
    . Carteira:
        . atributos:
            . user_id
            . patrimonio
            . total_investido
            . ativos_carteira
            . operacao
        . descrição:
            A carteira é criada automaticamente, após o cadastro do usuario.
    . Ativos em carteira:
        . atributos:
            . codigo_ativo
            . preco_medio
            . quantidade_ativo
            . status_em_carteira
            . preco_atual
            . carteira_id
        . descrição:
            Os Ativos é criado automaticamente zerados, após o cadastro da carteira. Os dados são atualizados, conforme o usuario inclui um registro de operação.
    . Operacao:
        .atributos:
            . codigo_ativo
            . tipo_operacao
            . valor_operacao
            . quantidade_ativo
            . data_operacao
            . carteira_id
        . descrição:
            A operação é criada vazia, após a carteira ser criada. Os valores de operação(compra/venda), são cadastrados manualmente pelo usuario.
    . A pessoa poderá acompanhar seus ativos em tempo real pelo "ativos_carteira":
        . status(porcentagem de ganho e perda)
        . preço médio
        . dividendos recebidos
        . valor do ativo com o desconto do dividendos


Dependencias:
    . Python + FastAPI
    . Será uma API REST
    . Banco de dados: Postgresql
    . migrações: alembic
    . kubernetes para o banco de dados