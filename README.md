# Projeto: Consulta de Filmes com OMDb API + Exportação para Excel e CSV

Este projeto em Python permite consultar informações detalhadas de filmes usando a **OMDb API**. A aplicação recebe o nome de um filme, realiza uma requisição à API e retorna os dados do título, como ano, diretor, gênero e nota no IMDb. Além disso, exporta os dados para **planilha Excel (`.xlsx`)** e **arquivo `.csv`** no diretório local.

## Funcionalidades

- Entrada interativa do nome do filme.
- Requisição HTTP para a OMDb API.
- Verificação do código de resposta HTTP.
- Extração e exibição de dados relevantes do filme.
- Criação de um **DataFrame** com os dados recebidos.
- Exportação para:
  - `.xlsx` (Excel)
  - `.csv` (arquivo de texto separado por vírgulas)
- Mensagens informativas para o usuário.
- Tratamento de erros HTTP (`401`, `504`).

---

## Tecnologias Utilizadas

- **Python 3.x**
- **requests** — Para realizar chamadas HTTP à API.
- **pandas** — Para manipulação de dados e exportação para Excel.
- **openpyxl** — Requisito do pandas para exportar `.xlsx`.

---

## Estrutura de Arquivos

```

consulta-filmes/
│
├── main.py           # Código-fonte principal do programa
├── README.md         # Este arquivo de explicação do projeto
├── Titanic.xlsx      # Arquivo gerado (exemplo)
└── Titanic.csv       # Arquivo gerado (exemplo)

````

---

## Exemplo de Uso

```bash
$ python main.py
Enter movie name: Titanic

Connection 200 successful...

Title: Titanic  
year: 1997  
Director: James Cameron  
Gender: Drama, Romance  
Score IMDb: 7.9  

Table and CSV of Date of Titanic saved in file Titanic.xlsx/csv in this folder
````

---

## Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/consulta-filmes.git
cd consulta-filmes
```

### 2. Instale as dependências

```bash
pip install requests pandas openpyxl
```

### 3. Execute o script

```bash
python main.py
```

---

## Como obter sua API Key da OMDb

1. Acesse: [https://www.omdbapi.com/apikey.aspx](https://www.omdbapi.com/apikey.aspx)
2. Registre-se gratuitamente e você receberá sua chave por e-mail.
3. Substitua no código:

```python
API_KEY = 'SUA_CHAVE_AQUI'
```

---

## Explicação do Código

* `requests.get(...)`: realiza a chamada HTTP para buscar os dados do filme.
* `response.json()`: transforma a resposta em um dicionário Python.
* `pandas.DataFrame(data)`: cria uma tabela com todos os dados da API.
* `to_excel(...)`: exporta os dados para um arquivo `.xlsx`.
* `with open(..., 'w')`: grava dados principais em um arquivo `.csv`.
* `print(...)`: exibe informações relevantes no terminal.

---

## Aprendizados

Este projeto demonstra o uso prático de:

* Consumo de APIs REST em Python.
* Manipulação de dados com pandas.
* Exportação de dados em formatos profissionais (CSV e Excel).
* Boas práticas no tratamento de erros HTTP.

---

## Possíveis Melhorias Futuras

* Exportar os dados para banco de dados SQLite.
