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

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

