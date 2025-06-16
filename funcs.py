import requests
import pandas as pd

# API key to link registration
chave = '91fbd453'

def buscar_Filme_Retorna_JSON(titulo):
    #Url da API para digitar chave e titulo do filme
    url = f'http://www.omdbapi.com/?apikey={chave}&t={titulo}'

    #Resposta e requisiçao
    response = requests.get(url)
    json =  response.json()
    codigoDeStatus = response.status_code

    if codigoDeStatus == 200:
        print(f"Filme [{json.get('Title')}], buscado com sucesso, veja seus dados na pasta arquivos!")
        return json
    elif codigoDeStatus == 401:
        print("Não autorizado, Erro 401!")
        return None
    elif codigoDeStatus == 504:
        print("Erro no servidor, Erro 504!")
        return None

def criar_DataFrame_Excel(dadosJson):
    dataFrame = pd.DataFrame(dadosJson)
    dataFrame.to_excel('arquivos/Tabela.xlsx')


def criarCSV(dadosJson):
    with open('arquivos/texto.csv', mode='w', encoding='utf-8') as f:
        for key, value in dadosJson.items():
            f.write(f"{key}: {value}\n")
