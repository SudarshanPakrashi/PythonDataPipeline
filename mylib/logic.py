import wikipedia


def wiki(name="War Goddess", length=1):
    """This is Wikipedia fetcher"""

    my_wiki = wikipedia.summary(name, length)
    return my_wiki


def search_wiki(name):
    return wikipedia.search(name)
