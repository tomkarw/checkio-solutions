VOWELS = "aeiouy"

def translate(phrase):
    
    n = len(phrase)
    phrase = list(phrase)

    i = 0
    while i < n:
        if phrase[i] == ' ':
            pass
        elif phrase[i] in VOWELS:
            del phrase[i+1:i+3]
            n -= 2
        else:
            del phrase[i+1]
            n -= 1
            
        i += 1
    
    return ''.join(phrase)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
