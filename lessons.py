lessons = {
    "Python lists": {
        "summary": (
            "A Python list stores multiple values in one variable. "
            "Lists keep items in order, and each item has an index. "
            "The first item is at index 0. Lists use square brackets, "
            "and they can store strings, numbers, booleans, or even other lists."
        ),
        "key_terms": {
            "List": "A collection that stores multiple values in one variable.",
            "Index": "The position number of an item in a list.",
            "Zero-based indexing": "Python starts counting list positions at 0.",
            "Element": "One item inside a list.",
            "Append": "To add an item to the end of a list.",
            "Slice": "A smaller section copied from a list."
        },
        "source_note": (
            "Local beginner lesson. Future versions will cite external sources."
        ),
        "questions": [
            {
                "question": "What does a Python list do?",
                "choices": [
                    "A. Stores several items in one variable",
                    "B. Deletes Python files",
                    "C. Turns numbers into pictures",
                    "D. Stops a program from running"
                ],
                "answer": "A",
                "hint": "Think of a shopping list with many items.",
                "explanation": "A Python list stores several items in one variable."
            },
            {
                "question": "What number is the first position in a Python list?",
                "choices": [
                    "A. 0",
                    "B. 10",
                    "C. 100",
                    "D. -99"
                ],
                "answer": "A",
                "hint": "Python starts counting list positions at the smallest non-negative number.",
                "explanation": "Python lists start counting at index 0."
            },
            {
                "question": "Which example shows a Python list?",
                "choices": [
                    "A. name = 'Steph'",
                    "B. age = 35",
                    "C. colors = ['red', 'blue', 'green']",
                    "D. print('hello')"
                ],
                "answer": "C",
                "hint": "A Python list uses square brackets.",
                "explanation": "A list uses square brackets and can hold several items."
            },
            {
                "question": "In this list, fruits = ['apple', 'banana', 'cherry'], what is fruits[0]?",
                "choices": [
                    "A. apple",
                    "B. banana",
                    "C. cherry",
                    "D. 0"
                ],
                "answer": "A",
                "hint": "Index 0 means the first item.",
                "explanation": "fruits[0] gives the first item, which is 'apple'."
            },
            {
                "question": "In this list, nums = [5, 10, 15], what is nums[1]?",
                "choices": [
                    "A. 5",
                    "B. 10",
                    "C. 15",
                    "D. 1"
                ],
                "answer": "B",
                "hint": "Index 1 means the second item.",
                "explanation": "nums[1] gives the second item, which is 10."
            },
            {
                "question": "Which symbol is used to create a list in Python?",
                "choices": [
                    "A. Square brackets []",
                    "B. Curly braces only {}",
                    "C. Parentheses only ()",
                    "D. Dollar signs $$"
                ],
                "answer": "A",
                "hint": "Look at this: colors = ['red', 'blue']",
                "explanation": "Python lists are created using square brackets."
            },
            {
                "question": "What does len(['cat', 'dog', 'bird']) return?",
                "choices": [
                    "A. 0",
                    "B. 1",
                    "C. 2",
                    "D. 3"
                ],
                "answer": "D",
                "hint": "Count how many items are inside the list.",
                "explanation": "The list has 3 items, so len() returns 3."
            },
            {
                "question": "What does append() do to a list?",
                "choices": [
                    "A. Adds an item to the end of the list",
                    "B. Deletes the whole list",
                    "C. Sorts the list backwards only",
                    "D. Turns the list into a string"
                ],
                "answer": "A",
                "hint": "Append means add onto the end.",
                "explanation": "append() adds a new item to the end of a list."
            },
            {
                "question": "What will this code do? colors = ['red']; colors.append('blue')",
                "choices": [
                    "A. Adds 'blue' to the list",
                    "B. Removes 'red'",
                    "C. Causes a SyntaxError",
                    "D. Prints the list automatically"
                ],
                "answer": "A",
                "hint": "append() adds one item.",
                "explanation": "colors.append('blue') adds 'blue' to the end of the list."
            },
            {
                "question": "What does negative index -1 usually mean in a Python list?",
                "choices": [
                    "A. The first item",
                    "B. The last item",
                    "C. The middle item",
                    "D. An empty list"
                ],
                "answer": "B",
                "hint": "Negative indexes count from the end.",
                "explanation": "Index -1 gives the last item in a list."
            },
            {
                "question": "In items = ['pen', 'book', 'bag'], what is items[-1]?",
                "choices": [
                    "A. pen",
                    "B. book",
                    "C. bag",
                    "D. -1"
                ],
                "answer": "C",
                "hint": "-1 means the last item.",
                "explanation": "items[-1] gives the last item, which is 'bag'."
            },
            {
                "question": "Which method removes an item by value?",
                "choices": [
                    "A. remove()",
                    "B. append()",
                    "C. len()",
                    "D. print()"
                ],
                "answer": "A",
                "hint": "The name sounds like what it does.",
                "explanation": "remove() removes a matching value from a list."
            },
            {
                "question": "What does pop() usually do when no index is given?",
                "choices": [
                    "A. Removes and returns the last item",
                    "B. Adds a new item",
                    "C. Counts the list",
                    "D. Makes the list empty without warning"
                ],
                "answer": "A",
                "hint": "pop() takes something out.",
                "explanation": "pop() removes and returns the last item if no index is provided."
            },
            {
                "question": "What does list slicing do?",
                "choices": [
                    "A. Gets part of a list",
                    "B. Deletes Python",
                    "C. Converts a list into a computer screen",
                    "D. Stops all loops"
                ],
                "answer": "A",
                "hint": "A slice is a section.",
                "explanation": "Slicing gets a smaller section from a list."
            },
            {
                "question": "For nums = [2, 4, 6, 8, 10], what does nums[1:4] return?",
                "choices": [
                    "A. [2, 4, 6]",
                    "B. [4, 6, 8]",
                    "C. [4, 6, 8, 10]",
                    "D. [6, 8, 10]"
                ],
                "answer": "B",
                "hint": "The start index is included, but the stop index is not.",
                "explanation": "nums[1:4] returns indexes 1, 2, and 3: [4, 6, 8]."
            },
            {
                "question": "Which answer best describes list indexes?",
                "choices": [
                    "A. Position numbers for items in a list",
                    "B. Random passwords",
                    "C. File names only",
                    "D. Python error messages only"
                ],
                "answer": "A",
                "hint": "Indexes tell Python where an item is.",
                "explanation": "Indexes are position numbers used to access list items."
            },
            {
                "question": "What happens if you try to access an index that does not exist?",
                "choices": [
                    "A. Python may raise an IndexError",
                    "B. Python always fixes it automatically",
                    "C. The computer shuts down",
                    "D. The list becomes a dictionary"
                ],
                "answer": "A",
                "hint": "Python complains when the position is outside the list.",
                "explanation": "Accessing a missing list position causes an IndexError."
            },
            {
                "question": "Which loop is commonly used to go through each item in a list?",
                "choices": [
                    "A. for loop",
                    "B. sleep loop",
                    "C. color loop",
                    "D. desktop loop"
                ],
                "answer": "A",
                "hint": "You have used this to repeat actions.",
                "explanation": "A for loop can go through each item in a list."
            },
            {
                "question": "What does this code do? for color in colors:",
                "choices": [
                    "A. Goes through each item in the colors list",
                    "B. Deletes the colors list",
                    "C. Turns colors into numbers",
                    "D. Skips every item"
                ],
                "answer": "A",
                "hint": "The word 'for' repeats through a collection.",
                "explanation": "for color in colors loops through each item in the colors list."
            },
            {
                "question": "Why are lists useful?",
                "choices": [
                    "A. They let you keep related items together",
                    "B. They only store one value forever",
                    "C. They prevent code from running",
                    "D. They are used only for pictures"
                ],
                "answer": "A",
                "hint": "Think of keeping several related values in one place.",
                "explanation": "Lists are useful because they store related items together in one variable."
            }
        ]
    },

    "Network outages": {
        "summary": (
            "A network outage happens when users, devices, or systems lose access "
            "to a network service. Outages can be caused by failed hardware, bad cables, "
            "power problems, routing issues, DNS issues, overloaded systems, configuration mistakes, "
            "or internet service provider problems. Network teams monitor devices, logs, alerts, "
            "and traffic patterns to detect problems quickly and restore service."
        ),
        "key_terms": {
            "Network outage": "A loss of network connection or network service.",
            "Router": "A device that moves traffic between networks.",
            "Switch": "A device that connects devices inside a local network.",
            "Latency": "Delay in network communication.",
            "Packet loss": "When data packets fail to reach their destination.",
            "Failover": "Switching to a backup path or system when the main one fails.",
            "NOC": "Network Operations Center, a team or place that monitors network health."
        },
        "source_note": (
            "Local beginner lesson. Future versions will cite external networking sources."
        ),
        "questions": [
            {
                "question": "What is a network outage?",
                "choices": [
                    "A. A loss of network connection or service",
                    "B. A type of Python list",
                    "C. A computer wallpaper",
                    "D. A saved music file"
                ],
                "answer": "A",
                "hint": "Think about users losing access.",
                "explanation": "A network outage means users, devices, or systems cannot reach a network service."
            },
            {
                "question": "Which issue could cause a network outage?",
                "choices": [
                    "A. Failed router or switch",
                    "B. A larger mousepad",
                    "C. Changing a desktop background",
                    "D. Opening a calculator app"
                ],
                "answer": "A",
                "hint": "Think about network hardware.",
                "explanation": "Routers and switches are important network devices. If they fail, users may lose connectivity."
            },
            {
                "question": "Why do NOC teams monitor networks?",
                "choices": [
                    "A. To detect and respond to network problems",
                    "B. To write grocery lists",
                    "C. To design phone wallpapers",
                    "D. To rename every file"
                ],
                "answer": "A",
                "hint": "A NOC watches network health.",
                "explanation": "NOC teams monitor networks so they can detect, troubleshoot, and respond to problems quickly."
            },
            {
                "question": "What does NOC stand for?",
                "choices": [
                    "A. Network Operations Center",
                    "B. New Office Computer",
                    "C. Number Order Code",
                    "D. Normal Output Color"
                ],
                "answer": "A",
                "hint": "It is a team or place that monitors networks.",
                "explanation": "NOC stands for Network Operations Center."
            },
            {
                "question": "What is a router used for?",
                "choices": [
                    "A. Moving traffic between networks",
                    "B. Printing documents only",
                    "C. Charging a phone",
                    "D. Changing monitor brightness"
                ],
                "answer": "A",
                "hint": "Routers help networks talk to each other.",
                "explanation": "A router moves traffic between networks, such as a local network and the internet."
            },
            {
                "question": "What is a switch used for?",
                "choices": [
                    "A. Connecting devices inside a local network",
                    "B. Baking food",
                    "C. Writing poems",
                    "D. Deleting emails automatically"
                ],
                "answer": "A",
                "hint": "Switches connect devices like computers and servers.",
                "explanation": "A switch connects devices inside a local area network."
            },
            {
                "question": "What is latency?",
                "choices": [
                    "A. Delay in network communication",
                    "B. A type of keyboard",
                    "C. A backup password",
                    "D. A deleted file"
                ],
                "answer": "A",
                "hint": "Latency means delay.",
                "explanation": "Latency is the delay between sending data and receiving a response."
            },
            {
                "question": "What is packet loss?",
                "choices": [
                    "A. When data packets fail to reach their destination",
                    "B. When a keyboard loses letters",
                    "C. When a file becomes a picture",
                    "D. When Python deletes a list"
                ],
                "answer": "A",
                "hint": "Packets are small pieces of network data.",
                "explanation": "Packet loss happens when some data packets do not arrive where they are supposed to go."
            },
            {
                "question": "Why can packet loss be a problem?",
                "choices": [
                    "A. It can cause slow, broken, or unreliable connections",
                    "B. It makes screens brighter",
                    "C. It improves every connection",
                    "D. It removes the need for monitoring"
                ],
                "answer": "A",
                "hint": "Lost data can hurt communication.",
                "explanation": "Packet loss can cause poor performance, dropped calls, failed downloads, or unreliable applications."
            },
            {
                "question": "What is failover?",
                "choices": [
                    "A. Switching to a backup path or system after a failure",
                    "B. Turning off every computer forever",
                    "C. Printing a network diagram",
                    "D. Changing a username"
                ],
                "answer": "A",
                "hint": "Failover uses a backup.",
                "explanation": "Failover means moving service to a backup system or connection when the primary one fails."
            },
            {
                "question": "Why are backup network paths useful?",
                "choices": [
                    "A. They can keep service running during a failure",
                    "B. They make outages impossible forever",
                    "C. They delete all logs",
                    "D. They replace every user"
                ],
                "answer": "A",
                "hint": "Backups help when the main path breaks.",
                "explanation": "Backup paths improve reliability by giving traffic another route if the main path fails."
            },
            {
                "question": "Which symptom may suggest a network outage?",
                "choices": [
                    "A. Users cannot access an application or website",
                    "B. The keyboard is a different color",
                    "C. A document has a typo",
                    "D. A desktop icon moved"
                ],
                "answer": "A",
                "hint": "Think about loss of access.",
                "explanation": "If many users cannot access a service, there may be a network outage or service issue."
            },
            {
                "question": "Which tool output is often useful during network troubleshooting?",
                "choices": [
                    "A. Logs and alerts",
                    "B. A recipe book",
                    "C. A drawing app only",
                    "D. A music playlist"
                ],
                "answer": "A",
                "hint": "Troubleshooting uses evidence.",
                "explanation": "Logs and alerts help network teams understand what happened and when."
            },
            {
                "question": "Why are timestamps important in network logs?",
                "choices": [
                    "A. They show when events happened",
                    "B. They change the network cable color",
                    "C. They delete old routers",
                    "D. They make passwords public"
                ],
                "answer": "A",
                "hint": "Time helps build the story.",
                "explanation": "Timestamps help teams connect events and understand the order of problems."
            },
            {
                "question": "What could repeated interface up/down messages suggest?",
                "choices": [
                    "A. A flapping or unstable connection",
                    "B. A healthy connection with no issues",
                    "C. A new wallpaper",
                    "D. A finished grocery list"
                ],
                "answer": "A",
                "hint": "Repeated changes can mean instability.",
                "explanation": "Repeated up/down events can indicate interface flapping or an unstable network link."
            },
            {
                "question": "What is a common first troubleshooting question during an outage?",
                "choices": [
                    "A. Who or what is affected?",
                    "B. What color is the mousepad?",
                    "C. Which song is playing?",
                    "D. How many icons are on the desktop?"
                ],
                "answer": "A",
                "hint": "Start by finding the scope.",
                "explanation": "Knowing who or what is affected helps narrow down the outage scope."
            },
            {
                "question": "What does outage scope mean?",
                "choices": [
                    "A. How much of the system or user base is affected",
                    "B. The size of a computer monitor",
                    "C. The name of a Python variable",
                    "D. A random password"
                ],
                "answer": "A",
                "hint": "Scope means size or reach.",
                "explanation": "Outage scope describes how widespread the problem is."
            },
            {
                "question": "Why should teams avoid guessing during an outage?",
                "choices": [
                    "A. Evidence-based troubleshooting is more reliable",
                    "B. Guessing always fixes networks",
                    "C. Logs are never useful",
                    "D. Alerts should be ignored"
                ],
                "answer": "A",
                "hint": "Use facts, logs, and tests.",
                "explanation": "Evidence-based troubleshooting helps teams avoid wasting time on wrong assumptions."
            },
            {
                "question": "Which is a good outage response habit?",
                "choices": [
                    "A. Document what happened and what was done",
                    "B. Hide the issue from everyone",
                    "C. Delete all alerts before reviewing them",
                    "D. Randomly unplug devices"
                ],
                "answer": "A",
                "hint": "Good records help later.",
                "explanation": "Documentation helps with communication, follow-up, and future prevention."
            },
            {
                "question": "Why is monitoring useful before an outage becomes severe?",
                "choices": [
                    "A. It can reveal warning signs early",
                    "B. It guarantees no device will ever fail",
                    "C. It removes the need for backups",
                    "D. It replaces all network engineers"
                ],
                "answer": "A",
                "hint": "Monitoring can catch early symptoms.",
                "explanation": "Monitoring can show warning signs like errors, packet loss, high latency, or repeated failures before users are heavily impacted."
            }
        ]
    },

    "AI fact-checking": {
        "summary": (
            "AI fact-checking means checking information against reliable sources "
            "before trusting or using it. A good system should compare claims, "
            "look for agreement across sources, identify uncertainty, and show citations. "
            "AI can be helpful, but it can also make mistakes, so important facts should be verified."
        ),
        "key_terms": {
            "Claim": "A statement that may need to be checked.",
            "Source": "Where information comes from.",
            "Citation": "A note showing where information was found.",
            "Verification": "The process of checking whether information is accurate.",
            "Reliable source": "A source that is trustworthy, relevant, and evidence-based.",
            "Hallucination": "When AI gives information that sounds true but is wrong or unsupported.",
            "Cross-checking": "Comparing information across more than one source."
        },
        "source_note": (
            "Local beginner lesson. Future versions will cite external fact-checking and AI safety sources."
        ),
        "questions": [
            {
                "question": "What is the main goal of AI fact-checking?",
                "choices": [
                    "A. To check whether information is reliable",
                    "B. To make a computer screen brighter",
                    "C. To delete every source",
                    "D. To make random guesses sound official"
                ],
                "answer": "A",
                "hint": "Fact-checking helps you avoid trusting bad information.",
                "explanation": "AI fact-checking helps confirm whether information is trustworthy."
            },
            {
                "question": "What is a claim?",
                "choices": [
                    "A. A statement that may need to be checked",
                    "B. A computer cable",
                    "C. A type of keyboard",
                    "D. A deleted folder"
                ],
                "answer": "A",
                "hint": "A claim is something someone says is true.",
                "explanation": "A claim is a statement that can be checked for accuracy."
            },
            {
                "question": "Why should a learning app compare multiple sources?",
                "choices": [
                    "A. To see whether important facts agree",
                    "B. To make the lesson disappear",
                    "C. To avoid learning anything",
                    "D. To replace the user completely"
                ],
                "answer": "A",
                "hint": "One source can be wrong, so comparison helps.",
                "explanation": "Comparing sources reduces the chance of trusting one incorrect source."
            },
            {
                "question": "What should a source-backed learning app show?",
                "choices": [
                    "A. Citations or source notes",
                    "B. Secret passwords",
                    "C. Random answers with no support",
                    "D. Private user data"
                ],
                "answer": "A",
                "hint": "The user should be able to see where information came from.",
                "explanation": "Citations help users check the sources behind the lesson."
            },
            {
                "question": "What is a citation?",
                "choices": [
                    "A. A note showing where information came from",
                    "B. A random password",
                    "C. A deleted app",
                    "D. A computer virus"
                ],
                "answer": "A",
                "hint": "Citations point back to sources.",
                "explanation": "A citation helps users find and review the source of information."
            },
            {
                "question": "What is verification?",
                "choices": [
                    "A. Checking whether information is accurate",
                    "B. Guessing without evidence",
                    "C. Removing every source",
                    "D. Making text longer for no reason"
                ],
                "answer": "A",
                "hint": "Verification means checking.",
                "explanation": "Verification is the process of checking whether information is true or accurate."
            },
            {
                "question": "What is an AI hallucination?",
                "choices": [
                    "A. When AI gives wrong or unsupported information that sounds true",
                    "B. When AI turns off a monitor",
                    "C. When AI deletes a keyboard",
                    "D. When AI prints a grocery list"
                ],
                "answer": "A",
                "hint": "It sounds confident but may be false.",
                "explanation": "An AI hallucination happens when AI gives information that sounds real but is incorrect or unsupported."
            },
            {
                "question": "Why are hallucinations dangerous in a learning app?",
                "choices": [
                    "A. They can teach users incorrect information",
                    "B. They make the app run faster",
                    "C. They always improve accuracy",
                    "D. They remove the need for sources"
                ],
                "answer": "A",
                "hint": "Bad information can become bad learning.",
                "explanation": "Hallucinations are dangerous because users may learn and trust false information."
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
                "hint": "Reliable sources give trustworthy evidence.",
                "explanation": "A reliable source is trustworthy, relevant, and supported by evidence."
            },
            {
                "question": "Why should AI avoid unsupported claims?",
                "choices": [
                    "A. Unsupported claims may be false or misleading",
                    "B. Unsupported claims are always correct",
                    "C. Unsupported claims make citations unnecessary",
                    "D. Unsupported claims replace learning"
                ],
                "answer": "A",
                "hint": "If there is no support, be careful.",
                "explanation": "Unsupported claims may mislead users because they are not backed by evidence."
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
                "hint": "Cross-checking means checking across sources.",
                "explanation": "Cross-checking compares facts across multiple sources to look for agreement or conflict."
            },
            {
                "question": "What should the app do if two sources disagree?",
                "choices": [
                    "A. Flag uncertainty instead of pretending everything is certain",
                    "B. Hide the disagreement",
                    "C. Pick a random answer",
                    "D. Delete both sources immediately"
                ],
                "answer": "A",
                "hint": "Disagreement means the app should be cautious.",
                "explanation": "When sources disagree, the app should show uncertainty and avoid overstating confidence."
            },
            {
                "question": "What is source quality?",
                "choices": [
                    "A. How trustworthy and useful a source is",
                    "B. How colorful a website looks",
                    "C. How many ads a page has",
                    "D. How long a password is"
                ],
                "answer": "A",
                "hint": "Quality means trustworthiness and usefulness.",
                "explanation": "Source quality describes whether a source is reliable, relevant, and useful for the claim being checked."
            },
            {
                "question": "Which source is usually better for a medical fact?",
                "choices": [
                    "A. A trusted medical organization or official health source",
                    "B. A random comment with no evidence",
                    "C. A meme",
                    "D. An unrelated shopping page"
                ],
                "answer": "A",
                "hint": "Important facts need strong sources.",
                "explanation": "High-stakes topics like medicine need reliable expert or official sources."
            },
            {
                "question": "Why should AI show uncertainty when it is unsure?",
                "choices": [
                    "A. It helps avoid misleading the user",
                    "B. It makes wrong answers correct",
                    "C. It hides the truth",
                    "D. It removes the need for learning"
                ],
                "answer": "A",
                "hint": "Being honest about uncertainty protects the user.",
                "explanation": "Showing uncertainty is better than pretending something is confirmed when it is not."
            },
            {
                "question": "What is a good habit before trusting an AI answer?",
                "choices": [
                    "A. Check important facts against reliable sources",
                    "B. Believe everything instantly",
                    "C. Ignore citations",
                    "D. Avoid reading the answer"
                ],
                "answer": "A",
                "hint": "Trust, but verify.",
                "explanation": "Important facts should be checked against reliable sources before being trusted."
            },
            {
                "question": "Why are citations useful for users?",
                "choices": [
                    "A. They let users review where information came from",
                    "B. They hide the source",
                    "C. They delete the lesson",
                    "D. They replace thinking"
                ],
                "answer": "A",
                "hint": "Citations make information traceable.",
                "explanation": "Citations help users check the original source and judge whether information is trustworthy."
            },
            {
                "question": "What should an AI learning app avoid doing with copyrighted books?",
                "choices": [
                    "A. Copying or reproducing the full book",
                    "B. Identifying the learning topic",
                    "C. Using light metadata safely",
                    "D. Creating original quiz questions"
                ],
                "answer": "A",
                "hint": "The app should stay copyright-safe.",
                "explanation": "A learning app should avoid copying full copyrighted books and instead use safe, summary-level information."
            },
            {
                "question": "What is the safest order for a source-backed AI quiz app?",
                "choices": [
                    "A. Sources first, summary second, quiz third",
                    "B. Quiz first, sources never",
                    "C. Guess first, verify never",
                    "D. Copy a book first, cite nothing"
                ],
                "answer": "A",
                "hint": "Build from evidence before generating questions.",
                "explanation": "A safe source-backed app should gather sources, create a supported summary, and then generate quiz questions."
            },
            {
                "question": "Why is fact-checking important for QuizMyBook's future?",
                "choices": [
                    "A. It helps the app teach accurate, source-backed information",
                    "B. It makes the app ignore sources",
                    "C. It prevents users from learning",
                    "D. It removes all explanations"
                ],
                "answer": "A",
                "hint": "The goal is trustworthy learning.",
                "explanation": "Fact-checking helps QuizMyBook become a trustworthy learning app instead of just a random quiz generator."
            }
        ]
    }
}