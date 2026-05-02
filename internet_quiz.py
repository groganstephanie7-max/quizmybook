def create_internet_summary_questions(internet_result):
    """
    Creates simple quiz questions from an internet lookup result.

    internet_result should be a dictionary from internet_lookup.py with:
    - status
    - title
    - summary
    - source_url
    - error_message

    This first version uses safe template-based questions.
    """

    if internet_result["status"] != "success":
        return []

    title = internet_result["title"]
    summary = internet_result["summary"]
    source_url = internet_result["source_url"]

    if title == "" or summary == "":
        return []

    questions = [
        {
            "question": "What topic was this internet summary about?",
            "choices": [
                "A. " + title,
                "B. A random computer error",
                "C. A deleted file",
                "D. An unknown menu option"
            ],
            "answer": "A",
            "hint": "Look at the topic title shown in the internet summary.",
            "explanation": "The internet summary was about " + title + "."
        },
        {
            "question": "Where did this internet summary come from?",
            "choices": [
                "A. Wikipedia",
                "B. A saved review bank file",
                "C. The local command prompt history",
                "D. A Python cache folder"
            ],
            "answer": "A",
            "hint": "Look at the source URL shown under the summary.",
            "explanation": "The internet lookup pulls a live summary from Wikipedia."
        },
        {
            "question": "Why does QuizMyBook show a source URL with internet summaries?",
            "choices": [
                "A. So the user can see where the information came from",
                "B. So the app can hide the source",
                "C. So the quiz can ignore evidence",
                "D. So the topic name disappears"
            ],
            "answer": "A",
            "hint": "Source-backed learning means showing where information came from.",
            "explanation": "Showing a source URL makes the summary more transparent and trustworthy."
        },
        {
            "question": "What should you do if an internet summary seems unclear or incomplete?",
            "choices": [
                "A. Check the source and compare with other reliable sources",
                "B. Assume it is always perfect",
                "C. Delete the app",
                "D. Ignore all sources"
            ],
            "answer": "A",
            "hint": "Internet information should be checked, especially for important topics.",
            "explanation": "A source-backed system should encourage checking and comparing reliable sources."
        },
        {
            "question": "What can QuizMyBook do with this internet summary in this new feature?",
            "choices": [
                "A. Turn it into simple study questions",
                "B. Guarantee every fact is verified across all sources",
                "C. Replace all built-in lessons",
                "D. Scan a barcode automatically"
            ],
            "answer": "A",
            "hint": "This feature is the first step toward internet-based quizzes.",
            "explanation": "This version can turn a live internet summary into simple quiz questions."
        }
    ]

    return questions


def show_internet_quiz_preview(internet_result):
    """
    Optional helper for testing this file later.
    Prints generated questions without running the quiz engine.
    """

    questions = create_internet_summary_questions(internet_result)

    if len(questions) == 0:
        print("\nNo internet quiz questions could be created.")
        return

    print("\nGenerated Internet Quiz Questions:")
    print("----------------------------------")

    for index, question in enumerate(questions, start=1):
        print("\nQuestion", index)
        print(question["question"])

        for choice in question["choices"]:
            print(choice)

        print("Answer:", question["answer"])