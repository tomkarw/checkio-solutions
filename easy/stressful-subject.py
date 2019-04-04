import re

def is_stressful(subj):
    """
        recognise stressful subject
    """
    
    if subj.isupper() or \
        subj.endswith('!!!'):
        return True
        
    subj = subj.lower()
    
    if re.search(r'h\S*e\S*l\S*p',subj) or \
        re.search(r'u\S*r\S*g\S*e\S*n\S*t',subj) or \
        re.search(r'a\S*s\S*a\S*p',subj):
        return True
        
    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')
