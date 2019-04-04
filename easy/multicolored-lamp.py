class Lamp:
    
    colors = ['Green','Red','Blue','Yellow']
    
    def __init__(self):
        def gen():
            i = 0
            while True:
                yield self.colors[i]
                i = (i+1)%4
        self.g = gen()
    
    def light(self):
        return next(self.g)
        

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    lamp_1 = Lamp()
    lamp_2 = Lamp()
    
    print(lamp_1.light()) #Green
    lamp_1.light() #Red
    lamp_2.light() #Green
    
    assert lamp_1.light() == "Blue"
    assert lamp_1.light() == "Yellow"
    assert lamp_1.light() == "Green"
    assert lamp_2.light() == "Red"
    assert lamp_2.light() == "Blue"
    print("Coding complete? Let's try tests!")
