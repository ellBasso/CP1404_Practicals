"""Prompts the user for a page title or search phrase, then prints the summary of that wikipedia page"""
import wikipedia

# search = input("""What would you like to search for?
# >> """)

search = "Julian Assange"

wiki_page = wikipedia.page(search)


print(wiki_page.title)
print(wiki_page.summary)
print(wiki_page.url)
