import requests


API_KEY = "a588171cdc4d96d36cb2cb3ef921404d"


def get_data(place, days=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    num_values = 8*days
    filtered_data = data["list"][:num_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data("tokyo", 5))

