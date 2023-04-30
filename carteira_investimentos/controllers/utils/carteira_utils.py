from carteira_investimentos.controllers.crud.operacao_controllers import OperacaoService


class CarteiraUtils:

    async def calc_total_investido(valor_atual: float):
        valor_investido = await OperacaoService.select_operacao()
        for valor in valor_investido:
            valor_atual += valor.valor_operacao * valor.quantidade_ativo
        return valor_atual
    
    async def calc_total_quantidade_ativos(valor_atual: int):
        pass
         # for ativos in carteira_result.operacao:
            #     lista_ativos = await AtivosCarteiraService.select_ativos_carteira(id_carteira=id_carteira)
            #     if not any(ativos.codigo_ativo in vars(ativo).values() for ativo in lista_ativos):
            #         ativos_carteira = AtivosCarteiraCreate(
            #             codigo_ativo=ativos.codigo_ativo,
            #             quantidade_ativos=0,
            #             status_em_carteira=1
            #         )
            #         await AtivosCarteiraService.create_ativos_carteira(
            #             id_carteira=id_carteira,
            #             ativos_carteira=ativos_carteira
            #         )
            # lista_ativos = await AtivosCarteiraService.select_ativos_carteira(id_carteira=id_carteira)
            # for ativos in lista_ativos:
            #     for ativos_operacao in carteira_result.operacao:
            #         if ativos.codigo_ativo == ativos_operacao.codigo_ativo and ativos_operacao.tipo_operacao == "COMPRA":
            #             ativos.quantidade_ativos += ativos_operacao.quantidade_ativo
            #         elif ativos.codigo_ativo == ativos_operacao.codigo_ativo and ativos_operacao.tipo_operacao == "VENDA":
            #             ativos.quantidade_ativos -= ativos_operacao.quantidade_ativo
            #     ativos_carteira = AtivosCarteiraCreate(
            #         codigo_ativo=ativos.codigo_ativo,
            #         quantidade_ativos=ativos.quantidade_ativos,
            #         status_em_carteira=1
            #     )
            #     print(ativos_carteira)
            #     print(carteira_result.ativos_carteira)