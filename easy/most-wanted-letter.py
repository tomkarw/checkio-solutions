import string

def checkio(text: str) -> str:
    
    text = str.lower(text)
    
    letterDict = dict()
    
    for char in text:
        if char in string.ascii_lowercase:
            letterDict[char] = letterDict.get(char,0) + 1
    
    #print(letterDict)
    
    sortedLetterDict = sorted(letterDict.items(),key = lambda kv: kv[1],reverse = True)
    
    #print(sortedLetterDict)
    
    maxList = []
    for kv in sortedLetterDict:
        if kv[1] == sortedLetterDict[0][1]:
            maxList += [kv]
        else:
            break
    
    #print(maxList)
    
    sortedMaxList = sorted(maxList, key = lambda kv: kv[0])
    
    #print(sortedMaxList)
    
    return sortedMaxList[0][0]

def checkio(text: str) -> str:

    """
    We iterate through latyn alphabet and count each letter in the text.
    Then 'max' selects the most frequent letter.
    For the case when we have several equal letter,
    'max' selects the first from them.
    """

    text = text.lower()

    return max(string.ascii_lowercase, key=text.count)

if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
