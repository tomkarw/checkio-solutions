def subnetworks(net, crushes):
    
    def walk(source):
        for edge in net:
            if source in edge:
                net.remove(edge)
                edge.remove(source)
                walk(edge[0])
        
    for crush in crushes:
        for edge in net:
            if crush in edge:
                net.remove(edge)
    
    mayors = 0
    
    while net != []:
        
        mayors += 1
        
        walk(net[0])
        
    return mayors
                
        
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert subnetworks([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ], ['B']) == 2, "First"
    assert subnetworks([
            ['A', 'B'],
            ['A', 'C'],
            ['A', 'D'],
            ['D', 'F']
        ], ['A']) == 3, "Second"
    assert subnetworks([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ], ['C', 'D']) == 1, "Third"
    print('Done! Check button is waiting for you!')
