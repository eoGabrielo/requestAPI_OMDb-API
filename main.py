import requests

#API key to link registration
API_KEY = '91fbd453'


movieTitle = input("Enter movie name: ")

#URL-API with your key and title
url = f'http://www.omdbapi.com/?apikey={API_KEY}&t={movieTitle}'

#request API
response = requests.get(url)
#Convert requst in json
data = response.json()

#If the request is completed with code 200
if response.status_code == 200:
    print("Connection 200 successful")
    #verify json - print(f"{data}")
    print(f"Title: {data.get('Title')}")
    print(f"year: {data.get('Year')}")
    print(f"Director: {data.get('Director')}")
    print(f"Gender: {data.get('Genre')}")
    print(f"Score IMDb: {data.get('imdbRating')}")
else:
    print(f"Connection error {response.status_code}")
    print("404 → not found")
    print("500 → server error")
    print("401 → unauthorized")

#Data movie JSON
dataMovie = {
    'Title': data.get('Title'),
    'year': data.get('Year'),
    'Director': data.get('Director'),
    'Gender': data.get('Genre'),
    'Score IMDb': data.get('imdbRating')
}
