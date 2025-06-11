import requests
import pandas as pd

#API key to link registration
API_KEY = '91fbd453'

movieTitle = "Matrix"
    #input("Enter movie name: "))

#URL-API with your key and title
url = f'http://www.omdbapi.com/?apikey={API_KEY}&t={movieTitle}'
#request API
response = requests.get(url)
#Convert requst in json
data = response.json()
df = pd.DataFrame(data)
print(df)

#If the request is completed with code 200
if response.status_code == 200 and data.get('Title') == None:
    print("Movie not found ")
elif response.status_code == 200:
    print("Connection 200 successful")
    # verify json - print(f"{data}")
    print(f"Title: {data.get('Title')}")
    print(f"year: {data.get('Year')}")
    print(f"Score IMDb: {data.get('imdbRating')}")
elif response.status_code == 401:
    print(f"Error request code: {response.status_code} Unauthorized")
elif response.status_code == 504:
    print(f"Error request code: {response.status_code} server error")


#Data movie JSON
dataMovie = {
        'Title': data.get('Title'),
        'year': data.get('Year'),
        'Score IMDb': data.get('imdbRating')
}

#Set name file
nameFile = f"{dataMovie['Title']}.xlsx"


# create file and Write in Txt
if response.status_code == 200 and nameFile != None:
    with open(nameFile, mode='w', encoding='utf-8') as f:
        for key, value in dataMovie.items():
            f.write(f"{key}: {value}")
            f.write('\n')
        print(f'Date saved in {data.get("Title")} in file movie.txt in this folder')
df.to_excel('tabela.xlsx')
