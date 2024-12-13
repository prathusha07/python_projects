questions = [
    "What is the capital of France?",
    "Which planet is known as the Red Planet?",
    "What is the largest mammal in the world?",
    "Who wrote 'To Kill a Mockingbird'?"
]

options = [
    ["1. Berlin", "2. Madrid", "3. Paris", "4. Rome"],
    ["1. Earth", "2. Venus", "3. Mars", "4. Jupiter"],
    ["1. Elephant", "2. Blue Whale", "3. Giraffe", "4. Shark"],
    ["1. J.K. Rowling", "2. Harper Lee", "3. Mark Twain", "4. Ernest Hemingway"]
]

# List of correct answers
correct_answers = [3, 3, 2, 2]

def quiz_game():
    name = input("Enter your name: ")

    score = 0
    for i in range(len(questions)):
        print(f"\n{name}, here's your question:")
        print(questions[i])
        for option in options[i]:
            print(option)
        while True:
            try:
                answer = int(input("Enter the number of your answer: "))
                if 1 <= answer <= 4:  
                    break
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if answer == correct_answers[i]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {correct_answers[i]}")

    print(f"\n{name}, your final score is: {score}/{len(questions)}")

if __name__ == "_main_":
    quiz_game()