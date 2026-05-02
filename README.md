# QuizMyBook

QuizMyBook is a beginner-friendly Python command-line learning and quiz app.

The goal of this project is to help a user study from a learning topic, pasted study text, internet topic lookup, book title, or ISBN/barcode. The app is being built toward a source-backed learning system that can create lessons, identify key terms, generate quizzes, show source notes, provide source links, save missed-question progress, pull live topic summaries from the internet, and eventually verify information using reliable sources.

---

## Current Features

QuizMyBook currently supports:

- Learning from built-in topic lessons
- Viewing built-in source-backed topic summaries before a lesson
- Direct menu option for viewing source-backed summaries
- 10 built-in source-backed summary topics
- Quiz questions for source-backed summary topics
- Optional quiz after viewing a source-backed summary
- Source links for source-backed summaries
- Source names, URLs, and notes for each summary topic
- Live internet topic lookup using Wikipedia summaries
- Displaying internet summary source URLs
- Pasting study text and generating a quiz
- Choosing how to study:
  - by number of questions
  - by study time in minutes
  - by default study mode
- Running quizzes with multiple-choice questions
- Answering with A, B, C, or D
- Typing `hint` during a question
- Typing `exit` during a quiz
- Score tracking
- Explanations after each question
- Missed-question review mode for targeted practice
- Review bank menu option for reviewing saved missed questions later
- Saved review bank progress across sessions using `review_bank.json`
- Safe example review bank file using `review_bank.example.json`
- GitHub cleanup using `.gitignore`
- Key terms for built-in lessons
- Source notes for built-in lessons
- Beginner lesson plans for source-backed summaries
- Book title placeholder
- ISBN/barcode placeholder

---

## Current Menu

When the app starts, the user sees:

```text
Welcome to QuizMyBook!
A source-backed learning and quiz app.
-----------------------------------
1. Enter a learning topic
2. Paste study text
3. Review missed questions
4. View source-backed summaries
5. Search the internet for a topic
6. Search by book title
7. Search by ISBN/barcode
8. Exit
```

---

## Study Modes

QuizMyBook currently lets the user choose how they want to study.

The user can choose:

```text
1. Choose number of questions
2. Study by time
3. Default quiz
```

### Choose Number of Questions

The user can enter how many quiz questions they want to answer.

Example:

```text
How many questions do you want? 5
```

The app then gives the user up to that number of questions from the selected topic, pasted study text, source-backed summary quiz, or review bank.

### Study by Time

The user can enter how many minutes they want to study.

Example:

```text
How many minutes do you want to study? 10
```

The app uses that choice to create a study session.

### Default Quiz

The user can choose the default quiz option if the user does not want to customize the number of questions or study time.

---

## Internet Topic Lookup

QuizMyBook now includes a live internet topic lookup feature.

This feature uses `internet_lookup.py` to pull a live topic summary from Wikipedia and display the source URL.

### Current Behavior

- Adds a main menu option for internet topic lookup
- Lets the user type a topic
- Pulls a live Wikipedia summary
- Displays the topic title
- Displays the summary
- Displays the source URL
- Handles empty input
- Allows the user to type `back` to return to the menu
- Keeps the feature read-only for now

### Example Flow

```text
Welcome to QuizMyBook!
A source-backed learning and quiz app.
-----------------------------------
1. Enter a learning topic
2. Paste study text
3. Review missed questions
4. View source-backed summaries
5. Search the internet for a topic
6. Search by book title
7. Search by ISBN/barcode
8. Exit

Choose an option: 5
```

The app then shows:

```text
Internet Topic Lookup
---------------------
This feature pulls a live summary from Wikipedia.
You can type 'back' to return to the main menu.

Enter a topic to look up:
```

Example topic:

```text
machine learning
```

Example output:

```text
========================================
Internet Topic Summary
========================================

Topic:
Machine learning

Summary:
Machine learning is a field of study in artificial intelligence...

Source:
https://en.wikipedia.org/wiki/Machine_learning

Internet lookup complete.
This is currently read-only.
Next version can turn this summary into quiz questions.
```

### Current Limitations

Internet topic lookup is currently read-only.

It does not yet:

- Generate quiz questions from the internet summary
- Compare multiple sources
- Fact-check across sources
- Save internet summaries
- Add internet lookup results to the review bank
- Create source-backed lesson plans from live lookup results

### Why This Matters

Internet lookup is a major step toward QuizMyBook becoming a real source-backed learning assistant.

Instead of only using built-in summaries, the app can now retrieve a live topic summary and show where the information came from.

---

## Source-Backed Topic Summary Mode

QuizMyBook includes source-backed topic summary mode.

This feature lets the user view beginner-friendly summaries from `source_summaries.py`.

Source-backed summaries can currently be opened in two ways:

1. Before a built-in lesson
2. Directly from the main menu using option 4

### Current Behavior

- Offers a source-backed topic summary before a built-in lesson
- Includes a direct main menu option for summaries
- Shows a topic summary
- Shows key terms
- Shows source notes
- Shows source links with source names, URLs, and notes
- Shows a beginner lesson plan
- Can show summaries without forcing the user into a quiz
- Can ask the user if they want to quiz themselves after viewing a summary
- Uses quiz questions stored in `source_summaries.py`
- Reuses the same quiz engine, hints, scoring, missed-question review, and review bank

### Current Built-In Summary Topics

Current source-backed summary topics include:

- Python lists
- Network outages
- AI fact-checking
- Machine learning basics
- MLOps basics
- APIs
- Git and GitHub
- Cloud computing
- Data pipelines
- Model monitoring

### Example Flow from Learning Topic

```text
Available learning topics:
1. Python lists
2. Network outages
3. AI fact-checking

Choose a topic number or type 'back': 1

Would you like to see a source-backed topic summary first? yes/no: yes
```

The app then shows the source-backed summary before continuing into the regular lesson and quiz flow.

### Example Flow from Direct Summary Menu

```text
Welcome to QuizMyBook!
A source-backed learning and quiz app.
-----------------------------------
1. Enter a learning topic
2. Paste study text
3. Review missed questions
4. View source-backed summaries
5. Search the internet for a topic
6. Search by book title
7. Search by ISBN/barcode
8. Exit

Choose an option: 4
```

The app then shows:

```text
Available source-backed summaries:
1. Python Lists
2. Network Outages
3. AI Fact-Checking
4. Machine Learning Basics
5. MLOps Basics
6. APIs
7. Git and GitHub
8. Cloud Computing
9. Data Pipelines
10. Model Monitoring
```

After the user chooses a topic, the app shows:

```text
Source-Backed Topic Summary

Topic:
MLOps Basics

Summary:
MLOps means Machine Learning Operations...

Key Terms:
- MLOps
- deployment
- pipeline
- automation
- monitoring
- model versioning
- production

Source Notes:
- MLOps is commonly described as applying DevOps-style practices to machine learning systems.
- Production ML systems often need monitoring after deployment.
- Versioning data, code, and models helps teams reproduce and debug ML results.

Source Links:
- Microsoft Azure - Machine Learning Operations
  URL: https://azure.microsoft.com/en-us/solutions/machine-learning-ops
  Note: Microsoft overview of MLOps as a practice for developing and deploying ML models.

- Google Cloud - What is MLOps?
  URL: https://cloud.google.com/discover/what-is-mlops
  Note: Google Cloud explanation of MLOps, deployment, monitoring, and the ML lifecycle.

Beginner Lesson Plan:
1. Understand what MLOps means.
2. Learn why models need more than training code.
3. Learn what a machine learning pipeline does.
4. Understand model deployment at a basic level.
5. Learn why monitoring production models matters.
```

Then the app asks:

```text
Would you like to quiz yourself on this summary? yes/no:
```

If the user chooses `yes`, the app opens study mode:

```text
How would you like to study?
1. Choose number of questions
2. Study by time
3. Default quiz
```

Then it runs the quiz questions connected to that source-backed summary.

### Example Source Summary Quiz Question

```text
What does MLOps stand for?
A. Machine Learning Operations
B. Manual Learning Options
C. Model Language Output
D. Main Logic Operations
```

### Current Limitations

The current source-backed summary mode is built from trusted built-in summaries and manually added source links. It does not yet automatically verify facts across multiple outside sources.

Future versions may connect this feature to reliable online sources, compare facts, and cite sources directly.

### Why This Matters

This feature moves QuizMyBook closer to its long-term goal: becoming a source-backed learning assistant instead of only a quiz app.

It now supports a stronger learning loop:

```text
Read summary → review key terms → see source notes → check source links → follow lesson plan → take quiz → review missed questions
```

---

## Source Links

QuizMyBook stores source links inside `source_summaries.py`.

Each source-backed summary can include a `source_links` field.

Each source link includes:

- Source name
- Source URL
- Short note explaining why the source is useful

Example structure:

```python
"source_links": [
    {
        "name": "Google Cloud - What is MLOps?",
        "url": "https://cloud.google.com/discover/what-is-mlops",
        "note": "Google Cloud explanation of MLOps, deployment, monitoring, and the ML lifecycle."
    }
]
```

### Why Source Links Matter

Source links make the project more trustworthy and portfolio-ready.

They show that QuizMyBook is being designed as a learning tool that can connect summaries, lessons, quiz questions, and supporting sources.

Current source links are manually added. Future versions may automatically search reliable sources, compare facts, and generate citations.

---

## Missed-Question Review Mode

QuizMyBook includes a missed-question review feature to help learners practice the questions they got wrong.

After finishing a quiz, the app checks whether any questions were missed. If there are missed questions, the user is offered a chance to review only those questions.

This helps turn mistakes into study practice instead of simply ending the quiz.

### Current Behavior

- Tracks missed questions during a quiz
- Shows the final score
- Offers a review round for missed questions
- Lets the user retry only the questions they missed
- Repeats review if the user misses questions during review
- Works with built-in lesson quizzes
- Works with pasted-text quizzes
- Works with source-backed summary quizzes
- Supports exiting early by typing `exit`
- Supports hints by typing `hint`

### Example Flow

```text
Quiz complete!
Your score: 2 out of 3

You missed 1 question.
Would you like to review missed questions? yes/no:
```

If the user chooses `yes`, QuizMyBook starts a review quiz using only the missed questions.

If the user misses a review question again, QuizMyBook can ask whether the user wants to review the missed question again.

### Why This Matters

Missed-question review makes QuizMyBook more useful as a learning tool because it encourages active recall, repetition, and targeted practice.

---

## Review Bank

QuizMyBook includes a review bank.

The review bank saves missed questions so the user can review them later from the main menu.

### Current Behavior

- Saves missed questions after a quiz
- Avoids adding duplicate missed questions
- Lets the user choose `Review missed questions` from the main menu
- Lets the user choose how many review questions to study
- Lets the user use default quiz mode for review questions
- Lets the user use study-by-time mode for review questions
- Removes questions that are answered correctly
- Keeps questions that are missed again
- Clears the review bank when all saved questions are answered correctly
- Works with source-backed summary quiz questions
- Saves missed-question progress to `review_bank.json`
- Loads saved missed questions when the app starts again

### Example Flow

```text
Quiz complete!
Your score: 14 out of 20

You missed 6 question(s).
Would you like to review missed questions? yes/no: no

No problem. These questions were saved to your review bank.
```

Later from the main menu:

```text
3. Review missed questions
```

The app shows:

```text
Review Bank
You have 6 question(s) saved.
```

The user can then choose how many saved questions to review.

### Why This Matters

The review bank makes QuizMyBook more useful as a study tool because missed questions are not lost if the user does not review them immediately.

---

## Saved Progress with `review_bank.json`

QuizMyBook saves review bank progress across app sessions.

The app uses a small JSON file called:

```text
review_bank.json
```

This file stores missed questions from the review bank.

### Current Behavior

- Saves missed questions to `review_bank.json`
- Loads saved missed questions when the app starts
- Shows a message if saved review questions are found
- Updates the JSON file when new missed questions are added
- Updates the JSON file when review questions are cleared
- Keeps the review bank available even after closing and reopening the app

### Example Startup Message

If saved review questions exist, the app can show:

```text
Loaded 1 saved review question(s).
```

### Example Saved Progress Flow

```text
Quiz complete!
Your score: 2 out of 3

You missed 1 question(s).
Would you like to review missed questions? yes/no: no

No problem. These questions were saved to your review bank.
```

Then the user exits the app:

```text
8. Exit
```

When the user later runs:

```bat
py main.py
```

the app loads the saved review question from `review_bank.json`.

### Why This Matters

Saved progress makes QuizMyBook feel more like a real study app.

The user can stop studying, close the app, come back later, and continue reviewing missed questions.

### Current Limitations

The saved review bank is stored locally in `review_bank.json`.

It does not yet support:

- Multiple user profiles
- Cloud sync
- Long-term study statistics
- Spaced repetition scheduling

Future versions may add saved user progress, quiz history, streaks, and spaced review.

---

## Example Review Bank File

The project includes:

```text
review_bank.example.json
```

This file shows the structure of saved review questions without uploading real local progress data.

Example:

```json
[
    {
        "question": "What does MLOps stand for?",
        "choices": [
            "A. Machine Learning Operations",
            "B. Manual Learning Options",
            "C. Model Language Output",
            "D. Main Logic Operations"
        ],
        "answer": "A",
        "hint": "MLOps combines machine learning with operations practices.",
        "explanation": "MLOps stands for Machine Learning Operations."
    }
]
```

The real local progress file is:

```text
review_bank.json
```

That file is ignored by Git using `.gitignore`.

---

## GitHub Cleanup with `.gitignore`

The project includes a `.gitignore` file to keep the repository clean.

The `.gitignore` should prevent local and generated files from being uploaded, including:

```text
__pycache__/
*.pyc
review_bank.json
.venv/
venv/
.vscode/
*.log
```

### Why This Matters

This keeps GitHub focused on the project source code instead of local cache files, personal progress files, or editor settings.

`review_bank.example.json` is safe to upload because it is only an example.

`review_bank.json` should stay local because it stores real saved review progress.

---

## Built-In Topic Lessons

QuizMyBook currently includes built-in topic lessons.

Each lesson can include:

- A beginner-friendly lesson explanation
- Key terms
- Source notes
- Multiple-choice quiz questions
- Hints
- Explanations

Current built-in topic lesson areas include:

- Python lists
- Network outages
- AI fact-checking

---

## Pasted Text Quiz Mode

QuizMyBook allows the user to paste study text and generate a quiz from it.

Current pasted-text support includes keyword-based routing for known topic areas.

Supported pasted-text quiz areas currently include:

- Python lists
- Network outages
- AI fact-checking

If the pasted text does not match a known topic yet, the app can show a safe fallback message instead of breaking.

---

## Book Title Search

Book title search is currently a safe placeholder.

This means the app does not yet search the internet or pull book information, but it tells the user that this feature is planned.

Future versions may use book title search to identify the learning topic and retrieve light book metadata.

The goal is not to copy full book content. The goal is to help identify what the user wants to learn and build a source-backed lesson from reliable summary-level information.

---

## ISBN/Barcode Search

ISBN/barcode search is currently a safe placeholder.

This means the app does not yet scan barcodes or look up ISBN data, but it tells the user that this feature is planned.

Future versions may use ISBN or barcode lookup to identify a book and connect it to a learning topic.

---

## Planned Future Features

Future versions of QuizMyBook may include:

- Quiz generation from internet lookup summaries
- Source-backed topic summaries from reliable online sources
- Reliable source comparison
- Fact-checking across multiple sources
- Automated citations for generated lessons
- Beginner-friendly lesson plans
- AI-generated quizzes from verified summaries
- Book title lookup
- ISBN lookup
- Barcode scanning support
- Website version
- User progress tracking
- Saved progress across multiple users
- Spaced repetition review
- More question types
- Difficulty levels
- Hints by difficulty
- Exportable study guides

---

## Project Structure

Current project files include:

```text
quizmybook/
│
├── main.py
├── lessons.py
├── quiz_engine.py
├── pasted_text_quiz.py
├── study_mode.py
├── source_summaries.py
├── internet_lookup.py
├── review_bank.example.json
├── review_bank.json
├── .gitignore
└── README.md
```

### File Purpose

```text
main.py
Runs the main menu, loads and saves the review bank, connects source summaries, internet lookup, pasted text, and quiz features together.

lessons.py
Stores built-in topic lessons, key terms, source notes, and quiz questions.

quiz_engine.py
Runs the quiz, handles answers, hints, exit behavior, scoring, and missed questions.

pasted_text_quiz.py
Creates quiz questions from pasted study text using keyword-based matching.

study_mode.py
Handles study choices such as number of questions, study time, or default quiz mode.

source_summaries.py
Stores built-in source-backed topic summaries, key terms, source notes, source links, beginner lesson plans, and quiz questions.

internet_lookup.py
Pulls live topic summaries from Wikipedia and displays the source URL.

review_bank.example.json
Shows the safe example structure for saved review questions.

review_bank.json
Stores local saved missed questions so the review bank can survive after the app closes. This file should stay local and be ignored by Git.

.gitignore
Prevents Python cache files, local review progress, virtual environments, logs, and local editor files from being uploaded to GitHub.

README.md
Documents the project, features, usage, and future plans.
```

---

## How to Open the Project

In Command Prompt, use:

```bat
cd C:\Users\12814\quizmybook
code .
```

---

## How to Run the App

In Command Prompt, use:

```bat
py main.py
```

---

## How to Test Internet Lookup

Run the app:

```bat
py main.py
```

Then choose:

```text
5
```

Enter a topic:

```text
machine learning
```

Expected result:

```text
Internet Topic Summary
Topic:
Machine learning

Summary:
...

Source:
https://en.wikipedia.org/wiki/Machine_learning
```

---

## Example Usage

```text
Welcome to QuizMyBook!
A source-backed learning and quiz app.
-----------------------------------
1. Enter a learning topic
2. Paste study text
3. Review missed questions
4. View source-backed summaries
5. Search the internet for a topic
6. Search by book title
7. Search by ISBN/barcode
8. Exit

Choose an option:
```

The user chooses an option, selects a study mode, answers quiz questions, searches internet topics, and receives a score or summary.

---

## Current Development Status

QuizMyBook is currently in command-line MVP development.

Completed so far:

- Main menu
- Built-in topic lessons
- 10 built-in source-backed topic summaries
- Source summary prompt before built-in lessons
- Direct source-backed summaries menu option
- Source-backed summary quiz questions
- Optional quiz after viewing a source-backed summary
- Source links added to source-backed summaries
- Source names, URLs, and notes displayed in summaries
- Internet topic lookup using Wikipedia summaries
- Internet source URL display
- Pasted text quiz mode
- Study mode choices
- Quiz engine
- Hints
- Explanations
- Score tracking
- Exit behavior
- Missed-question tracking
- Repeating missed-question review mode
- Review bank menu option
- Saved review bank progress using `review_bank.json`
- Safe review bank example file
- `.gitignore` for GitHub cleanup
- GitHub repository created and pushed
- Book title placeholder
- ISBN/barcode placeholder
- Project README documentation

---

## Next Development Steps

Recommended next steps:

1. Generate quiz questions from internet lookup summaries.
2. Save internet lookup summaries for later review.
3. Add more quiz questions for each source-backed summary topic.
4. Add automatic source lookup from reliable sources beyond Wikipedia.
5. Add source comparison and fact-checking across multiple sources.
6. Add automated citations for generated lessons.
7. Add book title and ISBN lookup as topic-identification helpers.
8. Add saved quiz history and study statistics.
9. Add spaced repetition review.
10. Add more question types and difficulty levels.
11. Build a simple website version.

---

## Project Goal

The long-term goal of QuizMyBook is to become a source-backed learning assistant.

Instead of only creating quizzes, QuizMyBook should eventually be able to:

1. Identify what the user wants to learn
2. Gather reliable summary-level information
3. Compare sources
4. Verify key facts
5. Create a beginner-friendly lesson
6. Generate a quiz from the verified lesson
7. Help the user review missed concepts
8. Save learning progress over time
9. Pull live topic information from reliable sources

---

## Notes

This project is being built step by step as a Python learning and AI engineering portfolio project.

The current version is intentionally simple, readable, and beginner-friendly.

The source-backed summary mode currently uses built-in summaries and manually added source links from `source_summaries.py`.

The internet lookup mode currently pulls live summaries from Wikipedia through `internet_lookup.py`.

The app does not yet perform multi-source fact-checking or automated citation checking.

The app currently has 10 built-in source-backed summaries, and each summary now includes source notes, source links, beginner lesson plans, and quiz questions.

The review bank saves missed questions to `review_bank.json`, so missed-question progress can survive after the app closes.

`review_bank.example.json` is included as a safe example file.

`.gitignore` keeps local progress, Python cache files, virtual environments, logs, and editor settings out of GitHub.