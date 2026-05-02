import re
import random


STOP_WORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from",
    "has", "have", "he", "her", "his", "in", "is", "it", "its", "of",
    "on", "or", "that", "the", "their", "this", "to", "was", "were",
    "which", "with", "also", "can", "may", "more", "most", "other",
    "some", "such", "than", "then", "these", "they", "used", "using",
    "into", "over", "under", "between", "about", "after", "before",
    "during", "through", "while", "where", "when", "who", "what",
    "why", "how", "been", "being", "both", "each", "many", "much",
    "only", "very", "often", "usually", "generally", "sometimes",
    "including", "include", "includes", "known", "called", "make",
    "made", "does", "did", "had", "will", "would", "could", "should",
    "because", "however", "therefore", "although", "around", "within",
    "without", "across", "those", "them", "there", "here", "again",
    "against", "same", "different", "several", "various", "common",
    "commonly", "important", "typically", "mainly"
}


GENERIC_DISTRACTORS = [
    "It is only a local app setting.",
    "It is mainly a Git command.",
    "It is only a deleted cache file.",
    "It is only an unknown menu option.",
    "It is not connected to the topic summary.",
    "It is only a saved review-bank file."
]


def clean_text(text):
    """
    Cleans extra spaces from text.
    """
    if not text:
        return ""

    return " ".join(str(text).split())


def get_result_value(internet_result, possible_keys, default_value=""):
    """
    Safely gets a value from the internet lookup result.

    This keeps internet_quiz.py flexible if internet_lookup.py uses
    slightly different key names.
    """
    if not isinstance(internet_result, dict):
        return default_value

    for key in possible_keys:
        if key in internet_result and internet_result[key]:
            return internet_result[key]

    return default_value


def split_summary_into_sentences(summary):
    """
    Splits a summary into readable sentence chunks.
    """
    summary = clean_text(summary)

    if not summary:
        return []

    sentences = re.split(r"(?<=[.!?])\s+", summary)

    clean_sentences = []

    for sentence in sentences:
        sentence = clean_text(sentence)

        if len(sentence) >= 35:
            clean_sentences.append(sentence)

    return clean_sentences


def shorten_text(text, max_length=175):
    """
    Keeps long choices readable in the command line.
    """
    text = clean_text(text)

    if len(text) <= max_length:
        return text

    return text[:max_length].rstrip() + "..."


def extract_keywords(summary, limit=10):
    """
    Extracts study keywords from the summary.

    This is not AI. It uses simple frequency and common-word filtering.
    """
    summary = clean_text(summary).lower()
    words = re.findall(r"\b[a-zA-Z][a-zA-Z\-]{3,}\b", summary)

    counts = {}

    for word in words:
        word = word.strip("-").lower()

        if word in STOP_WORDS:
            continue

        counts[word] = counts.get(word, 0) + 1

    sorted_words = sorted(
        counts.items(),
        key=lambda item: item[1],
        reverse=True
    )

    keywords = []

    for word, count in sorted_words:
        if word not in keywords:
            keywords.append(word)

        if len(keywords) >= limit:
            break

    return keywords


def make_multiple_choice_question(question, correct_answer, wrong_answers, hint, explanation):
    """
    Builds a multiple-choice question and shuffles the answer choices.

    The quiz engine expects:
    - choices as A-D strings
    - answer as "A", "B", "C", or "D"
    """
    labels = ["A", "B", "C", "D"]

    safe_wrong_answers = []

    for wrong_answer in wrong_answers:
        wrong_answer = clean_text(wrong_answer)

        if wrong_answer and wrong_answer != correct_answer and wrong_answer not in safe_wrong_answers:
            safe_wrong_answers.append(wrong_answer)

        if len(safe_wrong_answers) == 3:
            break

    for fallback in GENERIC_DISTRACTORS:
        if fallback != correct_answer and fallback not in safe_wrong_answers:
            safe_wrong_answers.append(fallback)

        if len(safe_wrong_answers) == 3:
            break

    answer_items = [
        {"text": shorten_text(correct_answer), "is_correct": True},
        {"text": shorten_text(safe_wrong_answers[0]), "is_correct": False},
        {"text": shorten_text(safe_wrong_answers[1]), "is_correct": False},
        {"text": shorten_text(safe_wrong_answers[2]), "is_correct": False},
    ]

    random.shuffle(answer_items)

    choices = []
    correct_label = "A"

    for index, item in enumerate(answer_items):
        label = labels[index]
        choices.append(label + ". " + item["text"])

        if item["is_correct"]:
            correct_label = label

    return {
        "question": question,
        "choices": choices,
        "answer": correct_label,
        "hint": hint,
        "explanation": explanation
    }


def find_definition_sentence(topic, sentences):
    """
    Finds a sentence that looks like it explains what the topic is.
    """
    topic_lower = topic.lower()

    definition_patterns = [
        " is ",
        " are ",
        " refers to ",
        " means ",
        " consists of ",
        " is a ",
        " is an ",
        " is the ",
        " are a ",
        " are the "
    ]

    for sentence in sentences:
        sentence_lower = sentence.lower()

        if topic_lower in sentence_lower:
            for pattern in definition_patterns:
                if pattern in sentence_lower:
                    return sentence

    for sentence in sentences:
        sentence_lower = sentence.lower()

        for pattern in definition_patterns:
            if pattern in sentence_lower:
                return sentence

    if sentences:
        return sentences[0]

    return ""


def find_history_or_importance_sentence(sentences):
    """
    Finds a sentence about history, use, importance, culture, or role.
    """
    signals = [
        "history",
        "historical",
        "important",
        "culture",
        "cultures",
        "used",
        "use",
        "role",
        "significance",
        "traditional",
        "throughout",
        "ancient",
        "modern",
        "known",
        "noted",
        "developed",
        "became"
    ]

    for sentence in sentences:
        sentence_lower = sentence.lower()

        for signal in signals:
            if signal in sentence_lower:
                return sentence

    if len(sentences) >= 2:
        return sentences[1]

    if sentences:
        return sentences[0]

    return ""


def find_ingredient_or_part_sentence(sentences):
    """
    Finds a sentence about ingredients, parts, components, or what something is made of.
    """
    signals = [
        "made from",
        "made of",
        "consists of",
        "contains",
        "include",
        "includes",
        "including",
        "composed of",
        "made by",
        "produced by",
        "created by",
        "formed by"
    ]

    for sentence in sentences:
        sentence_lower = sentence.lower()

        for signal in signals:
            if signal in sentence_lower:
                return sentence

    return ""


def find_process_sentence(sentences):
    """
    Finds a sentence that describes a process or how something happens.
    """
    signals = [
        "made by",
        "produced by",
        "created by",
        "formed by",
        "caused by",
        "through",
        "process",
        "baking",
        "cooking",
        "fermentation",
        "developed",
        "using",
        "requires"
    ]

    for sentence in sentences:
        sentence_lower = sentence.lower()

        for signal in signals:
            if signal in sentence_lower:
                return sentence

    return ""


def remove_topic_from_sentence(topic, sentence):
    """
    Turns a sentence into a simple fill-in-the-topic style answer when possible.
    """
    sentence = clean_text(sentence)
    topic = clean_text(topic)

    if not topic or not sentence:
        return sentence

    pattern = re.compile(re.escape(topic), re.IGNORECASE)
    return pattern.sub("the topic", sentence, count=1)


def create_topic_question(topic):
    """
    Creates a basic topic-recognition question.
    """
    return make_multiple_choice_question(
        question="What topic was this internet summary mainly about?",
        correct_answer=topic,
        wrong_answers=[
            "A deleted local file",
            "An unknown menu option",
            "A random computer error"
        ],
        hint="Look at the topic title shown above the summary.",
        explanation="The topic title tells you what the internet summary is focused on."
    )


def create_definition_question(topic, definition_sentence):
    """
    Creates a stronger concept question based on a definition-style sentence.
    """
    correct_answer = remove_topic_from_sentence(topic, definition_sentence)

    return make_multiple_choice_question(
        question=f"Which answer best explains {topic} based on the summary?",
        correct_answer=correct_answer,
        wrong_answers=[
            f"{topic} is mainly a command used only inside Git.",
            f"{topic} is a local file created by the quiz app.",
            f"{topic} is an error message from Command Prompt."
        ],
        hint="Look for the choice that explains the topic itself.",
        explanation="This question checks the main concept, not just whether a word appeared."
    )


def create_importance_question(topic, sentence):
    """
    Creates a question about why the topic matters.
    """
    return make_multiple_choice_question(
        question=f"Which detail helps explain why {topic} matters?",
        correct_answer=sentence,
        wrong_answers=[
            f"{topic} only matters because it changes the app menu.",
            f"{topic} only matters because it deletes old Python files.",
            f"{topic} only matters because it creates a Git commit."
        ],
        hint="Choose the answer that gives real-world importance or context.",
        explanation="Good learning questions ask why the topic matters, not only what words appeared."
    )


def create_parts_or_ingredients_question(topic, sentence):
    """
    Creates a question about what something includes, contains, or is made from.
    """
    return make_multiple_choice_question(
        question=f"According to the summary, what is one useful detail about what {topic} includes or is made from?",
        correct_answer=sentence,
        wrong_answers=[
            f"{topic} is made only from computer files.",
            f"{topic} is made only from app menu choices.",
            f"{topic} is made only from GitHub commits."
        ],
        hint="Look for the answer that sounds like a real detail from the summary.",
        explanation="This question focuses on the actual concept details from the summary."
    )


def create_process_question(topic, sentence):
    """
    Creates a question about how something works or is made.
    """
    return make_multiple_choice_question(
        question=f"Which answer describes a process or how something works for {topic}?",
        correct_answer=sentence,
        wrong_answers=[
            f"{topic} works by deleting the review bank.",
            f"{topic} works by changing only the command prompt color.",
            f"{topic} works by skipping every source."
        ],
        hint="Choose the answer that explains a real process from the summary.",
        explanation="Process questions help you understand how the topic works."
    )


def create_keyword_concept_question(topic, keywords):
    """
    Creates one keyword question, but frames it as study focus instead of trivia.
    """
    if not keywords:
        return None

    correct_keyword = keywords[0]

    wrong_answers = []

    for word in ["menu", "cache", "commit", "folder", "syntax", "terminal"]:
        if word != correct_keyword:
            wrong_answers.append(word)

        if len(wrong_answers) == 3:
            break

    return make_multiple_choice_question(
        question=f"Which term would be a useful study keyword for learning more about {topic}?",
        correct_answer=correct_keyword,
        wrong_answers=wrong_answers,
        hint="The best answer is a topic-related word pulled from the summary.",
        explanation="A study keyword should help you research or remember the topic."
    )


def create_source_question():
    """
    Creates a source-awareness question.
    """
    return make_multiple_choice_question(
        question="Why does QuizMyBook show a source URL after an internet lookup?",
        correct_answer="So the learner can see where the summary came from.",
        wrong_answers=[
            "So the app can hide the source.",
            "So the quiz can skip the topic.",
            "So the review bank can be deleted."
        ],
        hint="A source URL helps with transparency.",
        explanation="Showing the source URL helps the learner know where the information came from."
    )


def create_safety_question():
    """
    Creates a safe-learning question.
    """
    return make_multiple_choice_question(
        question="What should you do if internet information seems unclear, serious, or important?",
        correct_answer="Check it against trusted sources.",
        wrong_answers=[
            "Assume it is always perfect.",
            "Ignore the source completely.",
            "Delete the quiz engine."
        ],
        hint="Important information should be verified.",
        explanation="Internet summaries are useful for learning, but important facts should be checked with trusted sources."
    )


def add_unique_question(questions, new_question):
    """
    Adds a question only if it is not empty and not a duplicate prompt.
    """
    if not new_question:
        return

    new_prompt = new_question.get("question", "")

    for question in questions:
        if question.get("question", "") == new_prompt:
            return

    questions.append(new_question)


def create_no_summary_fallback_questions(topic):
    """
    Creates safe fallback questions if no useful summary text is available.
    """
    questions = [
        create_topic_question(topic),
        create_source_question(),
        create_safety_question(),
        make_multiple_choice_question(
            question="What should the app do when a summary is too short or unclear?",
            correct_answer="Give a safe, simple quiz and remind the learner to check sources.",
            wrong_answers=[
                "Pretend it fully understands the topic.",
                "Delete all saved review questions.",
                "Claim the summary is perfect."
            ],
            hint="The app should stay honest when information is limited.",
            explanation="A safe learning app should be honest about weak or missing information."
        )
    ]

    return questions[:5]


def create_internet_quiz_questions(internet_result):
    """
    Creates beginner-friendly concept questions from an internet lookup result.

    Expected internet_result example:
    {
        "topic": "Python",
        "summary": "Python is a programming language...",
        "url": "https://en.wikipedia.org/wiki/Python..."
    }

    This is not full AI question generation.
    It uses simple pattern matching to create better concept-focused questions.
    """
    topic = get_result_value(
        internet_result,
        ["topic", "title", "name"],
        "the searched topic"
    )

    summary = get_result_value(
        internet_result,
        ["summary", "extract", "description"],
        ""
    )

    source_url = get_result_value(
        internet_result,
        ["url", "source_url", "link"],
        "No source URL was provided."
    )

    topic = clean_text(topic)
    summary = clean_text(summary)
    source_url = clean_text(source_url)

    if not summary:
        return create_no_summary_fallback_questions(topic)

    sentences = split_summary_into_sentences(summary)
    keywords = extract_keywords(summary)

    if not sentences:
        return create_no_summary_fallback_questions(topic)

    definition_sentence = find_definition_sentence(topic, sentences)
    ingredient_sentence = find_ingredient_or_part_sentence(sentences)
    process_sentence = find_process_sentence(sentences)
    importance_sentence = find_history_or_importance_sentence(sentences)

    questions = []

    # Start with a simple orientation question.
    add_unique_question(questions, create_topic_question(topic))

    # Prefer real concept questions over shallow word-matching.
    if definition_sentence:
        add_unique_question(questions, create_definition_question(topic, definition_sentence))

    if ingredient_sentence:
        add_unique_question(questions, create_parts_or_ingredients_question(topic, ingredient_sentence))

    if process_sentence:
        add_unique_question(questions, create_process_question(topic, process_sentence))

    if importance_sentence:
        add_unique_question(questions, create_importance_question(topic, importance_sentence))

    # Add one study-keyword question only if we need more questions.
    if len(questions) < 4:
        add_unique_question(questions, create_keyword_concept_question(topic, keywords))

    # Add source/safety questions as useful support, not the whole quiz.
    if len(questions) < 5:
        add_unique_question(questions, create_source_question())

    if len(questions) < 5:
        add_unique_question(questions, create_safety_question())

    # If the summary did not match enough patterns, use strong sentence-based concept questions.
    sentence_index = 0

    while len(questions) < 5 and sentence_index < len(sentences):
        sentence = sentences[sentence_index]
        add_unique_question(
            questions,
            make_multiple_choice_question(
                question=f"Which statement best matches an idea from the {topic} summary?",
                correct_answer=sentence,
                wrong_answers=[
                    f"{topic} is only a local file in the project.",
                    f"{topic} is only a command prompt error.",
                    f"{topic} is only a GitHub branch name."
                ],
                hint="Choose the answer that gives real information from the summary.",
                explanation="This question checks understanding of a real idea from the summary."
            )
        )
        sentence_index += 1

    return questions[:5]


# Backward-friendly function names.
# These help main.py work even if it imports a slightly different function name.

def create_questions_from_internet_summary(internet_result):
    return create_internet_quiz_questions(internet_result)


def create_internet_summary_quiz(internet_result):
    return create_internet_quiz_questions(internet_result)


def build_internet_quiz(internet_result):
    return create_internet_quiz_questions(internet_result)


def create_internet_summary_questions(internet_result):
    return create_internet_quiz_questions(internet_result)
