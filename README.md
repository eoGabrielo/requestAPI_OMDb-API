## Projeto: Consulta de Filmes com OMDb API

Este projeto em Python realiza requisições à [OMDb API](http://www.omdbapi.com/) para buscar informações sobre filmes. O programa exibe os dados na tela e os salva em um arquivo `.txt` de forma formatada.

---

### Funcionalidades

* Entrada do título do filme pelo usuário.
* Requisição HTTP à OMDb API usando o título informado.
* Tratamento de erros de conexão e filmes não encontrados.
* Impressão dos dados principais do filme no terminal.
* Salvamento das informações em um arquivo `.txt`.

---

### Tecnologias e Bibliotecas

* Python 3.x
* [`requests`](https://pypi.org/project/requests/) – Para fazer requisições HTTP
* Biblioteca padrão para manipulação de arquivos (`open()`)

---

### Estrutura de Arquivos

```
requestAPI_OMDb-API/
│
├── main.py         # Código principal da aplicação
├── README.md       # Explicação do projeto (este arquivo)
└── movie.txt       # Arquivo de saída com os dados do filme
```

---

### Exemplo de Uso

```bash
$ python main.py
Enter movie name: The Matrix

Title: The Matrix
year: 1999
Director: Lana Wachowski, Lilly Wachowski
Gender: Action, Sci-Fi
Score IMDb: 8.7

Dados salvos no arquivo The Matrix.txt
```

---

### Exemplo de Saída (`The Matrix.txt`):

```
Title: The Matrix
year: 1999
Director: Lana Wachowski, Lilly Wachowski
Gender: Action, Sci-Fi
Score IMDb: 8.7
```

---

### ⚙Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

2. Navegue até a pasta do projeto:

```bash
cd requestAPI_OMDb-API
```

3. Instale as dependências (caso ainda não tenha):

```bash
pip install requests
```

4. Execute o script:

```bash
python main.py
```

---

### Como obter sua API Key da OMDb

1. Acesse: [https://www.omdbapi.com/apikey.aspx](https://www.omdbapi.com/apikey.aspx)
2. Registre-se gratuitamente.
3. Você receberá sua chave por e-mail.
4. Substitua o valor da variável `API_KEY` no seu código:

```python
API_KEY = 'SUA_CHAVE_AQUI'
```

---

### Aprendizados

Esse projeto mostra que você entende:

* Como usar bibliotecas externas como `requests`;
* Como consumir APIs REST e lidar com JSON;
* Como tratar erros de conexão e dados inválidos;
* Como manipular arquivos com `with open()` em Python.

---

### Possíveis Melhorias Futuras

* Exportar para banco de dados SQLite

---

### Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

Se quiser, posso gerar esse `README.md` como arquivo para você. Deseja que eu gere o `.md` pronto?
