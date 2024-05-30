# Odyssey Project

Welcome to the Odyssey Project!

## Project Description


## Installation

To install the Odyssey Project, follow these steps:

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your_username/odyssey-project.git
Navigate to the project directory:
bash
Copy code
cd odyssey-project
Install the required dependencies using pip:
bash
Copy code
pip install -r requirements.txt
Running the Project
To run the Odyssey Project, execute the following command:

bash
Copy code
python app.py
The project will be available at http://127.0.0.1:5000/ by default.

File Structure
The file structure of the Odyssey Project is as follows:

app.py: Main file for running the project.
requirements.txt: File containing the required dependencies.
templates/: Directory containing HTML templates.
static/: Directory containing static files such as CSS and JavaScript.
data/: Directory for storing data used by the project.
tests/: Directory containing test files.


Testare
Pentru a testa API-ul, puteți folosi o aplicație client REST, cum ar fi Postman, sau puteți face solicitări direct din codul Python. De asemenea, puteți folosi curl într-un terminal pentru a face solicitări către API:

Pentru a obține toate filmele: http://127.0.0.1:5000/movies
Pentru a obține un film specific:
 http://127.0.0.1:5000/movies/<titlu_film>

 -X PUT -H "Content-Type: application/json" -d '{"key": "value"}' http://127.0.0.1:5000/movies/<titlu_film>
Pentru a șterge un film:
-X DELETE http://127.0.0.1:5000/movies/<titlu_film>
Pentru a adăuga un film nou:
 -X POST -H "Content-Type: application/json" -d '{"key": "value"}' http://127.0.0.1:5000/movies
