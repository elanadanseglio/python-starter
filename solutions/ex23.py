def convertTextToMorseCode(inputString):
    textToMorseDict = {
        "a": "*-",
        "b": "-***",
        "c": "-*-*",
        "d": "-**",
        "e": "*",
        "f": "**-*",
        "g": "--*",
        "h": "****",
        "i": "**",
        "j": "*---",
        "k": "-*-",
        "l": "*-**",
        "m": "--",
        "n": "-*",
        "o": "---",
        "p": "*--*",
        "q": "--*-",
        "r": "*-*",
        "s": "***",
        "t": "-",
        "u": "**-",
        "v": "***-",
        "w": "*--",
        "x": "-**-",
        "y": "-*--",
        "z": "--**",
    }

    wordList = inputString.split()
    morsecode = ""
    for word in wordList:
        for i in range(len(word)):
            letter = word[i]
            morsecode += textToMorseDict[letter.lower()] + " "
        morsecode += "  "

    print(morsecode)


def convertMorseCodeToText(morseCode):
    morseToTextDict = {
        "*-": "a",
        "-***": "b",
        "-*-*": "c",
        "-**": "d",
        "*": "e",
        "**-*": "f",
        "--*": "g",
        "****": "h",
        "**": "i",
        "*---": "j",
        "-*-": "k",
        "*-**": "l",
        "--": "m",
        "-*": "n",
        "---": "o",
        "*--*": "p",
        "--*-": "q",
        "*-*": "r",
        "***": "s",
        "-": "t",
        "**-": "u",
        "***-": "v",
        "*--": "w",
        "-**-": "x",
        "-*--": "y",
        "--**": "z",
    }

    english = ""

    for word in morseCode.split("  "):
        for letterMorse in word.split():
            english += morseToTextDict[letterMorse]

        english += " "
    print(english)


def main():
    while True:
        userinput = input("Enter text or morse code: ")

        if userinput[0].isalpha():
            convertTextToMorseCode(userinput)
        else:
            convertMorseCodeToText(userinput)