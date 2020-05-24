import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/toptv/"
res = requests.get(url)

soup = BeautifulSoup(res.text,'lxml')

shows = soup.select('td.titleColumn')
ratings = soup.select('td.ratingColumn.imdbRating')
N = len(shows)
imdb = []
for i in range(N):
    show = shows[i].get_text()
    rating = ratings[i].get_text()
    data = {"showtitle":show, "rate":rating}
    #print("Show : "+shows[i].get_text() +"Rating "+ratings[i].get_text())
    imdb.append(data)
for item in imdb:
    print(item['showtitle'], '-', item['rate'])


# for index in range(len(shows)):
#     print(shows[0].get_text())

