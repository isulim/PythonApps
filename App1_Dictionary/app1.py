from json import load as loadJSON
from difflib import get_close_matches

data = loadJSON(open("App1_Dictionary/data.json"))

def translate(word) -> str:
    word = word.lower()
    matches = get_close_matches(word, data.keys(), n=5, cutoff=0.7)
    
    if word in data:
        return data[word]

    elif word.title() in data: # convert 1st letter to capital
        return data[word.title()]
    
    elif word.upper() in data:
        return data[word.upper()]

    elif len(get_close_matches(word, matches)) > 0:
        confirmation = input('Did you mean word "{}" instead (Y/N)? '.format(matches[0]))
        confirmation = confirmation.lower()

        if confirmation == 'y':
            return(data[matches[0]])

        elif confirmation == 'n':
            return "Sorry, the word doesn't exist."

        else:
            return "I don't understand this input."

    else:
        return "Sorry, the word doesn't exist."

if __name__ == "__main__":
    word = input("Enter word: ")
    
    output = translate(word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
