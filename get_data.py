import requests

def get_data():
    day = input("Enter the day number: ")

    url = "https://adventofcode.com/2025/day/{day}/input"
    cookies = {
        "session": "YOUR_SESSION_COOKIE_HERE"
    }

    response = requests.get(url.format(day=day), cookies=cookies)
    response.raise_for_status()

    return response.text.strip()

