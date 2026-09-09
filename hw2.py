paragraph = """
Python is a popular programming language.
This Python course teaches the basics of Python programming.
It is useful for beginners who want to learn Python.
"""

print("Length:", len(paragraph))
print("First character:", paragraph[0])
print("Last character:", paragraph[-1])
print("Preview:", paragraph[:50])

paragraph = paragraph.replace("Python", "PYTHON")
print("After replacement:", paragraph)

paragraph = paragraph.lower()
paragraph = paragraph.strip()

words = paragraph.split()
print("Words:", words)

if "course" in paragraph:
    print("The word 'course' is found in the paragraph.")

print("The course description is {} characters long and has {} words.".format(
    len(paragraph), len(words)
))