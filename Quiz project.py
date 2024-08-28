# Define the quiz questions and answers
questions = [
    "What is the correct way to declare a variable in Java",
    "Which of the following is not a Java keyword",
    "Which of these methods is used to start a thread in Java",
    "Which of the following is used to handle exceptions in Java",
    "What is the size of an int variable in Java",

]

options = [
    ["a) int num = 10","b) int num : 10","c) int num => 10","d) num int = 10"],
    ["a) static", "b)try ", "c)main ", "d) interface"],
    ["a) run() ", "b)start() ", "c)execute() ", "d) begin()"],
    ["a) try-catch", "b) throw-catch", "c) try-throw", "d) catch-throw"],
    ["a) 16 bits", "b) 32 bits", "c) 64 bits", "d)8 bits"]
]

answers = ['a', 'c', 'b', 'a', 'b']


# Function to run the quiz
def run_quiz():
    score = 0

    for i in range(len(questions)):
        # Print each question and the available options
        print(f"Q{i + 1}: {questions[i]}")
        for option in options[i]:
            print(option)

        # Get the user's answer
        answer = input("Your answer (a/b/c/d): ").lower()

        # Check if the answer is correct
        if answer == answers[i]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {answers[i]}.\n")

    # Print the final score
    print(f"Your final score is {score}/{len(questions)}")


# Start the quiz
run_quiz()
