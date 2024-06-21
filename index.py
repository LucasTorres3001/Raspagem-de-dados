import requests
from bs4 import BeautifulSoup

link = 'https://www.google.com/search?q=cotacao+dolar'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}
request = requests.get(url=link, headers=headers)

site = BeautifulSoup(request.text, 'html.parser')

cotacao_dolar = site.find(name='span', class_ = 'DFlfde SwHCTb')

print(cotacao_dolar.get_text())
print(cotacao_dolar['data-value'])