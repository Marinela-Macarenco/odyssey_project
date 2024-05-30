from flask import Flask, jsonify, request
import json

app = Flask(__name__)

DATABASE_FILE = 'imdb_movies_info.json'

def load_data():
    with open(DATABASE_FILE, 'r') as file:
        data = json.load(file)
    return data

def save_data(data):
    with open(DATABASE_FILE, 'w') as file:
        json.dump(data, file, indent=4)

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to the Movie API!'})

@app.route('/movies', methods=['GET'])
def get_all_movies():
    movies = load_data()
    return jsonify(movies)

@app.route('/movies/<title>', methods=['GET'])
def get_movie(title):
    movies = load_data()
    for movie in movies:
        if movie['title'] == title:
            return jsonify(movie)
    return jsonify({'message': 'Movie not found'}), 404

@app.route('/movies/<title>', methods=['PUT'])
def update_movie(title):
    data = request.json
    movies = load_data()
    for movie in movies:
        if movie['title'] == title:
            movie.update(data)
            save_data(movies)
            return jsonify(movie)
    return jsonify({'message': 'Movie not found'}), 404

@app.route('/movies/<title>', methods=['DELETE'])
def delete_movie(title):
    movies = load_data()
    for movie in movies:
        if movie['title'] == title:
            movies.remove(movie)
            save_data(movies)
            return jsonify({'message': 'Movie deleted successfully'})
    return jsonify({'message': 'Movie not found'}), 404

@app.route('/movies', methods=['POST'])
def add_movie():
    data = request.json
    movies = load_data()
    for movie in movies:
        if movie['title'] == data['title']:
            return jsonify({'message': 'Movie already exists'}), 400
    movies.append(data)
    save_data(movies)
    return jsonify(data), 201

if __name__ == '__main__':
    app.run(debug=True)
