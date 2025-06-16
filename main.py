<<<<<<< HEAD
from funcs import buscar_Filme_Retorna_JSON, criarCSV, criar_DataFrame_Excel

tituloFilme = input('Escreva o nome de um filme:')

dados_Do_Filme_JSON = buscar_Filme_Retorna_JSON(tituloFilme)

if dados_Do_Filme_JSON != None:
     criar_DataFrame_Excel(dados_Do_Filme_JSON)
     criarCSV(dados_Do_Filme_JSON)


=======
from funcs import buscar_Filme_Retorna_JSON, criarCSV, criar_DataFrame_Excel

tituloFilme = input('Escreva o nome de um filme:')

dados_Do_Filme_JSON = buscar_Filme_Retorna_JSON(tituloFilme)

if dados_Do_Filme_JSON != None:
     criar_DataFrame_Excel(dados_Do_Filme_JSON)
     criarCSV(dados_Do_Filme_JSON)
>>>>>>> 9f51d3926c0496b71156d94b52ad834cdbd9945e
