def get_sentences(study_text):
    cleaned_text = study_text.replace("!", ".").replace("?", ".")
    raw_sentences = cleaned_text.split(".")

    sentences = []

    for sentence in raw_sentences:
        clean_sentence = sentence.strip()

        if clean_sentence:
            sentences.append(clean_sentence)

    return sentences


def shorten_text(text, max_length=120):
    if len(text) <= max_length:
        return text

    return text[:max_length] + "..."


def create_generic_text_questions(study_text):
    sentences = get_sentences(study_text)

    if len(sentences) == 0:
        return [
            {
                "question": "What is the best first step when studying new material?",
                "choices": [
                    "A. Identify the main idea",
                    "B. Ignore the material",
                    "C. Guess without reading",
                    "D. Skip all details"
                ],
                "answer": "A",
                "hint": "Start with the big idea.",
                "explanation": "A good study habit is to identify the main idea first."
            }
        ]

    first_sentence = shorten_text(sentences[0])

    second_sentence = (
        shorten_text(sentences[1])
        if len(sentences) > 1
        else "Supporting details help explain the main idea"
    )

    third_sentence = (
        shorten_text(sentences[2])
        if len(sentences) > 2
        else "Key terms help reveal what the text is about"
    )

    return [
        {
            "question": "Which idea appears first in the pasted text?",
            "choices": [
                f"A. {first_sentence}",
                f"B. {second_sentence}",
                f"C. {third_sentence}",
                "D. The text does not provide a clear idea"
            ],
            "answer": "A",
            "hint": "Look at the first clear sentence of the pasted text.",
            "explanation": "The correct answer comes from the first sentence of the pasted text."
        },
        {
            "question": "Which detail also appears in the pasted text?",
            "choices": [
                f"A. {second_sentence}",
                f"B. {first_sentence}",
                f"C. {third_sentence}",
                "D. None of the listed details appear in the text"
            ],
            "answer": "A",
            "hint": "Look for another sentence after the first one.",
            "explanation": "This detail comes from the pasted text and supports the topic."
        },
        {
            "question": "What is the best way to study this pasted text?",
            "choices": [
                "A. Identify the main idea and supporting details",
                f"B. Memorize only this phrase: {first_sentence}",
                f"C. Ignore everything except this phrase: {second_sentence}",
                "D. Avoid reviewing the text"
            ],
            "answer": "A",
            "hint": "Good studying uses both the big idea and the details.",
            "explanation": "The best study approach is to understand the main idea and supporting details."
        }
    ]


def create_python_list_questions():
    return [
        {
            "question": "Based on the pasted text, what does a Python list store?",
            "choices": [
                "A. Several items in one variable",
                "B. Only one password",
                "C. A computer virus",
                "D. A deleted file"
            ],
            "answer": "A",
            "hint": "Look for what the text says lists can hold.",
            "explanation": "Python lists store multiple items in one variable."
        },
        {
            "question": "Based on the pasted text, what do Python lists use?",
            "choices": [
                "A. Square brackets",
                "B. Phone numbers",
                "C. Network cables",
                "D. Email addresses"
            ],
            "answer": "A",
            "hint": "Look for the punctuation mark mentioned in the text.",
            "explanation": "Python lists commonly use square brackets."
        },
        {
            "question": "Based on the pasted text, what is the first index in a Python list?",
            "choices": [
                "A. 0",
                "B. 1",
                "C. 10",
                "D. 100"
            ],
            "answer": "A",
            "hint": "Python starts counting from zero.",
            "explanation": "Python lists start at index 0."
        },
        {
            "question": "Which example shows a Python list?",
            "choices": [
                "A. colors = ['red', 'blue', 'green']",
                "B. name = 'Steph'",
                "C. age = 35",
                "D. print('hello')"
            ],
            "answer": "A",
            "hint": "A list uses square brackets.",
            "explanation": "colors = ['red', 'blue', 'green'] is a Python list."
        },
        {
            "question": "What is an index?",
            "choices": [
                "A. A position number for an item in a list",
                "B. A password",
                "C. A file extension",
                "D. A deleted program"
            ],
            "answer": "A",
            "hint": "Indexes help locate items.",
            "explanation": "An index is the position number of an item in a list."
        },
        {
            "question": "In nums = [5, 10, 15], what is nums[0]?",
            "choices": [
                "A. 5",
                "B. 10",
                "C. 15",
                "D. 0"
            ],
            "answer": "A",
            "hint": "Index 0 is the first item.",
            "explanation": "nums[0] gives the first item, which is 5."
        },
        {
            "question": "In nums = [5, 10, 15], what is nums[1]?",
            "choices": [
                "A. 5",
                "B. 10",
                "C. 15",
                "D. 1"
            ],
            "answer": "B",
            "hint": "Index 1 is the second item.",
            "explanation": "nums[1] gives the second item, which is 10."
        },
        {
            "question": "What does len(['cat', 'dog', 'bird']) return?",
            "choices": [
                "A. 1",
                "B. 2",
                "C. 3",
                "D. 4"
            ],
            "answer": "C",
            "hint": "Count the items in the list.",
            "explanation": "The list has 3 items, so len() returns 3."
        },
        {
            "question": "What does append() do?",
            "choices": [
                "A. Adds an item to the end of a list",
                "B. Deletes Python",
                "C. Converts a list into a password",
                "D. Stops the program"
            ],
            "answer": "A",
            "hint": "Append means add onto the end.",
            "explanation": "append() adds an item to the end of a list."
        },
        {
            "question": "What does colors.append('blue') do?",
            "choices": [
                "A. Adds 'blue' to the colors list",
                "B. Deletes the colors list",
                "C. Prints blue automatically",
                "D. Changes blue into a number"
            ],
            "answer": "A",
            "hint": "append() adds one item.",
            "explanation": "colors.append('blue') adds 'blue' to the list."
        },
        {
            "question": "What does index -1 mean in a list?",
            "choices": [
                "A. The last item",
                "B. The first item",
                "C. The second item",
                "D. Nothing in Python"
            ],
            "answer": "A",
            "hint": "Negative indexes count from the end.",
            "explanation": "Index -1 gives the last item in a list."
        },
        {
            "question": "In items = ['pen', 'book', 'bag'], what is items[-1]?",
            "choices": [
                "A. bag",
                "B. pen",
                "C. book",
                "D. -1"
            ],
            "answer": "A",
            "hint": "-1 means the last item.",
            "explanation": "items[-1] gives the last item, which is 'bag'."
        },
        {
            "question": "What does remove() do?",
            "choices": [
                "A. Removes a matching value from a list",
                "B. Adds a value to the end",
                "C. Counts the list",
                "D. Makes a list a string"
            ],
            "answer": "A",
            "hint": "The name tells you what it does.",
            "explanation": "remove() removes a matching value from a list."
        },
        {
            "question": "What does pop() usually do when no index is given?",
            "choices": [
                "A. Removes and returns the last item",
                "B. Adds a new first item",
                "C. Counts all values",
                "D. Sorts the list alphabetically"
            ],
            "answer": "A",
            "hint": "pop() takes something out.",
            "explanation": "pop() removes and returns the last item if no index is given."
        },
        {
            "question": "What does list slicing do?",
            "choices": [
                "A. Gets part of a list",
                "B. Deletes Python",
                "C. Converts a list into a screen",
                "D. Stops all loops"
            ],
            "answer": "A",
            "hint": "A slice is a section.",
            "explanation": "List slicing gets a smaller section from a list."
        },
        {
            "question": "For nums = [2, 4, 6, 8, 10], what does nums[1:4] return?",
            "choices": [
                "A. [4, 6, 8]",
                "B. [2, 4, 6]",
                "C. [4, 6, 8, 10]",
                "D. [6, 8, 10]"
            ],
            "answer": "A",
            "hint": "Start is included. Stop is not included.",
            "explanation": "nums[1:4] returns indexes 1, 2, and 3: [4, 6, 8]."
        },
        {
            "question": "What error can happen if you access a missing list index?",
            "choices": [
                "A. IndexError",
                "B. GoodJobError",
                "C. PasswordError",
                "D. ColorError"
            ],
            "answer": "A",
            "hint": "The error name is related to index.",
            "explanation": "Python raises an IndexError when a list index does not exist."
        },
        {
            "question": "Which loop is commonly used to go through each item in a list?",
            "choices": [
                "A. for loop",
                "B. sleep loop",
                "C. screen loop",
                "D. password loop"
            ],
            "answer": "A",
            "hint": "A for loop repeats over a collection.",
            "explanation": "A for loop is commonly used to go through items in a list."
        },
        {
            "question": "What does for color in colors: do?",
            "choices": [
                "A. Goes through each item in the colors list",
                "B. Deletes each color",
                "C. Turns colors into numbers",
                "D. Skips the list"
            ],
            "answer": "A",
            "hint": "The loop visits each list item.",
            "explanation": "for color in colors loops through each item in the colors list."
        },
        {
            "question": "Why are Python lists useful?",
            "choices": [
                "A. They keep related items together",
                "B. They only store one value forever",
                "C. They stop programs from running",
                "D. They are only used for pictures"
            ],
            "answer": "A",
            "hint": "Think about storing several related things.",
            "explanation": "Lists are useful because they keep related items together in one variable."
        }
    ]


def create_network_outage_questions():
    return [
        {
            "question": "Based on the pasted text, what is a network outage?",
            "choices": [
                "A. A loss of network connection or service",
                "B. A type of Python variable",
                "C. A book title",
                "D. A saved image"
            ],
            "answer": "A",
            "hint": "Think about losing access to a network.",
            "explanation": "A network outage means users or systems lose access to a network service."
        },
        {
            "question": "Which item could be related to a network outage?",
            "choices": [
                "A. Router or switch",
                "B. Notebook paper",
                "C. A kitchen spoon",
                "D. A music playlist"
            ],
            "answer": "A",
            "hint": "Think about network hardware.",
            "explanation": "Routers and switches are network devices that can affect connectivity."
        },
        {
            "question": "Why is monitoring useful for networks?",
            "choices": [
                "A. It helps detect problems",
                "B. It deletes all logs",
                "C. It hides outages",
                "D. It stops users from learning"
            ],
            "answer": "A",
            "hint": "Monitoring helps teams notice problems.",
            "explanation": "Monitoring helps detect and respond to network problems."
        },
        {
            "question": "What does NOC stand for?",
            "choices": [
                "A. Network Operations Center",
                "B. New Office Computer",
                "C. Number Output Code",
                "D. Normal Online Color"
            ],
            "answer": "A",
            "hint": "A NOC watches network health.",
            "explanation": "NOC stands for Network Operations Center."
        },
        {
            "question": "What does a router do?",
            "choices": [
                "A. Moves traffic between networks",
                "B. Prints documents",
                "C. Stores passwords only",
                "D. Changes screen brightness"
            ],
            "answer": "A",
            "hint": "Routers help networks talk to each other.",
            "explanation": "A router moves traffic between networks."
        },
        {
            "question": "What does a switch do?",
            "choices": [
                "A. Connects devices inside a local network",
                "B. Makes food",
                "C. Deletes folders",
                "D. Writes poetry"
            ],
            "answer": "A",
            "hint": "Switches connect local devices.",
            "explanation": "A switch connects devices inside a local network."
        },
        {
            "question": "What is latency?",
            "choices": [
                "A. Delay in network communication",
                "B. A type of keyboard",
                "C. A hidden file",
                "D. A deleted router"
            ],
            "answer": "A",
            "hint": "Latency means delay.",
            "explanation": "Latency is delay in network communication."
        },
        {
            "question": "What is packet loss?",
            "choices": [
                "A. When data packets fail to reach their destination",
                "B. When a keyboard loses letters",
                "C. When a list loses an index",
                "D. When a screen loses color"
            ],
            "answer": "A",
            "hint": "Packets are small pieces of network data.",
            "explanation": "Packet loss happens when data packets do not arrive successfully."
        },
        {
            "question": "Why can packet loss be harmful?",
            "choices": [
                "A. It can make connections unreliable",
                "B. It always improves the network",
                "C. It deletes every computer",
                "D. It removes the need for routers"
            ],
            "answer": "A",
            "hint": "Lost data can hurt communication.",
            "explanation": "Packet loss can cause slow, broken, or unreliable network connections."
        },
        {
            "question": "What is failover?",
            "choices": [
                "A. Switching to a backup path or system after a failure",
                "B. Turning off all computers forever",
                "C. Renaming a file",
                "D. Opening a calculator"
            ],
            "answer": "A",
            "hint": "Failover uses a backup.",
            "explanation": "Failover moves service to a backup path or system when the main one fails."
        },
        {
            "question": "Why are backup paths useful?",
            "choices": [
                "A. They help keep service running during failures",
                "B. They make outages impossible forever",
                "C. They delete all logs",
                "D. They replace every user"
            ],
            "answer": "A",
            "hint": "Backups help when the main path breaks.",
            "explanation": "Backup paths can keep traffic flowing during failures."
        },
        {
            "question": "Which symptom may suggest a network outage?",
            "choices": [
                "A. Users cannot access a service",
                "B. A desktop icon moved",
                "C. A typo appears in a note",
                "D. The mousepad is larger"
            ],
            "answer": "A",
            "hint": "Think about loss of access.",
            "explanation": "Users being unable to access a service can suggest a network outage."
        },
        {
            "question": "What kind of evidence helps during troubleshooting?",
            "choices": [
                "A. Logs and alerts",
                "B. Music playlists",
                "C. Random guesses",
                "D. Desktop wallpaper"
            ],
            "answer": "A",
            "hint": "Troubleshooting uses evidence.",
            "explanation": "Logs and alerts help show what happened."
        },
        {
            "question": "Why are timestamps useful in logs?",
            "choices": [
                "A. They show when events happened",
                "B. They change cable colors",
                "C. They erase errors",
                "D. They hide outages"
            ],
            "answer": "A",
            "hint": "Time helps build the timeline.",
            "explanation": "Timestamps help teams understand the order of network events."
        },
        {
            "question": "What could repeated interface up/down messages suggest?",
            "choices": [
                "A. A flapping or unstable connection",
                "B. A perfect connection",
                "C. A music file",
                "D. A new keyboard"
            ],
            "answer": "A",
            "hint": "Repeated state changes can mean instability.",
            "explanation": "Repeated up/down messages may suggest a flapping network interface."
        },
        {
            "question": "What is outage scope?",
            "choices": [
                "A. How much of the system or user base is affected",
                "B. The color of the router",
                "C. A Python variable",
                "D. A password length"
            ],
            "answer": "A",
            "hint": "Scope means reach or size.",
            "explanation": "Outage scope describes how widespread the problem is."
        },
        {
            "question": "What is a good first troubleshooting question?",
            "choices": [
                "A. Who or what is affected?",
                "B. What song is playing?",
                "C. What color is the mousepad?",
                "D. How many icons are on the desktop?"
            ],
            "answer": "A",
            "hint": "Start by finding the impact.",
            "explanation": "Knowing who or what is affected helps narrow down the problem."
        },
        {
            "question": "Why should teams avoid guessing during an outage?",
            "choices": [
                "A. Evidence-based troubleshooting is more reliable",
                "B. Guessing always fixes networks",
                "C. Logs are useless",
                "D. Alerts should be ignored"
            ],
            "answer": "A",
            "hint": "Use facts and tests.",
            "explanation": "Evidence-based troubleshooting helps avoid wasted time and wrong assumptions."
        },
        {
            "question": "Which is a good outage response habit?",
            "choices": [
                "A. Document what happened and what was done",
                "B. Hide the issue",
                "C. Delete all alerts first",
                "D. Randomly unplug devices"
            ],
            "answer": "A",
            "hint": "Good records help later.",
            "explanation": "Documentation helps with communication and future prevention."
        },
        {
            "question": "Why is monitoring useful before an outage becomes severe?",
            "choices": [
                "A. It can reveal warning signs early",
                "B. It guarantees nothing will ever fail",
                "C. It removes the need for backups",
                "D. It replaces every engineer"
            ],
            "answer": "A",
            "hint": "Monitoring catches early symptoms.",
            "explanation": "Monitoring can reveal warning signs like errors, packet loss, or high latency."
        }
    ]


def create_ai_fact_checking_questions():
    return [
        {
            "question": "Based on the pasted text, why are sources important?",
            "choices": [
                "A. They help support the information",
                "B. They make information disappear",
                "C. They replace studying",
                "D. They hide the answer"
            ],
            "answer": "A",
            "hint": "Sources show where information came from.",
            "explanation": "Sources help support claims and make information easier to verify."
        },
        {
            "question": "Why should facts be checked?",
            "choices": [
                "A. To make sure information is reliable",
                "B. To make guesses look official",
                "C. To remove all citations",
                "D. To avoid learning"
            ],
            "answer": "A",
            "hint": "Fact-checking helps prevent trusting bad information.",
            "explanation": "Checking facts helps confirm whether information is trustworthy."
        },
        {
            "question": "What should a source-backed app show?",
            "choices": [
                "A. Citations or source notes",
                "B. Secret passwords",
                "C. Random unsupported answers",
                "D. Private data"
            ],
            "answer": "A",
            "hint": "Users should see where information came from.",
            "explanation": "Citations or source notes help users verify information."
        },
        {
            "question": "What is a claim?",
            "choices": [
                "A. A statement that may need to be checked",
                "B. A cable",
                "C. A keyboard shortcut",
                "D. A folder name"
            ],
            "answer": "A",
            "hint": "A claim says something is true.",
            "explanation": "A claim is a statement that can be checked for accuracy."
        },
        {
            "question": "What is verification?",
            "choices": [
                "A. Checking whether information is accurate",
                "B. Guessing without evidence",
                "C. Removing sources",
                "D. Making text longer"
            ],
            "answer": "A",
            "hint": "Verification means checking.",
            "explanation": "Verification is the process of checking accuracy."
        },
        {
            "question": "What is an AI hallucination?",
            "choices": [
                "A. Wrong or unsupported information that sounds true",
                "B. A screen turning off",
                "C. A deleted keyboard",
                "D. A grocery list"
            ],
            "answer": "A",
            "hint": "It may sound confident but be wrong.",
            "explanation": "An AI hallucination is unsupported or wrong information that sounds believable."
        },
        {
            "question": "Why are AI hallucinations risky?",
            "choices": [
                "A. They can teach users incorrect information",
                "B. They always improve learning",
                "C. They remove the need for sources",
                "D. They make facts unnecessary"
            ],
            "answer": "A",
            "hint": "Bad information can become bad learning.",
            "explanation": "Hallucinations can mislead users and teach false information."
        },
        {
            "question": "What is a reliable source?",
            "choices": [
                "A. A trustworthy and evidence-based source",
                "B. A random unsupported comment",
                "C. A hidden password",
                "D. A broken file"
            ],
            "answer": "A",
            "hint": "Reliable means trustworthy.",
            "explanation": "Reliable sources are trustworthy, relevant, and supported by evidence."
        },
        {
            "question": "Why should unsupported claims be avoided?",
            "choices": [
                "A. They may be false or misleading",
                "B. They are always correct",
                "C. They replace citations",
                "D. They improve trust"
            ],
            "answer": "A",
            "hint": "Unsupported means not backed up.",
            "explanation": "Unsupported claims can mislead users because they are not backed by evidence."
        },
        {
            "question": "What does cross-checking mean?",
            "choices": [
                "A. Comparing information across more than one source",
                "B. Deleting all sources",
                "C. Guessing the answer",
                "D. Closing the app"
            ],
            "answer": "A",
            "hint": "Cross-checking uses more than one source.",
            "explanation": "Cross-checking compares information across sources."
        },
        {
            "question": "What should happen if sources disagree?",
            "choices": [
                "A. The app should flag uncertainty",
                "B. The app should hide the disagreement",
                "C. The app should pick randomly",
                "D. The app should delete everything"
            ],
            "answer": "A",
            "hint": "Disagreement means caution.",
            "explanation": "If sources disagree, the app should show uncertainty instead of pretending certainty."
        },
        {
            "question": "What is source quality?",
            "choices": [
                "A. How trustworthy and useful a source is",
                "B. How colorful a website is",
                "C. How many ads it has",
                "D. How long the title is"
            ],
            "answer": "A",
            "hint": "Quality means usefulness and trust.",
            "explanation": "Source quality describes whether a source is reliable and relevant."
        },
        {
            "question": "Which source is better for high-stakes information?",
            "choices": [
                "A. A trusted expert or official source",
                "B. A random unsupported comment",
                "C. A meme",
                "D. A shopping page"
            ],
            "answer": "A",
            "hint": "High-stakes facts need strong sources.",
            "explanation": "High-stakes information should come from trusted expert or official sources."
        },
        {
            "question": "Why should AI show uncertainty when unsure?",
            "choices": [
                "A. It helps avoid misleading the user",
                "B. It makes wrong answers correct",
                "C. It hides the truth",
                "D. It removes the need for sources"
            ],
            "answer": "A",
            "hint": "Honesty protects the user.",
            "explanation": "Showing uncertainty is safer than pretending something is confirmed."
        },
        {
            "question": "What is a good habit before trusting an AI answer?",
            "choices": [
                "A. Check important facts against reliable sources",
                "B. Believe everything instantly",
                "C. Ignore citations",
                "D. Avoid reading"
            ],
            "answer": "A",
            "hint": "Trust, but verify.",
            "explanation": "Important facts should be checked against reliable sources."
        },
        {
            "question": "Why are citations useful?",
            "choices": [
                "A. They let users review where information came from",
                "B. They hide the source",
                "C. They delete the lesson",
                "D. They replace thinking"
            ],
            "answer": "A",
            "hint": "Citations make information traceable.",
            "explanation": "Citations help users review the original source."
        },
        {
            "question": "What should an AI learning app avoid doing with copyrighted books?",
            "choices": [
                "A. Copying or reproducing the full book",
                "B. Identifying the topic",
                "C. Using light metadata safely",
                "D. Creating original questions"
            ],
            "answer": "A",
            "hint": "Stay copyright-safe.",
            "explanation": "A learning app should not copy full copyrighted books."
        },
        {
            "question": "What is the safest order for a source-backed quiz app?",
            "choices": [
                "A. Sources first, summary second, quiz third",
                "B. Quiz first, sources never",
                "C. Guess first, verify never",
                "D. Copy a book first, cite nothing"
            ],
            "answer": "A",
            "hint": "Start from evidence.",
            "explanation": "A safe app should gather sources, create a supported summary, then generate quiz questions."
        },
        {
            "question": "Why is fact-checking important for QuizMyBook?",
            "choices": [
                "A. It helps the app teach accurate, source-backed information",
                "B. It makes the app ignore sources",
                "C. It prevents users from learning",
                "D. It removes explanations"
            ],
            "answer": "A",
            "hint": "The goal is trustworthy learning.",
            "explanation": "Fact-checking helps QuizMyBook become a trustworthy learning app."
        },
        {
            "question": "What should users be able to do with source-backed information?",
            "choices": [
                "A. Review where the information came from",
                "B. Never see the source",
                "C. Only guess",
                "D. Delete the citation"
            ],
            "answer": "A",
            "hint": "Source-backed means traceable.",
            "explanation": "Users should be able to review sources behind important information."
        }
    ]


def create_pasted_text_questions(study_text):
    text = study_text.lower()

    if "list" in text or "index" in text or "square bracket" in text:
        return create_python_list_questions()

    elif "network" in text or "outage" in text or "router" in text or "switch" in text:
        return create_network_outage_questions()

    elif "source" in text or "fact" in text or "citation" in text or "verify" in text or "hallucination" in text:
        return create_ai_fact_checking_questions()

    else:
        return create_generic_text_questions(study_text)