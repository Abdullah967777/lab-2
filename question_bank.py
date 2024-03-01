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