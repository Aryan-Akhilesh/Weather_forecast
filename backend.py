import requests


API_KEY = "a588171cdc4d96d36cb2cb3ef921404d"


def get_data(place, days=None, option=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    num_values = 8*days
    filtered_data = data["list"][:num_values]
    if option == "Temperature":
        # dnr is short for dictionary,it's just a variable name
        filtered_data = [dnr["main"]["temp"] for dnr in filtered_data]
    elif option == "Sky":
        filtered_data = [dnr["weather"][0]["main"] for dnr in filtered_data]
    return filtered_data


if __name__ == "__main__":
    print(get_data("tokyo", 5, "Sky"))

