import requests,json
from pprint import pprint

acoes_disponiveis = {
    'NYSE': ['AAPL', 'IBM', 'GOOGL', 'MSFT', 'TSLA'],
    'NASDAQ': ['AMZN', 'FB', 'NFLX', 'NVDA', 'TSLA'],
    'B3': ['PETR3.SA', 'VALE3.SA', 'ITUB4.SA', 'ABEV3.SA', 'BBAS3.SA']
}

def obterDadosAcao(simbolo, chaveApi):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={simbolo}&apikey={chaveApi}'
    resposta = requests.get(url)
    
    if resposta.status_code != 200:
        print(f"Erro ao acessar a API: {resposta.status_code}")
        return None
    
    dados = resposta.json()
    
    if 'Error Message' in dados:
        print("Erro: A ação não foi encontrada.")
        return None

    return dados

def exibirDados(dados):
    pprint(dados)

def escolherBolsa():
    print("Escolha a bolsa:")
    print("1. NYSE (Nova Iorque)")
    print("2. NASDAQ")
    print("3. B3 (Brasil)")

    opcao = input("Digite o número da bolsa: ")
    
    if opcao == '1':
        return 'NYSE'
    elif opcao == '2':
        return 'NASDAQ'
    elif opcao == '3':
        return 'B3'
    else:
        print("Opção inválida. Usando NYSE como padrão.")
        return 'NYSE'

def exibirAcoesDisponiveis(bolsa):
    print(f"Ações disponíveis na bolsa {bolsa}:")
    for acao in acoes_disponiveis[bolsa]:
        print(f"- {acao}")

def main():
    chaveApi = 'F9FKRPU5HV42YER2'
    bolsa = escolherBolsa()
    
    exibirAcoesDisponiveis(bolsa)
    
    simbolo = input("Digite o símbolo da ação: ")
    
    dadosAcao = obterDadosAcao(simbolo, chaveApi)

    if dadosAcao:
        exibirDados(dadosAcao)

if __name__ == '__main__':
    main()
