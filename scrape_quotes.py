import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Website URL
url = 'http://quotes.toscrape.com'

# Step 2: Request website
response = requests.get(url)

# Step 3: Parse HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Step 4: Find all quote blocks
quotes = soup.find_all('div', class_='quote')

# Step 5: Store data
data = []

for quote in quotes:
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    tags = [tag.text for tag in quote.find_all('a', class_='tag')]
    data.append({
        'Quote': text,
        'Author': author,
        'Tags': ', '.join(tags)
    })

# Step 6: Create DataFrame
df = pd.DataFrame(data)

# Step 7: Save to Excel
df.to_excel('quotes.xlsx', index=False)

print("Data successfully scraped and saved to quotes.xlsx!")
