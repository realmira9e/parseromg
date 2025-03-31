import requests
from bs4 import BeautifulSoup

def get_image_links(article):
    image_tag = article.find('img')
    if image_tag and 'src' in image_tag.attrs:
        return "https:" + image_tag['src']
    return "Нет изображения"

search_query = 'Банан'
base_url = 'https://ru.wikipedia.org'
search_url = f'{base_url}/w/index.php?search={search_query.replace(" ", "+")}&title=Служебная:Поиск&profile=advanced&fulltext=1&ns0=1'

response = requests.get(search_url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

article_items = soup.find_all('li', class_ = "mw-search-result")

for article in article_items[:5]:
    title_tag = article.find('div', class_="mw-search-result-heading")
    title = title_tag.text.strip() if title_tag else "Нет названия"

    data_tag = article.find('div', class_='mw-search-result-data')
    data = data_tag.text.strip() if data_tag else "Нет даты" 

    description_tag = article.find('div', class_='searchresult')
    description = description_tag.text.strip()  if description_tag else "Нет описания"

    image_link = get_image_links(article)

    print(
        f'''
Название: {title}
Вес, кол-во слов и последняя дата изменения: {data}
Описание: {description}

Ссылка на изображение: {image_link}
'''
    )