import re

def extract_movie_type(entry: str) -> str:
    """Extract the type of the movie from the entry

    Args:
        entry (str): the entry from which to extract the type

    Returns:
        str: the type of the movie
    """
    # Încercați să găsiți tipul filmului folosind un set de cuvinte cheie
    keywords = ['movie', 'series', 'documentary']
    for keyword in keywords:
        if keyword.lower() in entry.lower():
            return keyword.capitalize()
    return "Unknown"

def extract_duration_period(entry: str) -> int:
    """Extract the duration of the movie from the entry

    Args:
        entry (str): the entry from which to extract the duration

    Returns:
        int: the duration of the movie in minutes
    """
  
    match = re.search(r'(\d+)\s*hour', entry, re.IGNORECASE)
    hours = int(match.group(1)) if match else 0
    match = re.search(r'(\d+)\s*min', entry, re.IGNORECASE)
    minutes = int(match.group(1)) if match else 0
    return hours * 60 + minutes  # Convertiți la minute

def extract_name(entry: str) -> str:
    """Extract the name of the movie from the entry

    Args:
        entry (str): the entry from which to extract the name

    Returns:
        str: the name of the movie
    """
    # Eliminați orice text în paranteze
    name = re.sub(r'\([^)]*\)', '', entry).strip()
    return name

def extract_genre(entry: str) -> str:
    """Extract the genre of the movie from the entry

    Args:
        entry (str): the entry from which to extract the genre

    Returns:
        str: the genre of the movie
    """
    # Eliminați genul și virgulele de la început și sfârșit
    genre = entry.strip(', ')
    return genre
