#---------------------------------------
#  User Experience
#    Student C
#---------------------------------------


#---------------------------------------

def choose_difficulty():
    """
    Allows players to choose the difficulty level of the questionsThe user is going to input their choice.

    Parameters: None
    Returns:
    - str: Valid difficulty levels are ('easy', 'medium', 'hard').
    """
    #------------------------
import random

def play_game(difficulty_level):
    base_points = 100

    if difficulty_level == "easy":
        points_multiplier = 0.8
    elif difficulty_level == "medium":
        points_multiplier = 1.0
    elif difficulty_level == "hard":
        points_multiplier = 1.2
    else:
        print("Invalid difficulty level. Defaulting to medium.")
        points_multiplier = 1.0

    final_points = int(base_points * points_multiplier)

    player_score = random.randint(1, 100)

    player_score *= points_multiplier

    print(f"Player score: {player_score} points (Difficulty: {difficulty_level.capitalize()})")

# Example usage:
chosen_difficulty = input("Choose difficulty level (easy/medium/hard): ").lower()
play_game(chosen_difficulty)

    #------------------------
    #------------------------

#---------------------------------------

def display_leaderboard(leaderboard):
    """
    Displays the leaderboard, showing top scores in descending order.

    Parameters:
    - leaderboard (dict): A dictionary containing player names as keys and their scores as values.

    Returns: None

    The function sorts the leaderboard by scores in descending order and prints the names and scores of the top players. If the leaderboard is empty, it prints a message indicating that there are no scores to display.
    """
    #------------------------
def display_leaderboard(scores):
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    print("Leaderboard:")
    print("Rank\tPlayer\tScore")
    for rank, (player, score) in enumerate(sorted_scores, start=1):
        print(f"{rank}\t{player}\t{score} points")

# Example usage:
example_scores = {
    "Player1": 120,
    "Player2": 90,
    "Player3": 150,
    "Player4": 110,
    "Player5": 80
}

display_leaderboard(example_scores)
    #------------------------
    #------------------------

#---------------------------------------

def save_score(player_name, score, file_path='scores.txt'):
    """
    Saves the player's score to a file.

    Parameters:
    - player_name (str): The name of the player.
    - score (int): The score achieved by the player.
    - file_path (str): The file path to save the score.

    Returns: None
    """
    #------------------------
def save_score(player_name, score):
    try:
        with open("leaderboard.txt", "a") as file:
            file.write(f"{player_name}: {score} points\n")
        print("Score saved successfully.")
    except Exception as e:
        print(f"Error saving score: {e}")

player_name = "Player1"
player_score = 120

save_score(player_name, player_score)

    #------------------------
    #------------------------

#---------------------------------------

def load_top_scores(file_path='scores.txt'):
    """
    Loads the top scores from a file into a leaderboard dictionary.

    Parameters:
    - file_path (str): The file path from which to load the scores.

    Returns:
    - dict: The leaderboard dictionary with player names as keys and scores as values.
    """
    #------------------------
def load_top_scores(file_path, num_top_scores=5):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()

            scores = {}
            for line in lines:
                parts = line.strip().split(":")
                if len(parts) == 2:
                    player_name = parts[0].strip()
                    score = int(parts[1].split(" ")[0].strip())
                    scores[player_name] = score

            sorted_scores = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True)[:num_top_scores])

            return sorted_scores
    except Exception as e:
        print(f"Error loading top scores: {e}")
        return {}



top_scores = load_top_scores(file_path, num_top_scores_to_load)
print("Top Scores:")
for player, score in top_scores.items():
    print(f"{player}: {score} points")
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def provide_feedback(is_correct):
    """
    Provides feedback to the player after each round.

    Parameters:
    - is_correct (bool): Indicates whether the player's answer was correct.

    Returns: None

    Example:
    - is it correct?   "Well done!"
    - is it incorrect? "Sorry, that's incorrect."
    """
    #------------------------
def give_feedback(player_score, target_score):
    threshold = 80

    if player_score >= target_score:
        print("Great job! You beat the target score.")
    elif player_score >= threshold:
        print("Good effort! You're getting closer to the target.")
    else:
        print("Try again! You can do better next time.")



give_feedback(player_score, target_score)
    #------------------------
    #------------------------

#---------------------------------------

def fifty_fifty_lifeline(correct_answer, options):
    """
    Provides a 50/50 lifeline by removing two incorrect answers, leaving the correct answer and one other incorrect answer.

    Parameters:
    - correct_answer (str): The correct answer to the current question.
    - options (list): A list containing all possible answers including the correct answer.

    Returns:
    - list: A reduced list of answers containing only the correct answer and one randomly selected incorrect answer.

    This function is designed to be used once per game session by a player who chooses to use the 50/50 lifeline. It randomly selects one incorrect answer to keep along with the correct answer and removes the other options.
    """
    #------------------------
import random

def fifty_fifty_lifeline(question, options, correct_answer):
    incorrect_answers = [option for option in options if option != correct_answer]

    answers_to_remove = random.sample(incorrect_answers, 2)

    print(question)
    for option in options:
        if option not in answers_to_remove:
            print(option)

    remaining_options = [option for option in options if option not in answers_to_remove]
    return remaining_options



remaining_options = fifty_fifty_lifeline(question_text, answer_options, correct_answer)

player_input = input("Enter your answer: ")
if player_input.lower() == correct_answer.lower():
    print("Correct!")
else:
    print("Incorrect. The correct answer is:", correct_answer)
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def skip_question(allowed_skips):
    """
    Allows the player to skip a question during the game.

    Parameters:
    - allowed_skips (int): The number of skips available to the player.

    Returns:
    - bool: True if the skip was successful (and a skip was available), False otherwise.

    This function checks if the player has any skips available. If so, it decrements the allowed_skips counter and returns True, indicating the question can be skipped. If no skips are available, it returns False. This function should be called before presenting a new question to the player.
    """
    #------------------------
def skip_question(current_question, remaining_skips):
    if remaining_skips > 0:
        print("You have a skip available. Do you want to use it for the following question?")
        print(current_question)
        user_input = input("Enter 'yes' to skip or 'no' to answer: ").lower()

        if user_input == 'yes':
            print("You've chosen to skip this question.")
            remaining_skips -= 1
            return None, remaining_skips
        elif user_input == 'no':
            return "Continue playing", remaining_skips
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            return skip_question(current_question, remaining_skips)
    else:
        print("You've already used your one-time skip. Please answer the question.")
        return "Continue playing", remaining_skips

remaining_skips = 1

question1 = "What is the capital of Italy?"
question2 = "Who wrote 'Romeo and Juliet'?"

print("Player's turn:")
response, remaining_skips = skip_question(question1, remaining_skips)
print(response)

print("Player's turn:")
response, remaining_skips = skip_question(question2, remaining_skips)
print(response)
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------



