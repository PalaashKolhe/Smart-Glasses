import requests

api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
city = 'Waterloo'
url = api_address + city
json_data = requests.get(url).json()
#format_add = json_data['base']
#print(format_add)
formatted_data = json_data['weather'][0]['description']
current_temp = round(json_data['main']['temp']-273.15)



print(url)
print(formatted_data)
print(str(current_temp)+'°C' )

