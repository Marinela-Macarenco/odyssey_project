import requests
from bs4 import BeautifulSoup
import json
def scrape_movies(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.find_all('h3', class_='ipc-title__text')
        durations = soup.find_all('span', class_='sc-b189961a-8 kLaxqf cli-title-metadata-item')
        years = soup.find_all('span', class_='sc-b189961a-8 kLaxqf cli-title-metadata-item')
        
        movie_info_list = []
        for title, duration, year in zip(titles, durations, years):
            title_text = title.text.strip()
            duration_text = duration.text.strip()
            year_text = year.text.strip()  # Am presupus că acest element conține anul filmului
            
            movie_info_list.append({'title': title_text, 'duration': duration_text, 'year': year_text})
        
        return movie_info_list
    else:
        print("Failed to retrieve data from IMDb.")
def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
# Test the function
url = "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"
movies_info = scrape_movies(url)
if movies_info:
    save_to_json(movies_info, 'imdb_movies_info.json')
    print("Movie information saved successfully!")
else:
    print("No movie information found.")
