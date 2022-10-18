import sqlite3


def load_data(sql):
    """Загрузка базы данных"""
    netflix = 'netflix.db'
    with sqlite3.connect(netflix) as connection:
        movie_data = connection.execute(sql).fetchall()
    return movie_data


def search_movie_by_title(title):
    """ПОиск фильма по названию"""
    sql = f"""
    SELECT title,country, release_year, listed_in, description
    FROM netflix
    WHERE title LIKE '%{title}%' 
    ORDER BY release_year DESC 
    LIMIT 1
    """
    found_movie = load_data(sql)[0]
    load_found_movie = {
        "title": found_movie[0],
        "country": found_movie[1],
        "release_year": found_movie[2],
        "genre": found_movie[3],
        "description": found_movie[4]
    }
    return load_found_movie


def search_by_years(start_year, end_year):
    """Поиск фильма по годам от первого года до второго"""
    sql = f"""
        SELECT title, release_year
        FROM netflix
        WHERE release_year BETWEEN {start_year} AND {end_year}  
        LIMIT 100
        """
    found_movie = load_data(sql)
    movie_list = []
    for movie in found_movie:
        load_found_movie = {
            "title": movie[0],
            "release_year": movie[1]
        }
        movie_list.append(load_found_movie)
    return movie_list


def search_by_rating(rating):
    """ПОиск фильма по рейтингу"""
    ratings = {
        "children": ('G', 'G'),
        "family": ('G', 'PG', 'PG-13'),
        "adult": ('R', 'NC-17')
    }
    sql = f"""
            SELECT title, rating, description
            FROM netflix
            WHERE rating IN {ratings[rating]}  
            """
    found_movie = load_data(sql)
    movie_list = []
    for movie in found_movie:
        load_found_movie = {
            "title": movie[0],
            "rating": movie[1],
            "description": movie[2]
        }
        movie_list.append(load_found_movie)
    return movie_list


def search_by_genre(genre):
    """Поиск фильма по жанру"""
    sql = f"""
            SELECT title, description
            FROM netflix
            WHERE listed_in LIKE '%{genre}%'
            ORDER BY release_year DESC
            LIMIT 10
            """
    found_movie = load_data(sql)
    movie_list = []
    for movie in found_movie:
        load_found_movie = {
            "title": movie[0],
            "description": movie[1]
        }
        movie_list.append(load_found_movie)
    return movie_list


def search_by_actors(actor_1, actor_2):
    """Поиск фильма по двум актерам"""
    sql = f"""
            SELECT "cast"
            FROM netflix
            WHERE "cast" LIKE '%{actor_1}%' AND "cast" LIKE '%{actor_2}%' 
            """
    found_movie = load_data(sql)
    actors_list = []
    actors_count = []
    for actors in found_movie:
        load_actors = actors[0].split(", ")
        actors_list.extend(load_actors)
    for actor in actors_list:
        if actor not in actors_count and actors_list.count(actor) > 2 \
                and actor not in [actor_1, actor_2]:
            actors_count.append(actor)
    return actors_count


def search_by_movie(movie_type, year, genre):
    """Поиск фильма по типу передачи, году и жанру"""
    sql = f"""
               SELECT title, description
               FROM netflix
               WHERE type LIKE '%{movie_type}%' 
               AND release_year = {year}
               AND listed_in LIKE '%{genre}%'
               """
    found_movie = load_data(sql)
    movie_list = []
    for movie in found_movie:
        load_found_movie = {
            "title": movie[0],
            "description": movie[1]
        }
        movie_list.append(load_found_movie)
    return movie_list

