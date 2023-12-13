'''
Author: Ashley Muka
Assignment Title: Animal Sounds
Assignment Description:Create a program to model different types of mammals and their sounds
Due Date:10/23/2023
Dae Created:10/23/2023
Date Last Modified:10/23/2023
'''

#process
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
        
#output
def display_info(mammal):
    mammal.show_species()
    mammal.make_sound()

if __name__ == "__main__":
    regular_mammal = Mammal('regular mammal')
    dog = Dog()
    cat = Cat()
    
#process
    display_info(regular_mammal)
    display_info(dog)
    display_info(cat)
    
#input
    species = input()
    
#process and output
    if species == 'dog':
        dog = Dog()
        display_info(dog)

    elif species == 'cat':
        cat = Cat()
        display_info(cat)
    else:
        new_mammal = Mammal(species)
        display_info(new_mammal)
