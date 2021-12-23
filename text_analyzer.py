# Defining all necessary variables for later
'''
author = Sebastián
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly , impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
USERS ={"bob": "123",
        "ann": "pass123",
        "mike": "password123",
        "liz": "pass123"}
separator = "-" * 48

values = {"words": 0,
          "titlecase": 0,
          "uppercase": 0,
          "lowercase": 0,
          "numeric": 0,
          "numsum": 0,
          }

word_occurrence = {}
clean_text = []

# welcoming the user and asking for login information
print("WELCOME TO TEXT ANALYZER!".center(len(separator)),
      separator,
      "Please login to continue...", sep="\n")
username = input("USERNAME: ")
password = input("PASSWORD: ")

# verifying login information
if username in USERS and str(password) == USERS[username]:
    print(separator,
        f"Login successful. Welcome {username.title()}!",
        f"There are {len(TEXTS)} texts currently available to analyze",
        separator, sep="\n")
else:
    print("Invalid Username or Password! Please try again")
    quit()

# allowing user to choose from TEXTS and verifying chosen number
chosen_text = input(f"Pick between 1 - {len(TEXTS)} " +
                    "to choose a text to analyze: ")

if chosen_text.isnumeric() and int(chosen_text) - 1 in range(len(TEXTS)):
    print(separator)
else:
    print(separator)
    print("The chosen number is invalid!")
    quit()

# Separating and splitting chosen text in TEXTS
for text in TEXTS[int(chosen_text) - 1].split():
    if text.strip(",.:;") == "":
        continue
    else:
        clean_text.append(text.strip(",.:;"))

# Checking values in clean_text and printing desired result
for word in clean_text:
    values["words"] += 1
    if word.istitle():
        values["titlecase"] += 1
    elif word.isupper():
        values["uppercase"] += 1
    elif word.isnumeric():
        values["numeric"] += 1
        values["numsum"] += int(word)
    else:
        values["lowercase"] += 1

print(f"""There are {values["words"]} words in the selected text.
There are {values["titlecase"]} titlecase words.
There are {values["uppercase"]} uppercase words.
There are {values["lowercase"]} lowercase words.
There are {values["numeric"]} numeric strings.
The sum of all the numbers {values["numsum"]}
""" + separator)

# checking word occurrence in clean_text and saving them
for word in clean_text:
    if len(word) not in word_occurrence:
        word_occurrence.setdefault(len(word), 1)
    else:
        word_occurrence[len(word)] += 1

# saving word, occurrence in word_occurrence into result for final print
result = [(word, word_occurrence[word]) for word in word_occurrence]

# printing result using a loop
print("LEN|  OCCURRENCES  |NR.",
      separator, sep="\n")
for word, count in sorted(result):
    print(f"{word:>2}|{'*'*count:<17}|{count}")
else:
    print(separator)