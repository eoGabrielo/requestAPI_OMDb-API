import requests
import pandas as pandas
#API key to link registration
API_KEY = '91fbd453'

movieTitle = input("Enter movie name: ")

#URL-API with your key and title
url = f'http://www.omdbapi.com/?apikey={API_KEY}&t={movieTitle}'
#request API
response = requests.get(url)
#Convert requst in json
data = response.json()

#Data movie JSON
dataMovie = {
        'Title': data.get('Title'),
        'year': data.get('Year'),
        'Director': data.get('Director'),
        'Gender:': data.get('Genre'),
        'Score IMDb': data.get('imdbRating')
}

#If the request is completed with code 200
if response.status_code == 200 and data.get('Title') == None:
    print("Movie not found ")
    #Set name to file if Title == None
    nameFile = None
elif response.status_code == 200:
    # Convert json in DataFrama to table
    dataframe = pandas.DataFrame(data)
    # Create dataframe table in Excel
    dataframe.to_excel(f"{dataMovie['Title']}.xlsx")
    # Set name to file csv
    nameFile = f"{dataMovie['Title']}.csv"
    print("")
    print("Connection 200 successful...\n")
    # verify json - print(f"{data}")
    print(f"Title: {data.get('Title')}")
    print(f"year: {data.get('Year')}")
    print(f"Director: {data.get('Director')}")
    print(f"Gender: {data.get('Genre')}")
    print(f"Score IMDb: {data.get('imdbRating')}\n")
    print(dataframe)
elif response.status_code == 401:
    print(f"Error request code: {response.status_code} Unauthorized")
elif response.status_code == 504:
    print(f"Error request code: {response.status_code} server error")


#Create file and Write in Csv if the title returns correctly
if response.status_code == 200 and nameFile != None:
    with open(nameFile, mode='w', encoding='utf-8') as f:
        for key, value in dataMovie.items():
            f.write(f"{key}: {value}")
            f.write('\n')
        print(f'Table and CSV of Date of {data.get("Title")} saved in file {data.get("Title")}.xlsx/csv in this folder\n')
