# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    pass

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


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