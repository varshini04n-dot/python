import re

try:
    booktitle = input("Enter the book title: ")
    publication_year = input("Enter the publication year: ")

    pattern = r"^[a-zA-Z\s]+$"

    if re.match(pattern, booktitle):
        print("Valid book title")
    else:
        print("Invalid book title")

    pattern1 = r"^(19|20)\d{2}$"

    if re.match(pattern1, publication_year):
        print("Valid publication year")
    else:
        print("Invalid publication year")

except Exception as e:
    print("Invalid input:", e)

finally:
    print("Program execution completed.")