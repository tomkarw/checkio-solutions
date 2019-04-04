# Taken from mission Army Battles

from itertools import cycle

class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
    
    @property
    def is_alive(self) -> bool:
        return self.health > 0
        
    def __str__(self):
        return str(self.health)
        
class Knight(Warrior):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attack = 7

class Defender(Warrior):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.health = 60
        self.attack = 3
        self.defense = 2
        
    
def fight(unit1, unit2):
    
    while unit1.is_alive:
        
        reduction = unit1.attack - unit2.__dict__.get('defense',0)
        if reduction < 0:
            reduction = 0
        unit2.health -= reduction
        
        if not unit2.is_alive:
            break
        
        reduction = unit2.attack - unit1.__dict__.get('defense',0)
        if reduction < 0:
            reduction = 0
        unit1.health -= reduction
    
    return unit1.is_alive
  
class Army:
    
    def __init__(self):
        self.units = []
        
    def add_units(self, unit: Warrior, number: int):
        for _ in range(number):
            self.units += [unit()]
        
    def __str__(self):
        return ','.join(str(unit) for unit in self.units)
        
class Battle:
    
    def fight(self,army1: Army, army2: Army):
        
        i = 0
        j = 0
        while i < len(army1.units) and j < len(army2.units):
            print(army1,army2)
            if fight(army1.units[i],army2.units[j]):
                print(i,j)
                j += 1
            else:
                print(i,j)
                i += 1

        return i < len(army1.units)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")
