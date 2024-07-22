import requests

# Replace with your actual API key
api_key = "46f353333322ad69b33d2a37e7671ea8"
latitude = 33.726
latitude = 73.0515

url = f"https://api.openweathermap.org/data/3.0/onecall?lat={latitude}&lon={latitude}&appid={api_key}"

response = requests.get(url)
data = response.json()

print(data)



# https://api.openweathermap.org/data/2.5/weather?lat=33.726&lon=73.0515&appid=5176bed9d49d306783dcf267da1926aa


# https://api.openweathermap.org/data/3.0/onecall?lat=33.726&lon=73.0515&exclude={part}&appid=5176bed9d49d306783dcf267da1926aa


# https://api.openweathermap.org/data/3.0/onecall?lat=33.726&lon=-94.04&appid=5176bed9d49d306783dcf267da1926aa