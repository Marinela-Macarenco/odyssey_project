import re
import json

def extract_movie_type(entry: str) -> str:
    match = re.search(r'\((.*?)\)', entry)
    return match.group(1) if match else "Unknown"

def extract_duration_period(entry: str) -> tuple:
    match = re.search(r'(\d+)\s*hour', entry, re.IGNORECASE)
    hours = int(match.group(1)) if match else 0
    match = re.search(r'(\d+)\s*min', entry, re.IGNORECASE)
    minutes = int(match.group(1)) if match else 0
    return hours, minutes

def extract_name(entry: str, movie_type="Unknown") -> str:
    name = entry.split('(')[0].strip()
    return name

def extract_genre(entry: str) -> str:
    genre = entry.split(',')[-1].strip()
    return genre

import unittest

class TestDataProcessing(unittest.TestCase):

    def test_extract_movie_type(self):
        self.assertEqual(extract_movie_type('(Movie)'), 'Movie')
        self.assertEqual(extract_movie_type('(Series)'), 'Series')
        self.assertEqual(extract_movie_type(''), 'Unknown')

    def test_extract_duration_period(self):
        self.assertEqual(extract_duration_period('2 hours 30 min'), (2, 30))
        self.assertEqual(extract_duration_period('1 hour 45 min'), (1, 45))
        self.assertEqual(extract_duration_period('1 hour'), (1, 0))

    def test_extract_name(self):
        self.assertEqual(extract_name('Movie Name (2023)'), 'Movie Name')
        self.assertEqual(extract_name('Another Movie (2024)'), 'Another Movie')
        self.assertEqual(extract_name('Yet Another Movie'), 'Yet Another Movie')

    def test_extract_genre(self):
        self.assertEqual(extract_genre('Action, Thriller'), 'Thriller')
        self.assertEqual(extract_genre('Drama'), 'Drama')
        self.assertEqual(extract_genre('Comedy, Drama, Romance'), 'Romance')
        
def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# Testăm funcția salvând datele procesate despre filme
processed_movies = [
    {'title': 'Movie 1', 'duration': 120, 'rating': 'R', 'genre': 'Action'},
    {'title': 'Movie 2', 'duration': 105, 'rating': 'PG-13', 'genre': 'Comedy'},
    {'title': 'Movie 3', 'duration': 120, 'rating': 'PG', 'genre': 'Drama'}
]

save_to_json(processed_movies, 'movies_database.json')

if __name__ == '__main__':
    unittest.main()
