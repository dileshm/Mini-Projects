import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(res.text, "html.parser")
links = soup.select(".titleline")
votes = soup.select(".score")


def create_custom_hn(links, votes):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get("href", None)
        vote = subtext[idx].get(".score")
        if len(vote):
            points = int(votes[idx].getText().replace("points", ""))
            print(points)
            title = links[idx].getText()
            hn.append({"title":
                       title, "link": href})
    return hn


print(create_custom_hn(links, votes))
