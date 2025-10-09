import requests
from bs4 import BeautifulSoup
import pandas as pd

#scraping through urls

urls={
    'nigeria':'https://www.apple.com/ng/iphone-16/-nigeria',
    'usa':'https://www.apple.com/shop/buy-iphone/iphone-16-usa',
    'uk':'https://www.apple.com/uk/shop/buy-iphone/iphone-16-uk',
    'uae':'https://www.apple.com/ae/shop/buy-iphone/iphone-16-uae',
   'spain':'https://www.apple.com/es/shop/buy-iphone/iphone-16-spain'
}

data= []

for country, url in urls.items():
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')
    price = soup.find('span', class_='price').text.strip()
    data.append({'Country': country, 'product':'iphone 16', 'Price':price})
    
df = pd.DataFrame(data)
print(df)    