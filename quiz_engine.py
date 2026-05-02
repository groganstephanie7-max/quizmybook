def run_quiz(questions):
    score = 0
    total = len(questions)
    missed_questions = []

    for question_data in questions:
        print("\n" + question_data["question"])

        for choice in question_data["choices"]:
            print(choice)

        print()

        while True:
            user_answer = input("Your answer, type 'hint', or type 'exit': ").strip().upper()

            if user_answer == "EXIT":
                print("\nQuiz ended early.")
                print("Your score:", score, "out of", total)

                return {
                    "status": "exit",
                    "score": score,
                    "total": total,
                    "missed_questions": missed_questions
                }

            elif user_answer == "HINT":
                print("Hint:", question_data["hint"])
                print()

            elif user_answer in ["A", "B", "C", "D"]:
                break

            else:
                print("Please enter A, B, C, D, type 'hint', or type 'exit'.")
                print()

        if user_answer == question_data["answer"]:
            print("Correct! Great job.")
            score += 1
        else:
            print("Good try — this one is tricky.")
            print("The correct answer is:", question_data["answer"])
            missed_questions.append(question_data)

        print("Explanation:", question_data["explanation"])

    print("\nQuiz complete!")
    print("Your score:", score, "out of", total)

    if score == total:
        print("Perfect score! Excellent work.")
    elif score >= total / 2:
        print("Good job. Keep practicing.")
    else:
        print("Keep going. Every attempt helps you learn.")

    return {
        "status": "complete",
        "score": score,
        "total": total,
        "missed_questions": missed_questions
    }