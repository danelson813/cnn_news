from utils.util_selenium import get_soup, save_soup, retreive_soup
from utils.util import setup_logger, does_it_exist, to_sqlite3
import pandas as pd

logger = setup_logger()

url = "https://edition.cnn.com/?refresh=1"

filename = "data/soup_cnn.txt"

if does_it_exist(filename):
    soup = retreive_soup(filename=filename)
else:
    soup = get_soup(url)
    save_soup(str(soup))


articles = soup.find_all('span', class_='container__headline-text')
logger.info(f"There are {len(articles)} articles")
results = []

base = 'https://edition.cnn.com'
for article in articles:
    result = {
        'headline': article.text,
        'link': base + article.parent.parent.parent['href']
    }
    results.append(result)

df = pd.DataFrame(results)
df.to_csv('data/results.csv', index=False)

to_sqlite3(df)
