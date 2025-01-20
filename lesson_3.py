# Scope problem

# def update_health(amount):
#     global health
#     health += amount
#
#
# health = 10
# print(update_health(10))

class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    def update_energy(self, amount):
        self.energy += amount

    def get_damage(self, amount):
        self.health -= amount

monster = Monster(health=100, energy=50)
# monster.update_energy(20)
print(monster.energy)

# Create a hero class with two parameters: damage, monster

class Hero:
    def __init__(self, damage, monster):
        self.damage = damage
        self.monster = monster

# The monster class should have a method that lowers the health -> get_damage(amount)

# The hero class should have an attack method that calls the get_damage method from the monster
    def attack(self):
        self.monster.get_damage(self.damage)

hero = Hero(damage=20, monster=monster)
print(monster.health)
hero.attack()
print(monster.health)