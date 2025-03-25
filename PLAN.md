For our notice about plan and etc... 
Tatyna:
 1. Read and make a plan
 2. Write code
 3. Revision and fix bugs

Requarements :

- check the `tests` folder, and find the test file you want to run
  - In that test file, read through each test case
    - If it is incomplete, complete the test.
        - *Is this a nominal or edge case?*
        - *What type of input do we need to test this case?*
        - *What is the expected output for the given input?*
- Remove the lines that contain `@pytest.mark.skip()` for the test(s) you want to run.
- Write code in `party.py` to pass the test in the viewing_party
- For Waves 2, 3, 4, and 5, your implementation of each of the functions should not modify `user_data`.

Wave_1:
1. `create_movie`
input:

- [ ]  create a function with 3 parametrs `create_movie`(`title`, `genre`, `rating`)
Output:
- [ ]  return a dictionary
  
Restrictions and edge case:

- If `title` is falsy, `genre` is falsy, or `rating` is falsy, this function should return `None`
- For Waves 2, 3, 4, and 5, your implementation of each of the functions should not modify `user_data`.

# code Example:
# input parameters examples: 
movie_title: 'It Came from the Stack Trace'
genre: 'Horror'
rating: '3.5'

# output example:
return create_movie => {
		"title": 'It Came from the Stack Trace'
		"genre": 'Horror'
		"rating": '3.5'
} 

# implementation


Example of plan to work with Waves:
 Input:
-  
- 

Output:
- 

Restriction/edge cases Idea!! 
-
  
code Example:




 Marina:
 1. Check virtual environment.
 2. Go to tests. CHECK TESTS FIRST. Rewrite some tests.
 3. Activate PYTEST
 4. If tests are wrong, think on it: 
 - Is it your test? Improve it! 
 - Was it given test? Change the code to go through the tests.
 1. Improve code in PARTY.PU
 2. Repeat steps until all test have been finished. 
 3. SWITCH ROLES REGULARLY, DON'T FORFET GIT PULL AND GIT PUSH.
    THE MAIN IDEA OF THIS PROJECT IS TO MASTER IN NAVIGATION OF GIT.
 4. Play testing. Using play_tester.py it was suggested to play with code.
 5. DON'T TOUCH TEST_CONSTANTS.PY.
 6.  All names of functiona are in the description. 

 WAVE 1. def create_movie(title, gender, rating)
         def add_to_watched(user_data, movie)
         def add_to_watchlist(user_data, movie)
         def watch_movie(user_data, title)

 DON'T CHANGE THE PARAMETER USER_DATA

 WAVE 2. def get_watched_avg_rating(user_data)
         def get_most_watched_genre(user_data)

 WAVE 3. def get_unique_watched(user_data)
         def get_friends_unique_watched(user_data)

 WAVE 4. def get_available_recs(user_data)

 WAVE 5. def get_new_rec_by_genre(user_data)
         def get_rec_from_favorites(user_data)

PLAN
MONDAY: study assignment, sketches.

TUESDAY: write tests and functions.

WEDNSDAY: edge check the system's functionality.

THURSDAY: reserv day.


