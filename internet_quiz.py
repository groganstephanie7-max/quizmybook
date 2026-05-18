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
    "commonly", "important", "typically", "mainly", "substantial",
    "amount", "become", "became", "commonplace"
}


GENERIC_DISTRACTORS = [
    "It is a related idea, but it does not fully explain the main concept.",
    "It describes only one small part of the topic, not the whole idea.",
    "It sounds connected, but it reverses the main meaning.",
    "It is a common misconception about the topic.",
    "It is too broad and does not answer the question directly.",
    "It is too narrow and leaves out the most important idea.",
]


BAD_KEYWORDS = {
    "about", "after", "again", "against", "amount", "became", "become",
    "before", "commonplace", "different", "important", "including",
    "known", "mainly", "other", "substantial", "through", "typically",
    "using", "various", "within", "without"
}


STRONG_KEYWORD_SIGNALS = {
    "agriculture", "cultures", "domesticated", "farming", "grain",
    "harvest", "management", "population", "production", "seed",
    "species", "storage", "transport", "worldwide"
}


def clean_text(text):
    """
    Cleans extra spaces from text.
    """
    if not text:
        return ""

    return " ".join(str(text).split())


def generate_concept_distractors(topic):
    """
    Creates safer, more believable wrong answers for concept questions.

    These are not random nonsense answers. They are designed to be:
    - related enough to feel plausible
    - still clearly wrong when compared with the summary
    - better for learning than unrelated Git/app/file distractors
    """
    topic = clean_text(topic)

    if not topic:
        topic = "The topic"

    return [
        f"{topic} is only a small part of a much larger concept.",
        f"{topic} is often confused with a similar but different idea.",
        f"{topic} is a general idea but does not fully explain the concept.",
    ]


def generate_process_distractors(topic):
    """
    Creates believable wrong answers for process/how-it-works questions.
    """
    topic = clean_text(topic)

    if not topic:
        topic = "The topic"

    return [
        f"{topic} happens through a completely unrelated process.",
        f"{topic} works only because of one small detail, not the full process.",
        f"{topic} is often explained backward from how it actually works.",
    ]


def generate_importance_distractors(topic):
    """
    Creates believable wrong answers for why-it-matters questions.
    """
    topic = clean_text(topic)

    if not topic:
        topic = "The topic"

    return [
        f"{topic} matters only in one narrow situation.",
        f"{topic} is important for a reason that is related but incomplete.",
        f"{topic} is often treated as important for the wrong reason.",
    ]


def generate_parts_distractors(topic):
    """
    Creates believable wrong answers for parts, ingredients, or components questions.
    """
    topic = clean_text(topic)

    if not topic:
        topic = "The topic"

    return [
        f"{topic} includes only one part and nothing else.",
        f"{topic} is made from a related but incorrect set of parts.",
        f"{topic} is often simplified in a way that leaves out key details.",
    ]


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
    words = re.findall(r"\b[a-zA-Z][a-zA-Z\-]{4,}\b", summary)

    counts = {}

    for word in words:
        word = word.strip("-").lower()

        if word in STOP_WORDS:
            continue

        if word in BAD_KEYWORDS:
            continue

        if word.endswith("ed") or word.endswith("ing"):
            continue

        counts[word] = counts.get(word, 0) + 1

    sorted_words = sorted(
        counts.items(),
        key=lambda item: (
            item[0] not in STRONG_KEYWORD_SIGNALS,
            -item[1],
            item[0]
        )
    )

    keywords = []

    for word, count in sorted_words:
        if word not in keywords:
            keywords.append(word)

        if len(keywords) >= limit:
            break

    return keywords


def generate_dynamic_distractors(topic, summary):
    """
    Creates smarter wrong answers using keywords from the summary.
    This makes distractors feel more realistic and topic-related.
    """
    topic = clean_text(topic)
    summary = clean_text(summary)

    if not topic:
        topic = "The topic"

    words = extract_keywords(summary)

    distractors = []

    for word in words:
        if word.lower() not in topic.lower():
            patterns = [
                f"{topic} is closely related to {word}.",
                f"{word} plays a role in understanding {topic}.",
                f"{topic} is sometimes confused with {word}.",
                f"{word} is often mistaken as the main idea behind {topic}."
            ]

            distractors.append(random.choice(patterns))

        if len(distractors) == 3:
            break

    fallback_distractors = generate_concept_distractors(topic)

    for fallback in fallback_distractors:
        if fallback not in distractors:
            distractors.append(fallback)

        if len(distractors) == 3:
            break

    return distractors[:3]

def make_multiple_choice_question(question, correct_answer, wrong_answers, hint, explanation):
    """
    Builds a multiple-choice question and shuffles the answer choices.

    The quiz engine expects:
    - choices as A-D strings
    - answer as "A", "B", "C", or "D"
    """
    labels = ["A", "B", "C", "D"]

    safe_wrong_answers = []
    correct_answer = clean_text(correct_answer)

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

    while len(safe_wrong_answers) < 3:
        safe_wrong_answers.append("It is related to the topic but does not answer this question correctly.")

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


def create_topic_question(topic, summary):
    """
    Creates a basic topic-recognition question using real summary context.
    """
    return make_multiple_choice_question(
        question="What topic was this internet summary mainly about?",
        correct_answer=topic,
        wrong_answers=generate_dynamic_distractors(topic, summary),
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
        wrong_answers=generate_dynamic_distractors(topic, definition_sentence),
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
        wrong_answers=generate_dynamic_distractors(topic, sentence),
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
        wrong_answers=generate_dynamic_distractors(topic, sentence),
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
        wrong_answers=generate_dynamic_distractors(topic, sentence),
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

    for keyword in keywords[1:]:
        if keyword != correct_keyword and keyword not in wrong_answers:
            wrong_answers.append(keyword)

        if len(wrong_answers) == 3:
            break

    for fallback in ["related", "context", "background", "example", "category"]:
        if fallback != correct_keyword and fallback not in wrong_answers:
            wrong_answers.append(fallback)

        if len(wrong_answers) == 3:
            break

    return make_multiple_choice_question(
        question=f"Which term would be a useful study keyword for learning more about {topic}?",
        correct_answer=correct_keyword,
        wrong_answers=wrong_answers,
        hint="The best answer is a topic-related word pulled from the summary.",
        explanation="A study keyword should help you research or remember the topic."
    )


def create_source_question(source_url):
    """
    Creates a source-awareness question that uses the real source URL.
    """
    source_url = clean_text(source_url)

    if not source_url:
        source_url = "No source URL was provided."

    return make_multiple_choice_question(
        question="Where did the information for this summary come from?",
        correct_answer=source_url,
        wrong_answers=[
            "It was generated randomly without a source.",
            "It came only from a local file on your computer.",
            "It was created from the quiz review bank."
        ],
        hint="Look at the source shown after the summary.",
        explanation="Knowing the source helps you verify and trust the information."
    )


def create_safety_question():
    """
    Creates a safe-learning question.
    """
    return make_multiple_choice_question(
        question="What should you do if internet information seems unclear, serious, or important?",
        correct_answer="Check it against trusted sources.",
        wrong_answers=[
            "Use only the shortest summary available.",
            "Treat the first result as enough for every situation.",
            "Focus only on memorizing the quiz answer."
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


def create_no_summary_fallback_questions(topic, source_url="No source URL was provided."):
    """
    Creates safe fallback questions if no useful summary text is available.
    """
    questions = [
        create_topic_question(topic, topic),
        create_source_question(source_url),
        create_safety_question(),
        make_multiple_choice_question(
            question="What should the app do when a summary is too short or unclear?",
            correct_answer="Give a safe, simple quiz and remind the learner to check sources.",
            wrong_answers=[
                "Use a related idea, but clearly show that the summary was limited.",
                "Ask general source-checking questions instead of pretending to know more.",
                "Keep the quiz simple and avoid unsupported details."
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
        return create_no_summary_fallback_questions(topic, source_url)

    sentences = split_summary_into_sentences(summary)
    keywords = extract_keywords(summary)

    if not sentences:
        return create_no_summary_fallback_questions(topic, source_url)

    definition_sentence = find_definition_sentence(topic, sentences)
    ingredient_sentence = find_ingredient_or_part_sentence(sentences)
    process_sentence = find_process_sentence(sentences)
    importance_sentence = find_history_or_importance_sentence(sentences)

    questions = []

    # Start with a simple orientation question.
    add_unique_question(questions, create_topic_question(topic, summary))

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
        add_unique_question(questions, create_source_question(source_url))

    if len(questions) < 5:
        add_unique_question(questions, create_safety_question())

    # If the summary did not match enough patterns, use sentence-based concept questions.
    sentence_index = 0

    while len(questions) < 5 and sentence_index < len(sentences):
        sentence = sentences[sentence_index]
        add_unique_question(
            questions,
            make_multiple_choice_question(
                question=f"Which statement best matches an idea from the {topic} summary?",
                correct_answer=sentence,
                wrong_answers=generate_dynamic_distractors(topic, sentence),
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
