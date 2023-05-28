# from bs4 import BeautifulSoup
#
# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title.string)
#
# # print(soup.prettify())
#
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
#
# # for i in all_anchor_tags:
# #     print(i)
#
# class_is_heading = soup.find_all(class_= "heading")
# # print(class_is_heading)
#
# # h3_heading = soup.find_all("h3", class_="heading")
#
# name = soup.select_one("#name")
# print(name)
#
# headings = soup.select(".heading")
# print(headings)


import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)



heading_list = []
link_list = []
score_list = []
all_headings = soup.find_all(class_="titleline")

for heading in all_headings:
    heading_list.append(heading.a.text)
    link_list.append(heading.a.get("href"))

score = [score_list.append(int(i.text.split(" ")[0])) for i in soup.find_all(name="span", class_="score")]
print(score_list)

index_highest_up = 0
for i in range(len(score_list)):
    if score_list[i] > score_list[index_highest_up]:
        index_highest_up = i
print(heading_list[index_highest_up], link_list[index_highest_up], score_list[index_highest_up])

# for child in all_headings:
#     print(child.a)
    # print("hi")






































