import requests
from bs4 import BeautifulSoup

def get_data(day):
    url = "https://adventofcode.com/2025/day/{day}/input"
    cookies = {
        "session": "YOUR_SESSION_COOKIE_HERE"
    }

    response = requests.get(url.format(day=day), cookies=cookies)
    response.raise_for_status()

    return response.text.strip()

def answer(num, part, day):
    url = "https://adventofcode.com/2025/day/{day}/answer"

    cookies = {
        "session": "YOUR_SESSION_COOKIE_HERE"
    }

    payload = {
        "level": part,
        "answer" : num
    }

    response = requests.post(url.format(day=day), data=payload, cookies=cookies)

    print("Submitting answer for Day {}, Part {}: {}".format(day, part, num))
    print("Response code: " + str(response.status_code))
    html = response.text

    soup = BeautifulSoup(html, "html.parser")
    result = soup.find("main").find("article").find("p").get_text()
    return result.split(".")[0]