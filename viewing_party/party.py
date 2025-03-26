# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
    if None in (title, genre, rating):
        return None
    
    return {
        "title": title,
        "genre": genre,
        "rating": rating
    }

def add_to_watched(user_data, movie):
    copy_user_data = dict(user_data)
    copy_user_data["watched"].append(movie)
    return copy_user_data

def add_to_watchlist(user_data, movie):
    copy_user_data = dict(user_data)
    copy_user_data["watchlist"].append(movie)
    return copy_user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    if len(user_data["watched"]) == 0:
        return 0.0
    
    total_rating = 0.0
    for movie in user_data["watched"]:
        total_rating += movie["rating"]
        
    average_rating = total_rating / len(user_data["watched"])
    return average_rating
        
def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None

    genre_counts = {}

    for movie in user_data["watched"]:
        genre_counts[movie["genre"]] = genre_counts.get(movie["genre"], 0) + 1

    return max(genre_counts, key=genre_counts.get)

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    unique_watched_user_movies = []
    for user_movie in user_data["watched"]:
        none_unique_movie = 0
        for friend in user_data["friends"]:
            for friend_movie in friend["watched"]:
                if user_movie["title"] == friend_movie["title"]:
                    none_unique_movie =+ 1
        if none_unique_movie == 0:
            if user_movie not in unique_watched_user_movies:
                unique_watched_user_movies.append(user_movie)
    return unique_watched_user_movies

def get_friends_unique_watched(user_data):
    unique_watched_friends_movies = []

    for friend in user_data["friends"]:
        
        for friend_movie in friend["watched"]:
            none_unique_movie = 0
            for user_movie in user_data["watched"]:
                if friend_movie["title"] == user_movie["title"]:
                    none_unique_movie =+ 1

            if none_unique_movie == 0:
                if friend_movie not in unique_watched_friends_movies:
                    unique_watched_friends_movies.append(friend_movie)
    
            
    return unique_watched_friends_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    unique_watched_friends_movie = get_friends_unique_watched(user_data)
    recommended_movies = []

    for friend_movie in unique_watched_friends_movie:
        #friend_movie => {'title': 'The Lord of the Functions: The Fellowship of the Function', 'genre': 'Fantasy', 'rating': 4.8, 'host': 'netflix'}
        if friend_movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(friend_movie)
    return recommended_movies


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    unique_watched_friends_movie = get_friends_unique_watched(user_data)
    recommended_movies = []
    
    # calculate genre
    genre_count = {}
    for user_movie in user_data["watched"]:
        if user_movie["genre"] in genre_count:
            genre_count[user_movie["genre"]] += 1
        else:
            genre_count[user_movie["genre"]] = 0

    # find max genre
    max_genre_count = 0 
    favorite_genre = ""

    for genre, count in genre_count.items():
        if count > max_genre_count:
            favorite_genre = genre
            max_genre_count = count
    
    # find friends movie that equel favorite genre
    for friends_movie in unique_watched_friends_movie:
        if favorite_genre == friends_movie["genre"]:
            recommended_movies.append(friends_movie)
            
    return recommended_movies

def get_rec_from_favorites(user_data):
    unique_watched_user_movie = get_unique_watched(user_data)
    result = []
    for user_movie in unique_watched_user_movie:
        if user_movie in user_data["favorites"]:
            result.append(user_movie)
    return result