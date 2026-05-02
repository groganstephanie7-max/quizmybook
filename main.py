import json
import os

from lessons import lessons
from quiz_engine import run_quiz
from pasted_text_quiz import create_pasted_text_questions
from source_summaries import source_summaries, show_source_summary
from internet_lookup import show_internet_summary
from internet_quiz import create_internet_summary_questions


REVIEW_BANK_FILE = "review_bank.json"
review_bank = []


def load_review_bank():
    if not os.path.exists(REVIEW_BANK_FILE):
        return []

    try:
        with open(REVIEW_BANK_FILE, "r", encoding="utf-8") as file:
            saved_questions = json.load(file)

        if isinstance(saved_questions, list):
            return saved_questions

        return []

    except json.JSONDecodeError:
        print("\nWarning: review_bank.json could not be read.")
        print("Starting with an empty review bank.")
        return []

    except FileNotFoundError:
        return []


def save_review_bank():
    with open(REVIEW_BANK_FILE, "w", encoding="utf-8") as file:
        json.dump(review_bank, file, indent=4)


def show_menu():
    print("\nWelcome to QuizMyBook!")
    print("A source-backed learning and quiz app.")
    print("-----------------------------------")
    print("1. Enter a learning topic")
    print("2. Paste study text")
    print("3. Review missed questions")
    print("4. View source-backed summaries")
    print("5. Search the internet for a topic")
    print("6. Search by book title")
    print("7. Search by ISBN/barcode")
    print("8. Exit")


def ask_return_to_menu():
    while True:
        again = input("\nReturn to the main menu? yes/no: ").strip().lower()

        if again in ["yes", "y"]:
            return True
        elif again in ["no", "n"]:
            print("\nGood job today, keep learning!")
            return False
        else:
            print("Please type yes or no.")


def add_to_review_bank(missed_questions):
    for question in missed_questions:
        if question not in review_bank:
            review_bank.append(question)

    save_review_bank()


def choose_study_mode(questions):
    if len(questions) == 0:
        print("\nNo questions are available yet.")
        return []

    print("\nHow would you like to study?")
    print("1. Choose number of questions")
    print("2. Study by time")
    print("3. Default quiz")

    while True:
        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            return choose_number_of_questions(questions)

        elif choice == "2":
            return choose_study_time(questions)

        elif choice == "3":
            print("\nStarting default quiz...")
            return questions

        else:
            print("Please choose 1, 2, or 3.")


def choose_number_of_questions(questions):
    while True:
        amount = input("\nHow many questions do you want? ").strip()

        if amount.isdigit():
            amount = int(amount)

            if amount <= 0:
                print("Please enter a number greater than 0.")
            elif amount > len(questions):
                print("\nThat is more questions than are currently available.")
                print("Starting with all available questions instead.")
                return questions
            else:
                return questions[:amount]

        else:
            print("Please enter a whole number.")


def choose_study_time(questions):
    while True:
        minutes = input("\nHow many minutes do you want to study? ").strip()

        if minutes.isdigit():
            minutes = int(minutes)

            if minutes <= 0:
                print("Please enter a number greater than 0.")
            else:
                question_count = minutes

                if question_count > len(questions):
                    question_count = len(questions)

                print("\nStarting a", minutes, "minute study session.")
                print("You will get", question_count, "question(s).")
                return questions[:question_count]

        else:
            print("Please enter a whole number.")


def review_missed_questions(missed_questions):
    current_missed = missed_questions

    while len(current_missed) > 0:
        print("\nYou missed", len(current_missed), "question(s).")

        review_choice = input("Would you like to review missed questions? yes/no: ").strip().lower()

        if review_choice not in ["yes", "y"]:
            print("\nNo problem. These questions were saved to your review bank.")
            add_to_review_bank(current_missed)
            break

        review_result = run_quiz(current_missed)

        if review_result["status"] == "exit":
            print("\nReview ended early.")
            add_to_review_bank(review_result["missed_questions"])
            break

        current_missed = review_result["missed_questions"]

        if len(current_missed) == 0:
            print("\nGreat work! You answered all review questions correctly.")
            break

    save_review_bank()


def start_quiz_session(questions):
    selected_questions = choose_study_mode(questions)

    if len(selected_questions) == 0:
        return

    result = run_quiz(selected_questions)

    add_to_review_bank(result["missed_questions"])

    if result["status"] != "exit":
        review_missed_questions(result["missed_questions"])


def show_lesson(topic_name, lesson_data):
    print("\n" + "=" * 40)
    print(topic_name)
    print("=" * 40)

    summary_choice = input(
        "\nWould you like to see a source-backed topic summary first? yes/no: "
    ).strip().lower()

    if summary_choice in ["yes", "y"]:
        show_source_summary(topic_name)

    if "lesson" in lesson_data:
        print("\nLesson:")
        print(lesson_data["lesson"])

    if "key_terms" in lesson_data:
        print("\nKey Terms:")
        for term in lesson_data["key_terms"]:
            print("-", term)

    if "source_notes" in lesson_data:
        print("\nSource Notes:")
        print(lesson_data["source_notes"])


def handle_learning_topic():
    print("\nAvailable learning topics:")
    topic_names = list(lessons.keys())

    for index, topic_name in enumerate(topic_names, start=1):
        print(str(index) + ".", topic_name)

    while True:
        choice = input("\nChoose a topic number or type 'back': ").strip().lower()

        if choice == "back":
            return

        if choice.isdigit():
            choice = int(choice)

            if 1 <= choice <= len(topic_names):
                selected_topic = topic_names[choice - 1]
                lesson_data = lessons[selected_topic]

                show_lesson(selected_topic, lesson_data)

                if "questions" in lesson_data:
                    start_quiz_session(lesson_data["questions"])
                else:
                    print("\nThis topic does not have quiz questions yet.")

                return

            else:
                print("Please choose a valid topic number.")
        else:
            print("Please enter a number or type 'back'.")


def handle_pasted_text():
    print("\nPaste your study text below.")
    print("When you are finished, press Enter.")
    print("You can type 'back' to return to the menu.")

    pasted_text = input("\nPaste text here: ").strip()

    if pasted_text.lower() == "back":
        return

    if pasted_text == "":
        print("\nNo text was entered.")
        return

    questions = create_pasted_text_questions(pasted_text)

    if len(questions) == 0:
        print("\nI could not create quiz questions from that text yet.")
        print("Try pasting text about Python lists, network outages, or AI fact-checking.")
        return

    print("\nQuiz questions were created from your pasted text.")
    start_quiz_session(questions)


def handle_review_bank():
    if len(review_bank) == 0:
        print("\nYour review bank is empty.")
        print("Miss questions in a quiz first, then they will show up here.")
        return

    print("\nReview Bank")
    print("You have", len(review_bank), "question(s) saved.")

    selected_questions = choose_study_mode(review_bank)

    if len(selected_questions) == 0:
        return

    result = run_quiz(selected_questions)

    review_bank.clear()
    add_to_review_bank(result["missed_questions"])
    save_review_bank()

    if len(review_bank) == 0:
        print("\nGreat work! Your review bank is now clear.")
    else:
        print("\nYou still have", len(review_bank), "question(s) in your review bank.")


def ask_quiz_from_summary(summary_data):
    if "questions" not in summary_data:
        print("\nThis source-backed summary does not have quiz questions yet.")
        return

    questions = summary_data["questions"]

    if len(questions) == 0:
        print("\nThis source-backed summary does not have quiz questions yet.")
        return

    while True:
        quiz_choice = input(
            "\nWould you like to quiz yourself on this summary? yes/no: "
        ).strip().lower()

        if quiz_choice in ["yes", "y"]:
            start_quiz_session(questions)
            return

        elif quiz_choice in ["no", "n"]:
            print("\nNo problem. You can review the summary again later.")
            return

        else:
            print("Please type yes or no.")


def ask_quiz_from_internet_summary(internet_result):
    questions = create_internet_summary_questions(internet_result)

    if len(questions) == 0:
        print("\nNo quiz questions could be created from this internet summary yet.")
        return

    while True:
        quiz_choice = input(
            "\nWould you like to quiz yourself on this internet summary? yes/no: "
        ).strip().lower()

        if quiz_choice in ["yes", "y"]:
            start_quiz_session(questions)
            return

        elif quiz_choice in ["no", "n"]:
            print("\nNo problem. You can review the internet summary again later.")
            return

        else:
            print("Please type yes or no.")


def handle_source_summaries():
    print("\nAvailable source-backed summaries:")
    topic_keys = list(source_summaries.keys())

    for index, topic_key in enumerate(topic_keys, start=1):
        print(str(index) + ".", source_summaries[topic_key]["topic"])

    while True:
        choice = input("\nChoose a summary number or type 'back': ").strip().lower()

        if choice == "back":
            return

        if choice.isdigit():
            choice = int(choice)

            if 1 <= choice <= len(topic_keys):
                selected_topic_key = topic_keys[choice - 1]
                summary_data = source_summaries[selected_topic_key]

                show_source_summary(selected_topic_key)
                ask_quiz_from_summary(summary_data)

                return

            else:
                print("Please choose a valid summary number.")
        else:
            print("Please enter a number or type 'back'.")


def handle_internet_topic_search():
    print("\nInternet Topic Lookup")
    print("---------------------")
    print("This feature pulls a live summary from Wikipedia.")
    print("You can type 'back' to return to the main menu.")

    topic = input("\nEnter a topic to look up: ").strip()

    if topic.lower() == "back":
        return

    if topic == "":
        print("\nNo topic was entered.")
        return

    result = show_internet_summary(topic)

    if result["status"] == "success":
        print("\nInternet lookup complete.")
        print("QuizMyBook can now turn this summary into simple quiz questions.")
        ask_quiz_from_internet_summary(result)


def handle_book_title_search():
    print("\nBook title search is planned, but not active yet.")
    print("Future versions will use a book title to identify the learning topic.")
    print("The app will not copy full book content.")
    print("The goal is to create source-backed lessons from reliable summary-level information.")


def handle_isbn_barcode_search():
    print("\nISBN/barcode search is planned, but not active yet.")
    print("Future versions will use ISBN or barcode lookup to identify a book or topic.")
    print("The app will not copy full book content.")
    print("The goal is to connect the book to safe, source-backed learning material.")


def main():
    global review_bank

    review_bank = load_review_bank()

    if len(review_bank) > 0:
        print("\nLoaded", len(review_bank), "saved review question(s).")

    keep_running = True

    while keep_running:
        show_menu()

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            handle_learning_topic()
            keep_running = ask_return_to_menu()

        elif choice == "2":
            handle_pasted_text()
            keep_running = ask_return_to_menu()

        elif choice == "3":
            handle_review_bank()
            keep_running = ask_return_to_menu()

        elif choice == "4":
            handle_source_summaries()
            keep_running = ask_return_to_menu()

        elif choice == "5":
            handle_internet_topic_search()
            keep_running = ask_return_to_menu()

        elif choice == "6":
            handle_book_title_search()
            keep_running = ask_return_to_menu()

        elif choice == "7":
            handle_isbn_barcode_search()
            keep_running = ask_return_to_menu()

        elif choice == "8":
            print("\nGood job today, keep learning!")
            save_review_bank()
            keep_running = False

        else:
            print("\nPlease choose 1, 2, 3, 4, 5, 6, 7, or 8.")


if __name__ == "__main__":
    main()