
#---------------------------------------
#  Game Mechanics
#    Student A (team lead)
#---------------------------------------

def welcome_message():
    """
    Display the game's welcome message to the player.

    Parameters: None
    Returns: None
    """
    #------------------------
    def display_welcome_message():
    print("Welcome to Awesome Game!")
    print("Get ready for an exciting adventure.")
    print("Let the game begin!")

display_welcome_message()

    #------------------------
  
    #------------------------
#---------------------------------------
    
def choose_category(categories):
    """
    Ask the player to choose a quiz category from a list of categories.

    Parameters:
    - categories (list of str): A list of category names.

    Returns:
    - str: The chosen category.
    """
    #------------------------
    def ask_for_category():
    print("Please choose a category:")
    print("1. Adventure")
    print("2. Puzzle")
    print("3. Action")
    print("4. Mystery")

    while True:
        try:
            choice = int(input("Enter the number of your chosen category: "))
            if 1 <= choice <= 4:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

chosen_category = ask_for_category()
print("You chose category:", chosen_category)

    #------------------------
    #------------------------

#---------------------------------------

def display_score(score, round_number):
    """
    Display the current score and round number to the player.

    Parameters:
    - score (int): The player's current score.
    - round_number (int): The current round number.

    Returns: None
    """
    #------------------------
    def display_score_and_round(score, round_number):
    print("Current Score: {}".format(score))
    print("Round Number: {}".format(round_number))
    print("--------------------------")


    #------------------------
    #------------------------

#---------------------------------------
    
def game_over_message(final_score):
    """
    Display a "game over" message along with the player's final score.

    Parameters:
    - final_score (int): The player's final score at the end of the game.

    Returns: None
    """
    #------------------------
    def display_game_over(score):
    print("Game Over!")
    print("Final Score: {}".format(score))
    print("Thanks for playing!")


    #------------------------
    #------------------------

#---------------------------------------
    
def run_game_rounds(categories):
    """
    Implement a basic loop to run the game for 5 rounds.

    Parameters:
    - categories (list of str): A list of quiz categories.

    Returns: None
    """
    #------------------------
    def play_game():
    total_rounds = 5
    current_round = 0
    total_score = 0

    display_welcome_message()

    while current_round < total_rounds:
        current_round += 1

        display_score_and_round(total_score, current_round)

        chosen_category = ask_for_category()

        import random
        round_score = random.randint(10, 50)
        total_score += round_score

        print("You earned {} points in round {}.".format(round_score, current_round))
        print("--------------------------")

    display_game_over(total_score)

play_game()

    #------------------------
    #------------------------
quiz_categories = ["General Knowledge", "Science", "History", "Geography", "Music", "Movies", "Sports", "Literature", "Art", "Technology"]

#---------------------------------------
        
def validate_answer(player_answer, correct_answer):
  
    #------------------------
def validate_answer(player_answer, correct_answer):
    return player_answer.lower() == correct_answer.lower()

if validate_answer(player_answer, correct_answer):
    print("Correct!")
else:
    print("Incorrect. The correct answer is:", correct_answer)

    #------------------------
    #------------------------

#---------------------------------------

def update_score(score, correct):
   
    #------------------------
def validate_answer(player_answer, correct_answer):
 
    return player_answer.lower() == correct_answer.lower()

def play_quiz():
    quiz_categories = ["General Knowledge", "Science", "History", "Geography", "Music", "Movies", "Sports", "Literature", "Art", "Technology"]
    total_score = 0

    for category in quiz_categories:
        print(f"\nCategory: {category}")
        correct_answer = "Python" 
        player_answer = input("What is a popular programming language? ")

        if validate_answer(player_answer, correct_answer):
            print("Correct!")
            round_score = 10 
            total_score += round_score
        else:
            print("Incorrect. The correct answer is:", correct_answer)

    print("\nQuiz completed!")
    print("Total Score:", total_score)

# Call the play_quiz function to start the quiz game
play_quiz()

    #------------------------
    #------------------------

#---------------------------------------

def next_round(round_number):
    
    #------------------------
def validate_answer(player_answer, correct_answer):
   
    return player_answer.lower() == correct_answer.lower()

def increase_round_number(current_round):
   
    return current_round + 1

def play_quiz():
    quiz_categories = ["General Knowledge", "Science", "History", "Geography", "Music", "Movies", "Sports", "Literature", "Art", "Technology"]
    total_score = 0
    current_round = 0

    for category in quiz_categories:
        current_round = increase_round_number(current_round)
        print(f"\nRound {current_round} - Category: {category}")
        correct_answer = "Python" 
        player_answer = input("What is a popular programming language? ")

        if validate_answer(player_answer, correct_answer):
            print("Correct!")
            round_score = 10  
            total_score += round_score
        else:
            print("Incorrect. The correct answer is:", correct_answer)

    print("\nQuiz completed!")
    print("Total Score:", total_score)

play_quiz()

    #------------------------
    #------------------------

#---------------------------------------

def check_game_over(incorrect_answers):

    #------------------------
def validate_answer(player_answer, correct_answer):
    return player_answer.lower() == correct_answer.lower()

def increase_round_number(current_round):
    return current_round + 1

def play_quiz():
    quiz_categories = ["General Knowledge", "Science", "History", "Geography", "Music", "Movies", "Sports", "Literature", "Art", "Technology"]
    total_score = 0
    current_round = 0
    incorrect_answers = 0
    max_incorrect_answers = 3 

    while current_round < len(quiz_categories) and incorrect_answers < max_incorrect_answers:
        current_round = increase_round_number(current_round)
        print(f"\nRound {current_round} - Category: {quiz_categories[current_round-1]}")
        correct_answer = "Python" 
        player_answer = input("What is a popular programming language? ")

        if validate_answer(player_answer, correct_answer):
            print("Correct!")
            round_score = 10  
            total_score += round_score
        else:
            print("Incorrect. The correct answer is:", correct_answer)
            incorrect_answers += 1

    if incorrect_answers == max_incorrect_answers:
        print("\nGame Over! You reached the maximum number of incorrect answers.")
    else:
        print("\nQuiz completed!")
        print("Total Score:", total_score)

play_quiz()

    #------------------------
    #------------------------

#---------------------------------------

def restart_or_exit():
    """
    Restart the game or exit after the game is over.

    Parameters: None
    Returns: None
    """
    #------------------------
def ask_to_play_again():
    play_again = input("Do you want to play again? (yes/no): ").lower()
    return play_again == "yes"

def play_quiz():
    while True:
        quiz_categories = ["General Knowledge", "Science", "History", "Geography", "Music", "Movies", "Sports", "Literature", "Art", "Technology"]
        total_score = 0
        current_round = 0
        incorrect_answers = 0
        max_incorrect_answers = 3  # Set the maximum allowed incorrect answers

        while current_round < len(quiz_categories) and incorrect_answers < max_incorrect_answers:
            current_round += 1
            print(f"\nRound {current_round} - Category: {quiz_categories[current_round-1]}")
            correct_answer = "Python"  # Replace with actual correct answer based on your game logic
            player_answer = input("What is a popular programming language? ")

            if validate_answer(player_answer, correct_answer):
                print("Correct!")
                round_score = 10  # You can assign different scores based on the difficulty of the question
                total_score += round_score
            else:
                print("Incorrect. The correct answer is:", correct_answer)
                incorrect_answers += 1

        if incorrect_answers == max_incorrect_answers:
            print("\nGame Over! You reached the maximum number of incorrect answers.")
        else:
            print("\nQuiz completed!")
            print("Total Score:", total_score)

        if ask_to_play_again():
            print("\nRestarting the game...\n")
        else:
            print("\nThanks for playing! Goodbye!")
            break

play_quiz()

    #------------------------0
    #------------------------

#---------------------------------------
