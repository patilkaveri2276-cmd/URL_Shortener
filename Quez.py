import json

# Load questions from file
def load_questions():
    with open("questions.json", "r") as file:
        return json.load(file)

# Quiz logic
def start_quiz():
    questions = load_questions()
    score = 0

    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        
        for option in q["options"]:
            print(option)

        answer = input("Enter your answer (A/B/C/D): ").upper()

        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

    print("\nQuiz Completed!")
    print(f"Your Score: {score}/{len(questions)}")

# Run quiz
start_quiz()
