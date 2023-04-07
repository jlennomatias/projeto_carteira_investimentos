from carteira_investimentos.controllers.crud.operacao_controllers import OperacaoService


class CarteiraUtils:

    async def calc_total_investido(valor_atual: float):
        valor_investido = await OperacaoService.select_operacao()
        for valor in valor_investido:
            valor_atual += valor.valor_operacao
        return valor_atual