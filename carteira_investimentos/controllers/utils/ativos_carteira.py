from carteira_investimentos.controllers.crud.ativos_carteira_controllers import AtivosCarteiraService

from carteira_investimentos.schemas.schemas import AtivosCarteiraCreate, OperacaoCreate


class AtivosUtils:
    def __init__(self, id_carteira: str):
        self.id_carteira = id_carteira
    
    async def cadastrar_ativos_carteira(self, dados_ativo: OperacaoCreate):
        #criando um objeto para gravar este dado
        ativos_create = AtivosCarteiraCreate(
            codigo_ativo=dados_ativo.codigo_ativo,
            preco_medio=dados_ativo.quantidade_ativo * dados_ativo.valor_operacao,
            quantidade_ativos=dados_ativo.quantidade_ativo,
            preco_atual=0,
            status_em_carteira=True
        )
        result = await AtivosCarteiraService.select_ativos_carteira(self.id_carteira)
        if not any(ativos_create.codigo_ativo in vars(ativo).values() for ativo in result):
            await AtivosCarteiraService.create_ativos_carteira(self.id_carteira, ativos_create)
        else:
            for ativo in result:
                if ativos_create.codigo_ativo in ativo.codigo_ativo:
                    if dados_ativo.tipo_operacao == "COMPRA":
                        ativo.quantidade_ativos += ativos_create.quantidade_ativos
                        ativo.preco_medio += ativos_create.preco_medio
                    elif dados_ativo.tipo_operacao == "VENDA":
                        ativo.quantidade_ativos -= ativos_create.quantidade_ativos
                        ativo.preco_medio -= ativos_create.preco_medio
                    if ativo.quantidade_ativos <= 0:
                        ativo.status_em_carteira = False
                    await AtivosCarteiraService.update_carteira_id(id_ativo=ativo.id, ativos_carteira=ativo)