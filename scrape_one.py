Python 3.13.2 (v3.13.2:4f8bb3947cf, Feb  4 2025, 11:51:10) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import pandas as pd
from bs4 import BeautifulSoup
import requests

# request website to scrape
requests.get('https://www.scrapethissite.com/pages/simple/')
<Response [200]>

# store in variable
countries=requests.get('https://www.scrapethissite.com/pages/simple/')

>>> # Parse using BeautifulSoup
>>> kurom=BeautifulSoup(countries.text)
>>> 
>>> # Locate all country data
>>> country=kurom.find_all('div', class_='col-md-4 country')
>>> 
>>> # Extract country data
>>> 
>>> data=[]
>>> 
>>> for t in country:
...     name=t.find('h3').text.strip()
...     capital=t.find('span', class_='country-capital').text.strip()
...     population=t.find('span', class_='country-population').text.strip()
...     area=t.find('span', class_='country-area').text.strip()
...     data.append({'Country Name': name,
...                 'Capital': capital,
...                 'Population': population,
...                 'Area': area
...                 })
... 
...     
>>> # Convert to data frame
>>> df1=pd.DataFrame(data)
>>> df1
             Country Name           Capital Population       Area
0                 Andorra  Andorra la Vella      84000      468.0
1    United Arab Emirates         Abu Dhabi    4975593    82880.0
2             Afghanistan             Kabul   29121286   647500.0
3     Antigua and Barbuda        St. John's      86754      443.0
4                Anguilla        The Valley      13254      102.0
..                    ...               ...        ...        ...
245                 Yemen             Sanaa   23495361   527970.0
246               Mayotte         Mamoudzou     159042      374.0
247          South Africa          Pretoria   49000000  1219912.0
248                Zambia            Lusaka   13460305   752614.0
249              Zimbabwe            Harare   11651858   390580.0

[250 rows x 4 columns]
