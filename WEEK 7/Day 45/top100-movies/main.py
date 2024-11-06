import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20241007205559/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
html_file = response.text


soup = BeautifulSoup(html_file, 'html.parser')
all_movies=soup.find_all(name='h3', class_='listicleItem_listicle-item__title__BfenH')
movie_title = [movie.getText() for movie in all_movies]
movies= movie_title[::-1]
# print(movies)
with open('movies.txt', mode='w') as file:
    for movie in movies:
        # print(movie)
        file.write(f"{movie}\n")
