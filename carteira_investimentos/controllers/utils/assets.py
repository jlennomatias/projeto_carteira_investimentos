from aiohttp import ClientSession


url_yahoo = "https://query1.finance.yahoo.com"

class AssetService:
    async def list_assets(symbol: str):
        async with ClientSession() as session:
            url = f'{url_yahoo}/v7/finance/quote?symbols={symbol}.SA'
            response = await session.get(url)
            dados_api = await response.json()
            print(dados_api)
            dados_api = {
                "codigo_ativo": dados_api['quoteResponse']['result'][0]['symbol'],
                "nome_ativo": dados_api['quoteResponse']['result'][0]['shortName'],
                "preco_ativo": dados_api['quoteResponse']['result'][0]['regularMarketPrice']
            }
            return dados_api