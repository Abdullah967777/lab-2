
import random

question = {
    "Science": [
        ("What is the chemical symbol for water?", "H2O"),
        ("What is the chemical symbol for ammonia?", "NH3"),
        ("What is the chemical symbol for glucose?", "C6H12O6"),
    ],

    "Mathematics": [
        ("What is the square root of 64?", "8"),
        ("What is the formula for (a+b)2?", "a2 + b2 + 2ab"),
        ("What is the formula for (a-b)2?", "a2 + b2 - 2ab"),
    ],

    "History": [
        ("What year did World War II end?", "1945"),
        ("Who was the first president of the United States?", "George Washington"),
        ("Which civilization built the Great Wall of China?", "Ming Dynasty"),
    ],
}

def select_random_question(category):
    if category in question:
        return random.choice(question[category])
    else:
        return "Category not found."

def check_answer(player_answer, correct_answer):
    player_answer = player_answer.lower()
    correct_answer = correct_answer.lower()
    if player_answer == correct_answer:
        return True
    else:
        return False
    
def remove_question(category, question):
    if category in question:
        if question in question[category]:
            question[category].remove(question)
            return f"Question '{question}' removed from '{category}' category."
        else:
            return f"Question '{question}' not found in '{category}' category."
    else:
        return f"Category '{category}' not found."
    
def display_question(question):
    print(question)

def accept_answer():
    return input("Your answer: ").strip()

def check_answer(player_answer, correct_answer):
    player_answer = player_answer.lower()
    correct_answer = correct_answer.lower()
    return player_answer == correct_answer

def display_correct_answer(correct_answer):
    print(f"The correct answer is: {correct_answer}")
=======
#---------------------------------------
#  Question Bank
#    Student B
#---------------------------------------

import random

# Simplified example with one category. Expand as needed.
questions = {
    "Science": [
        ("What is the chemical symbol for water?", "H2O"),
        # Add more questions as tuples (question, answer)
    ],
}

hints = {
    "Science": [
        # Pair each question with a corresponding hint.
    ],
    # Repeat for other categories as needed.
}

#---------------------------------------

def select_random_question(category):
    """
    Selects a random question from the specified category.

    Parameters:
    - category (str): The category from which to select a question.

    Returns:
    - tuple: A tuple containing the selected question (str) and its corresponding answer (str).
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def check_answer(player_answer, correct_answer):
    """
    Checks if the player's answer matches the correct answer.

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the answers match, False otherwise.
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def remove_question(category, question):
    """
    Removes a question from the list once it has been asked.

    Parameters:
    - category (str): The category from which to remove the question.
    - question (str): The question to be removed.

    Returns:
    - None
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def display_question_and_accept_answer(question):
    """
    Displays a question to the player and accepts their answer via input.

    Parameters:
    - question (str): The question to be displayed.

    Returns:
    - str: The player's answer to the question.
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def provide_hint(category, question):
    """
    Provides a hint for the given question based on its category.

    Parameters:
    - category (str): The category of the question.
    - question (str): The question for which to provide a hint.

    Returns:
    - str: The hint for the given question.
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def display_correct_answer(correct_answer):
    """
    Displays the correct answer if the player's answer is incorrect.

    Parameters:
    - correct_answer (str): The correct answer to the question.

    Returns:
    - None
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

