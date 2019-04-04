def check_connection(network, first, second, depth=0):
    
    depth += 1
    
    if depth > len(network):
        return False
    
    for pair in network:
        if first in pair and second in pair:
            return True
    
    results = []
    
    for link in network:
        pair = link.split('-')
        if first == pair[0]:
            results += [check_connection(network, pair[1], second, depth)]
        elif first == pair[1]:
            results += [check_connection(network, pair[0], second, depth)]
    
    return any(results)
    


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    """
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
    """
