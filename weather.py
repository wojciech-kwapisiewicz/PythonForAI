import requests


# city = "Warsaw"
# countryCode = "PL"
# https://geocoding-api.open-meteo.com/v1/search?name=Warsaw&countryCode=PL
def get_coordinates(city, country_code):
    city_request_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&countryCode={country_code}"
    city_request_response = requests.get(city_request_url)
    city_request_data = city_request_response.json()
    # print(city_request_response.status_code)
    # print(city_request_data)
    return city_request_data["results"][0]["latitude"], city_request_data["results"][0][
        "longitude"
    ]


def get_weather(latitude, longitude):
    wather_request_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"
    wather_request_response = requests.get(wather_request_url)
    wather_request_data = wather_request_response.json()
    return wather_request_data["current"]["temperature_2m"], wather_request_data[
        "current_units"
    ]["temperature_2m"]


city = "Warsaw"
countryCode = "PL"

lat, lng = get_coordinates(city, countryCode)
# print(lng)
# print(lat)

temerature, unit = get_weather(lat, lng)
print(f"For {city}, {countryCode}, {lng} {lat}\nTemperature is now {temerature} {unit}")


# url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"
