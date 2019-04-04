class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
    
    @property
    def is_alive(self):
        return self.health > 0
        
class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7

def fight(unit1, unit2):
    
    while unit1.is_alive:
        
        unit2.health -= unit1.attack
        
        if not unit2.is_alive:
            break
        
        unit1.health -= unit2.attack
    
    return unit1.is_alive
    
def fight(u1, u2):

    alternate = cycle([u1, u2])

    while u1.is_alive and u2.is_alive:

        attacker, attacked = next(alternate), next(alternate)

        attacked.health -= attacker.attack

        next(alternate) # skip one to alternate roles

    return u1.is_alive



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")
