import json
import textwrap
import urllib.parse
import urllib.request
import urllib.error


WIKIPEDIA_API_URL = "https://en.wikipedia.org/api/rest_v1/page/summary/"


def print_wrapped_text(text, width=88):
    """
    Prints long text in readable wrapped lines for Command Prompt.
    """
    if not text:
        print("No text available.")
        return

    paragraphs = str(text).split("\n")

    for paragraph in paragraphs:
        paragraph = paragraph.strip()

        if not paragraph:
            print()
        else:
            print(textwrap.fill(paragraph, width=width))


def clean_topic(topic):
    """
    Cleans the user's topic input so it can be safely used in a Wikipedia URL.
    """
    return topic.strip()


def build_wikipedia_url(topic):
    """
    Converts a topic into a Wikipedia REST API summary URL.
    Example:
    machine learning -> https://en.wikipedia.org/api/rest_v1/page/summary/machine%20learning
    """
    cleaned_topic = clean_topic(topic)
    encoded_topic = urllib.parse.quote(cleaned_topic)
    return WIKIPEDIA_API_URL + encoded_topic


def lookup_wikipedia_summary(topic):
    """
    Looks up a topic using Wikipedia's summary API.

    Returns a dictionary with:
    - status
    - title
    - summary
    - source_url
    - error_message
    """

    cleaned_topic = clean_topic(topic)

    if cleaned_topic == "":
        return {
            "status": "error",
            "title": "",
            "summary": "",
            "source_url": "",
            "error_message": "No topic was entered."
        }

    url = build_wikipedia_url(cleaned_topic)

    try:
        request = urllib.request.Request(
            url,
            headers={
                "User-Agent": "QuizMyBook/1.0 beginner learning project"
            }
        )

        with urllib.request.urlopen(request, timeout=10) as response:
            data = response.read().decode("utf-8")
            result = json.loads(data)

        title = result.get("title", cleaned_topic)
        summary = result.get("extract", "")
        source_url = ""

        if "content_urls" in result:
            source_url = result["content_urls"]["desktop"]["page"]

        if summary == "":
            return {
                "status": "error",
                "title": title,
                "summary": "",
                "source_url": source_url,
                "error_message": "A summary was not found for that topic."
            }

        return {
            "status": "success",
            "title": title,
            "summary": summary,
            "source_url": source_url,
            "error_message": ""
        }

    except urllib.error.HTTPError as error:
        if error.code == 404:
            message = "No Wikipedia summary was found for that topic."
        else:
            message = "Wikipedia returned an HTTP error: " + str(error.code)

        return {
            "status": "error",
            "title": cleaned_topic,
            "summary": "",
            "source_url": "",
            "error_message": message
        }

    except urllib.error.URLError:
        return {
            "status": "error",
            "title": cleaned_topic,
            "summary": "",
            "source_url": "",
            "error_message": "Could not connect to the internet. Check your connection and try again."
        }

    except TimeoutError:
        return {
            "status": "error",
            "title": cleaned_topic,
            "summary": "",
            "source_url": "",
            "error_message": "The internet lookup timed out. Try again."
        }

    except json.JSONDecodeError:
        return {
            "status": "error",
            "title": cleaned_topic,
            "summary": "",
            "source_url": "",
            "error_message": "The internet response could not be read."
        }


def show_internet_summary(topic):
    """
    Displays the internet summary in a clean format.
    """

    result = lookup_wikipedia_summary(topic)

    if result["status"] != "success":
        print("\nInternet lookup failed.")
        print("Reason:", result["error_message"])
        return result

    print("\n" + "=" * 40)
    print("Internet Topic Summary")
    print("=" * 40)

    print("\nTopic:")
    print(result["title"])

    print("\nSummary:")
    print_wrapped_text(result["summary"])

    print("\nSource:")
    print(result["source_url"])

    return result


def test_lookup():
    """
    Simple test mode for this file only.
    Run this file directly with:
    py internet_lookup.py
    """

    print("\nInternet Lookup Test")
    print("--------------------")

    topic = input("Enter a topic to look up: ").strip()
    show_internet_summary(topic)


if __name__ == "__main__":
    test_lookup()