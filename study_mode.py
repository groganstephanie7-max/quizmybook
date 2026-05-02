def adjust_question_count(requested_count, total_questions, content_label="quiz"):
    if total_questions == 0:
        print(f"\nNo questions are available for this {content_label} yet.")
        return 0

    if requested_count > total_questions:
        print(f"\nThis {content_label} only has {total_questions} question(s) available.")
        print(f"Running all {total_questions} question(s).")
        return total_questions

    return requested_count


def get_question_range(total_questions):
    minimum_questions = 1
    maximum_questions = min(45, total_questions)

    return minimum_questions, maximum_questions


def choose_question_count(total_questions, content_label="quiz"):
    minimum_questions, maximum_questions = get_question_range(total_questions)

    while True:
        user_input = input(
            f"\nHow many questions do you want? Choose {minimum_questions}-{maximum_questions}, or type exit: "
        ).strip().lower()

        if user_input == "exit":
            return "exit"

        if not user_input.isdigit():
            print(f"Please enter a number from {minimum_questions} to {maximum_questions}.")
            continue

        question_count = int(user_input)

        if question_count < minimum_questions or question_count > maximum_questions:
            print(f"Please choose between {minimum_questions} and {maximum_questions} questions.")
            continue

        return adjust_question_count(question_count, total_questions, content_label)


def choose_study_minutes(total_questions, content_label="quiz"):
    while True:
        user_input = input(
            "\nHow many minutes do you want to study? Choose 1-60, or type exit: "
        ).strip().lower()

        if user_input == "exit":
            return "exit"

        if not user_input.isdigit():
            print("Please enter a number from 1 to 60.")
            continue

        minutes = int(user_input)

        if minutes < 1 or minutes > 60:
            print("Please choose between 1 and 60 minutes.")
            continue

        estimated_questions = minutes

        if estimated_questions > 45:
            estimated_questions = 45

        if estimated_questions > total_questions:
            estimated_questions = total_questions

        print(f"\nEstimated quiz length: {estimated_questions} question(s).")

        return adjust_question_count(estimated_questions, total_questions, content_label)


def choose_study_mode(total_questions, content_label="quiz"):
    if total_questions == 0:
        print(f"\nNo questions are available for this {content_label} yet.")
        return 0

    print(f"\nThis {content_label} has {total_questions} question(s) available.")
    print("\nHow do you want to study?")
    print("1. Choose number of questions")
    print("2. Choose study time in minutes")
    print("3. Use default study mode")

    while True:
        choice = input(
            "\nChoose 1, 2, or 3. You can also type exit: "
        ).strip().lower()

        if choice == "exit":
            return "exit"

        if choice == "1":
            return choose_question_count(total_questions, content_label)

        if choice == "2":
            return choose_study_minutes(total_questions, content_label)

        if choice == "3":
            default_count = min(20, total_questions)
            print(f"\nDefault study mode selected: {default_count} question(s).")
            return adjust_question_count(default_count, total_questions, content_label)

        print("Please choose 1, 2, or 3.")