Claro! Aqui está o **README.md completo**, no exato estilo que você pediu, adaptado ao seu **código mais recente**:

---

# Projeto: Consulta de Filmes com OMDb API

Este projeto em Python realiza requisições à OMDb API para buscar informações sobre filmes. O programa exibe os dados na tela e os salva em um arquivo `.txt` com o nome do filme de forma formatada.

## Funcionalidades

* Entrada do título do filme pelo usuário.
* Requisição HTTP à OMDb API usando o título informado.
* Tratamento de erros de conexão e filmes não encontrados.
* Impressão dos dados principais do filme no terminal.
* Salvamento das informações em um arquivo `.txt` com o nome do filme.

## Tecnologias e Bibliotecas

* **Python 3.x**
* `requests` – Para fazer requisições HTTP
* Biblioteca padrão do Python para manipulação de arquivos (`open()`)

## Estrutura de Arquivos

```
requestAPI_OMDb-API/
│
├── main.py         # Código principal da aplicação
├── README.md       # Explicação do projeto (este arquivo)
└── The Matrix.txt  # Arquivo de saída com os dados do filme (exemplo)
```

## Exemplo de Uso

```bash
$ python main.py
Enter movie name: The Matrix

Connection 200 successful
Title: The Matrix
year: 1999
Director: Lana Wachowski, Lilly Wachowski
Gender: Action, Sci-Fi
Score IMDb: 8.7

Date saved in The Matrix in file movie.txt in this folder
```

### Exemplo de Saída (`The Matrix.txt`):

```
Title: The Matrix
year: 1999
Director: Lana Wachowski, Lilly Wachowski
Gender: Action, Sci-Fi
Score IMDb: 8.7
```

## Como Executar

3. Instale as dependências:

```bash
pip install requests
```

4. Execute o script:

```bash
python main.py
```

## obter sua API Key da OMDb

1. Acesse: [https://www.omdbapi.com/apikey.aspx](https://www.omdbapi.com/apikey.aspx)
2. Você receberá sua chave por e-mail.
3. Substitua o valor da variável `API_KEY` no código:

```python
API_KEY = 'SUA_CHAVE_AQUI'
```

## Aprendizados

* Como usar bibliotecas externas como `requests`
* Como consumir APIs REST e lidar com JSON
* Como tratar erros de conexão e dados inválidos
* Como manipular arquivos com `with open()` em Python

## Possíveis Melhorias Futuras

* Exportar os dados para um banco de dados
