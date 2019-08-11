import json

data = json.load(open("App1_Dictionary/data.json"))

def translate(word) -> str:
    word: [str] = word.lower()
    if word in data:
        return data[word]
    else:
        return "Sorry, the word doesn't exist."

if __name__ == "__main__":
    word = input("Enter word: ")
    print(translate(word))
