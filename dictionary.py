import json
import difflib

def load_dictionary():
    return json.load(open("data.json"))

def get_user_input():
    return input("Enter a word you want defined: ")

def get_alternate_word(word):
    return difflib.get_close_matches(word, dictionary)

def pick_alternative(alternates):
    while True:   
        number = int(input("Select a number to get the definition of that word: "))
        selection = number - 1
        print(len(alternates), number, selection)
        if selection >= len(alternates):
            print("Please select a valid number")
        else:
            return alternates[selection]

def print_definitions(word):
    index = 1
    num_definitions = len(dictionary[word])
    if num_definitions > 1:
        print(f"\nWord: {word.upper()}: There are {num_definitions} definitions.")
    else:
        print(f"\nWord: {word.upper()}: There is 1 definition.")

    for definition in dictionary[word]:
        print(f"{index}: {definition}")
        index += 1
    print("\n")

dictionary = load_dictionary()

while True:
    word = get_user_input().lower()
    if word in dictionary:
        index = 1
        print_definitions(word)
    elif word == '/exit':
        print("Goodbye")
        break
    elif word not in dictionary:
        alternates = get_alternate_word(word)
        if len(alternates) > 1:
            print(f"{word} not found, did you perhaps mean one of these words?")
            index = 1
            for alternate in alternates:
                print(f"{index}. {alternate}")
                index += 1

            new_word = pick_alternative(alternates)
            print_definitions(new_word)
        else:
            print("Word not found.")
    else:
        print("Word not found.")

