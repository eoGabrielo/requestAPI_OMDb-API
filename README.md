# Buscador de Filmes com API OMDb

Este projeto em Python permite buscar informações detalhadas de um filme através da API pública [OMDb](http://www.omdbapi.com/), exportando os dados obtidos em dois formatos: **Excel (.xlsx)** e **CSV (.csv)**.  

---

## Estrutura do Projeto

```

projeto\_filmes/
├── main.py              # Arquivo principal que executa o programa
├── funcs.py             # Arquivo com as funções auxiliares
````

---

## Como Executar

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
````

2. **Instale as dependências**:

   ```bash
   pip install pandas requests
   ```

3. **Crie a pasta onde os arquivos serão salvos**:

   ```bash
   mkdir arquivos
   ```

4. **Execute o programa**:

   ```bash
   python main.py
   ```

5. **Digite o nome do filme desejado** e os arquivos serão salvos na pasta `arquivos/`.

---

## Funcionalidades

* Busca de filme na API OMDb por título.
* Exibição de mensagem com sucesso ou erro da requisição.
* Exportação dos dados em:

  * Excel (`Tabela.xlsx`)
  * CSV (`texto.csv`)

---

## Tecnologias Utilizadas

* **Python 3**
* **Requests** – para fazer requisições HTTP
* **Pandas** – para manipulação de dados e criação do Excel
* **API OMDb** – para consulta de dados dos filmes

---

## Observações

* É necessário ter acesso à internet para que a API funcione.
* Certifique-se da chave da API: `91fbd453`

---

## Exemplo de uso

```bash
Escreva o nome de um filme: Interestelar
Filme [Interstellar], buscado com sucesso, veja seus dados na pasta arquivos!
```
