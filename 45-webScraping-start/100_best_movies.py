import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
contents = response.text

soup = BeautifulSoup(contents, "html.parser")

movies_list = []
x = soup.find_all(class_="image-container")
del x[0]
movie_index = 100
for i in x:
    movies_list.insert(0, f"{movie_index}) {i.img.get('alt')}")
    movie_index -= 1

with open("movies.txt", "w") as file:
    for i in movies_list:
        file.write(f"{i}\n")
