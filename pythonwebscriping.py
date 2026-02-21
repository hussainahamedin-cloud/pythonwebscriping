from bs4 import BeautifulSoup
import requests
import openpyxl

# Create Excel file
excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = "Movie List"

# Column names
sheet.append(["Rank", "Movie Name", "Year", "IMDB Rating"])

# Get IMDb page
response = requests.get("https://www.imdb.com/chart/top/")
soup = BeautifulSoup(response.text, "html.parser")

# Find all movies
movies = soup.find("tbody", class_="lister-list").find_all("tr")

# Get details
for movie in movies:
    rank = movie.find("td", class_="titleColumn").get_text().split(".")[0]
    name = movie.find("a").text
    year = movie.find("span").text.replace("(", "").replace(")", "")
    rating = movie.find("strong").text

    sheet.append([rank, name, year, rating])

# Save Excel file
excel.save("Movies.xlsx")

print("Excel file created successfully")