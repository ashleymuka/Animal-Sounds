'''
Description:Create a program to model different types of mammals and their sounds
'''

class Mammal:
    def __init__(self, species):
        self.species = species

    def show_species(self):
        print(f"I am a {self.species}")

    def make_sound(self):
        print("Grrrr")

class Dog(Mammal):
    def __init__(self):
        Mammal.__init__(self, "dog")  

    def make_sound(self):
        print("woof, woof")

class Cat(Mammal):
    def __init__(self):
        Mammal.__init__(self, "cat")  

    def make_sound(self):
        print("meow")
        
def display_info(mammal):
    mammal.show_species()
    mammal.make_sound()

if __name__ == "__main__":
    regular_mammal = Mammal('regular mammal')
    dog = Dog()
    cat = Cat()

    display_info(regular_mammal)
    display_info(dog)
    display_info(cat)
    
    species = input()
    
    if species == 'dog':
        dog = Dog()
        display_info(dog)

    elif species == 'cat':
        cat = Cat()
        display_info(cat)
    else:
        new_mammal = Mammal(species)
        display_info(new_mammal)
