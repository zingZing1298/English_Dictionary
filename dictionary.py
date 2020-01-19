import json
from difflib import SequenceMatcher as sqm 
from difflib import get_close_matches as gcm 
data = json.load(open("data.json"))

def meaning(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[w.title()]
    elif word.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]

    elif len(gcm(word, data.keys())) > 0:
        yn =  input("Did you mean %s instead? Enter Y for yes and N for no. " % gcm(word, data.keys())[0]) #compares the closest match and then recommends the word to the user.
        if yn == "Y":
            return data[gcm(word, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Enter a valid word."
        else:
            return "Invalid Entry. Try again."

    else:
        return "Word doesn't exist. Enter a valid word"
word = input("Enter a word: ")

output = meaning(word)


if type(output) == list:
    for item in output:
        print(item)
else:
    print(item)