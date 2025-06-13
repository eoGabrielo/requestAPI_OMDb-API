import pandas as pd
import requests

#API key to link registration
apiKey = '91fbd453'

titleMovie = input('Write title movie: ')

def searchMovie(title):
    # URL-API with your key and title
    url = f'http://www.omdbapi.com/?apikey={apiKey}&t={title}'

    # request API, check StatusCode
    response = requests.get(url)
    #print(f"RESPONSE -> {response}")

    # Code Status
    statusCode = response.status_code
    #print(f"{statusCode}")

    # Convert to JSON
    dataJson = response.json()
    if response.status_code == 200 and dataJson.get('Title') == None:
        print(f"Movie not found, are you sure that's the name? -> {title} ")
        return None
    elif response.status_code == 401:
        print(f"Error request code: {response.status_code} Unauthorized")
        return None
    elif response.status_code == 504:
        print(f"Error request code: {response.status_code} server error")
        return None
    elif response.status_code == 200:
        print(f"Film [{dataJson['Title']}] successfully found\n")
    return dataJson

#Saved return JSON for convert to DATAFRAME and CSV
dataJsonMovie = searchMovie(titleMovie)

#Convert JSON in DATAFRAME
dataFrame = pd.DataFrame(dataJsonMovie)

def createCsvFile(dfMovie):
    with open(f"{dfMovie['Title']}.csv", mode='w', encoding='utf-8') as f:
        for key, value in dfMovie.items():
            f.write(f"{key}: {value}\n")

#Create table with DATAFRAME
if dataJsonMovie != None:
    #Create Excel and Csv file
    dataFrame.to_excel(f"{dataJsonMovie['Title']}.xlsx")
    createCsvFile(dataJsonMovie)
    print(f'Title: {dataJsonMovie.get("Title")}')
    print(f'Year: {dataJsonMovie.get("Year")}')
    print(f'Director: {dataJsonMovie.get("Director")}')
    print(f'Genre: {dataJsonMovie.get("Genre")}')
    print(f'Score IMDb: {dataJsonMovie.get("imdbRating")}\n')
    print(f"EXCEL and CSV file created in this folder with successfully, named as {dataJsonMovie.get('Title')}.xlsx/csv")
