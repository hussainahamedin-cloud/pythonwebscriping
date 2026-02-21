import requests
from bs4 import BeautifulSoup
import pandas as pd

# IMDb Top Movies page
url = "https://www.imdb.com/chart/top/"

# Get webpage
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.text, "html.parser")

# Find movie items
movies = soup.select("li.ipc-metadata-list-summary-item")

titles = []
years = []
ratings = []

# Get details of first 10 movies
for movie in movies[:10]:
    titles.append(movie.select_one("h3").text)
    years.append(movie.select(".cli-title-metadata-item")[0].text)
    ratings.append(movie.select_one(".ipc-rating-star--rating").text)

# Create table
data = {
    "Title": titles,
    "Year": years,
    "Rating": ratings
}

df = pd.DataFrame(data)

# Save to Excel
df.to_excel("imdb_movies.xlsx", index=False)

print("Excel file created successfully ")