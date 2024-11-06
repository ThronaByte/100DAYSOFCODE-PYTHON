from bs4 import BeautifulSoup
import requests
import re

yc_news = requests.get('https://news.ycombinator.com/news')
yc_article = yc_news.text

soup = BeautifulSoup(yc_article, 'html.parser')
# print(soup.prettify())
articles = soup.find_all(name='td', class_="title")
article_text = []
article_links = []
for article in articles:
    text = article.getText()
    # clean_text = text.split('. ', 1)[-1] if text[0].isdigit() else text
    clean_text = re.sub(r'^\d+\.\s*', '', text).lstrip()

    # Only add to article_text if it's non-empty after cleanup
    if clean_text:
        article_text.append(clean_text)
    # print(article_text)
    # Links
    link_tag = article.find('a')
    link = link_tag.get('href') if link_tag else None
    article_links.append(link)


article_links = [link for link in article_links if link is not None]
article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_="score")]

largest_number = max(article_upvote)
largest_index = article_upvote.index(largest_number)

print(f"{article_text[largest_index]}")
print(article_links[largest_index])
# print(article_text[1])
# print(f"Links: {article_links}\nNames: {article_text}\nScores: {article_upvote}")
# for t in article_text:
#     print(t)

#
# with open("index.html", encoding='cp850') as file:
#     content = file.read()
# soup = BeautifulSoup(content, "html.parser")
# # print(soup.prettify())
#
# all_anchor = soup.find_all(name='a')
# # print(all_anchor)
#
# # for tag in all_anchor:
# #     # print(tag.getText())
# #     print(tag.get('href'))
# heading = soup.find_all(name='h1', id="name")
#
# sec_head = soup.find(name='h3', class_="heading")
# print(sec_head.getText())
# print(sec_head.name)
# print(sec_head.get("class"))