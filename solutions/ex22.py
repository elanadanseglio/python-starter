
def convertTextToMorseCode(inputString):
    textToMorseDict = {
    'a' : '*-',
    'b' : '-***',
    'c' : '-*-*',
    'd' : '-**',
    'e' : '*',
    'f' : '**-*',
    'g' : '--*',
    'h' : '****',
    'i' : '**',
    'j' : '*---',
    'k' : '-*-',
    'l' : '*-**',
    'm' : '--',
    'n' : '-*',
    'o' : '---',
    'p' : '*--*',
    'q' : '--*-',
    'r' : '*-*',
    's' : '***',
    't' : '-',
    'u' : '**-',
    'v' : '***-',
    'w' : '*--',
    'x' : '-**-',
    'y' : '-*--',
    'z' : '--**'
    }
    
    wordList = inputString.split()
    morsecode = ""
    for word in wordList:
        for i in range(len(word)):
            letter = word[i]
            morsecode+=(textToMorseDict[letter.lower()] + " ")
        morsecode+="  "
        
    print(morsecode)

def main():
    while True:
        userinput = input("Enter text: ")
        convertTextToMorseCode(userinput)
        
    
main()
    
            
            