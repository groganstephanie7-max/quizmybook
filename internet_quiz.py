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
    "without", "across", "those", "them", "there", "here", "into",
    "over", "under", "again", "against", "same", "different"
}


GENERIC_WRONG_KEYWORDS = [
    "banana",
    "spaceship",
    "toothbrush",
    "pancake",
    "sidewalk",
    "volcano",
    "backpack",
    "television",
    "snowflake",
    "umbrella",
    "shoelace",
    "cupcake"
]


def clean_text(text):
    """
    Cleans extra spaces from text.
    """
    if not text:
        return ""

    return " ".join(str(text).split())


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

        # Avoid tiny sentence fragments.
        if len(sentence) >= 45:
            clean_sentences.append(sentence)

    return clean_sentences


def extract_keywords(summary, limit=10):
    """
    Extracts useful keywords from the summary.

    This is not AI.
    It uses simple word frequency and filters out common words.
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


def shorten_text(text, max_length=190):
    """
    Keeps long answer choices readable in the command line.
    """
    text = clean_text(text)

    if len(text) <= max_length:
        return text

    return text[:max_length].rstrip() + "..."


def make_multiple_choice_question(question, correct_answer, wrong_answers, hint, explanation):
    """
    Builds a multiple-choice question and shuffles the answer choices.

    The quiz engine expects:
    - choices as A-D strings
    - answer as "A", "B", "C", or "D"
    """
    labels = ["A", "B", "C", "D"]

    answer_items = [
        {"text": correct_answer, "is_correct": True},
        {"text": wrong_answers[0], "is_correct": False},
        {"text": wrong_answers[1], "is_correct": False},
        {"text": wrong_answers[2], "is_correct": False},
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


def choose_wrong_keywords(correct_keyword, keywords):
    """
    Creates wrong keyword choices.

    It tries to use other extracted keywords first, then falls back to
    generic unrelated words.
    """
    wrong_choices = []

    for keyword in keywords:
        if keyword != correct_keyword and keyword not in wrong_choices:
            wrong_choices.append(keyword)

        if len(wrong_choices) == 3:
            return wrong_choices

    for word in GENERIC_WRONG_KEYWORDS:
        if word != correct_keyword and word not in wrong_choices:
            wrong_choices.append(word)

        if len(wrong_choices) == 3:
            return wrong_choices

    return ["unrelated word", "random item", "unknown phrase"]


def choose_sentence_wrong_answers():
    """
    Creates safe wrong answers for sentence-based questions.
    """
    return [
        "The summary only discussed the app menu and did not explain the topic.",
        "The summary said the topic cannot be studied from sources.",
        "The summary was mainly about deleting local project files."
    ]


def create_topic_question(topic):
    """
    Creates a question about the main topic.
    """
    return make_multiple_choice_question(
        question="What topic was this internet summary mainly about?",
        correct_answer=topic,
        wrong_answers=[
            "A random computer error",
            "A deleted local file",
            "An unknown menu option"
        ],
        hint="Look at the topic title shown above the summary.",
        explanation="The topic title tells you what the internet summary is focused on."
    )


def create_keyword_question(keyword, keywords):
    """
    Creates a question about a keyword from the summary.
    """
    wrong_answers = choose_wrong_keywords(keyword, keywords)

    return make_multiple_choice_question(
        question="Which keyword appeared as an important term in the internet summary?",
        correct_answer=keyword,
        wrong_answers=wrong_answers,
        hint="The correct answer is a word pulled from the summary.",
        explanation="Keywords help identify the main ideas in a summary."
    )


def create_second_keyword_question(keyword, keywords):
    """
    Creates another keyword question when enough keywords exist.
    """
    wrong_answers = choose_wrong_keywords(keyword, keywords)

    return make_multiple_choice_question(
        question="Which word is another useful study keyword from the summary?",
        correct_answer=keyword,
        wrong_answers=wrong_answers,
        hint="The correct answer came from the internet summary text.",
        explanation="Finding repeated or important keywords can help you decide what to study next."
    )


def create_sentence_question(sentence):
    """
    Creates a question using a real sentence from the summary.
    """
    sentence = shorten_text(sentence)
    wrong_answers = choose_sentence_wrong_answers()

    return make_multiple_choice_question(
        question="Which statement is supported by the internet summary?",
        correct_answer=sentence,
        wrong_answers=wrong_answers,
        hint="Choose the answer that sounds like it came from the summary.",
        explanation="This question uses an actual sentence from the internet summary."
    )


def create_main_idea_question(sentence):
    """
    Creates a beginner-friendly main idea question from the summary.
    """
    sentence = shorten_text(sentence)

    return make_multiple_choice_question(
        question="Which answer best matches one idea from the internet summary?",
        correct_answer=sentence,
        wrong_answers=[
            "The topic has no information available.",
            "The topic is only a saved review question.",
            "The topic is only a Git command."
        ],
        hint="The correct choice is based on the summary text.",
        explanation="Main idea questions help connect reading with recall."
    )


def create_source_question(source_url):
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


def create_source_location_question(source_url):
    """
    Creates a question about the displayed source URL.
    """
    readable_url = source_url

    if not readable_url:
        readable_url = "No source URL was provided."

    return make_multiple_choice_question(
        question="Which answer best describes the source shown for this internet summary?",
        correct_answer=readable_url,
        wrong_answers=[
            "A local review bank file",
            "A deleted Python cache folder",
            "A random app menu option"
        ],
        hint="Look at the URL shown after the summary.",
        explanation="The source URL points to where the summary information came from."
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
            "Delete the quiz engine.",
        ],
        hint="Important information should be verified.",
        explanation="Internet summaries are useful for learning, but important facts should be checked with trusted sources."
    )


def create_no_summary_fallback_questions(topic, source_url):
    """
    Creates safe fallback questions if no useful summary text is available.
    """
    questions = [
        create_topic_question(topic),
        create_source_question(source_url),
        create_source_location_question(source_url),
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
    Creates beginner-friendly quiz questions from an internet lookup result.

    Expected internet_result example:
    {
        "topic": "Python",
        "summary": "Python is a programming language...",
        "url": "https://en.wikipedia.org/wiki/Python..."
    }

    This is not full AI question generation.
    It is simple, predictable, source-aware quiz generation.
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

    sentences = split_summary_into_sentences(summary)
    keywords = extract_keywords(summary)

    if not summary:
        return create_no_summary_fallback_questions(topic, source_url)

    questions = []

    # 1. Always include the topic question.
    questions.append(create_topic_question(topic))

    # 2. Add a keyword question if possible.
    if len(keywords) >= 1:
        questions.append(create_keyword_question(keywords[0], keywords))

    # 3. Add a second keyword question if possible.
    if len(keywords) >= 2:
        questions.append(create_second_keyword_question(keywords[1], keywords))

    # 4. Add a sentence-based question if possible.
    if len(sentences) >= 1:
        questions.append(create_sentence_question(sentences[0]))

    # 5. Add a second sentence/main idea question if possible.
    if len(sentences) >= 2:
        questions.append(create_main_idea_question(sentences[1]))

    # 6. Always include source awareness.
    questions.append(create_source_question(source_url))

    # 7. Include source URL recognition if there is room.
    questions.append(create_source_location_question(source_url))

    # 8. Always include safe-learning reminder.
    questions.append(create_safety_question())

    # Keep quiz short and beginner-friendly.
    return questions[:5]


# Backward-friendly function names.
# These help main.py work even if it was using a different function name before.

def create_questions_from_internet_summary(internet_result):
    return create_internet_quiz_questions(internet_result)


def create_internet_summary_quiz(internet_result):
    return create_internet_quiz_questions(internet_result)


def build_internet_quiz(internet_result):
    return create_internet_quiz_questions(internet_result)
def create_internet_summary_questions(internet_result):
    return create_internet_quiz_questions(internet_result)
