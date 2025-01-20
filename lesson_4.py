class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    # Methods
    def attack(self, amount):
        print("The monster has attacked!")
        print(f"It has attacked for {amount} damage!")
        self.energy -= 20

    def move(self, speed):
        print('The monster has moved')
        print(f'It has a speed of {speed}')


class Shark(Monster):
    def __init__(self, speed, health, energy):
        # Monster.__init__(self, health, energy)
        super().__init__(health, energy)
        super().move(10)
        self.speed = speed

    def bite(self):
        print('The shark bites')

    def move(self):
        print('The shark moves')
        print(f'It has a speed of {self.speed}')

# Create scorpion class that inherits from monster
# Health and energy from the parent

class Scorpion(Monster):
    def __init__(self, poisson_damage, scorpion_health, scorpion_energy):
        super().__init__(scorpion_health, scorpion_energy)
        self.poison_damage = poisson_damage

    def attack(self):
        print('The scorpion has attacked!')
        print(f'It has delt a poison damage of {self.poison_damage}')

# poisson_damage attribute
# Overwrite the damage method to show poison damage

scorpion = Scorpion(poisson_damage=50, scorpion_health=20, scorpion_energy=10)
print(scorpion.health)
print(scorpion.energy)