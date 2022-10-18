from flask import Flask, jsonify
import utils

app = Flask(__name__)


@app.route("/movie/<title>")
def found_by_title(title):
    """Вьюшка поиска по названию"""
    found_movies = utils.search_movie_by_title(title)
    return jsonify(found_movies)


@app.route("/rating/<rating>")
def found_by_rating(rating):
    """Вьюшка поиска по рейтингу"""
    found_movies = utils.search_by_rating(rating)
    return jsonify(found_movies)


@app.route("/movie/<int:start_year>/to/<int:end_year>")
def found_by_year(start_year, end_year):
    """Вьюшка поиска по годам"""
    found_movies = utils.search_by_years(start_year, end_year)
    return jsonify(found_movies)


@app.route("/genre/<genre>")
def found_by_genre(genre):
    """Вьюшка поиска по жанру"""
    found_movies = utils.search_by_genre(genre)
    return jsonify(found_movies)

app.run()