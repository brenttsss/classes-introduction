
# Classes Introduction
# Brenton Suriah
# 17 January 2025

# Classes, by convention, are written in CamelCase whereas variables are written in snake_case

# Create class
class Monster:

    # Dunder method can create attributes
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    def __len__(self):
        return self.health

    def __abs__(self):
        return self.energy

    def __call__(self):
        return 'The monster was called'

    def __add__(self, other):
        return self.health + other

    def __str__(self):
        return f'A monster with health {self.health} and energy {self.energy}'

    # Methods
    def attack(self, amount):
        print("The monster has attacked!")
        print(f"It has attacked for {amount} damage!")
        self.energy -= 20
        print(self.energy)

    def move(self, speed):
        print('The monster has moved')
        print(f'It has a speed of {speed}')

# Turn the class in an object
monster = Monster(10, 20)
print(monster)