def add(a, b):
    return a + b

class Test:
    def __init__(self, add_function):
        self.add_function = add_function

test = Test(add_function=add)
print(test.add_function(1, 2))

# Create a Monster class with a parameter called func, store this func as a parameter

class Monster:
    def __init__(self, func):
        self.func = func

# Create another class called Attack, that has 4 methods:
# bite, strike, slash, kick

class Attack:
    def bite(self):
        print('The monster bites')

    def strike(self):
        print('The monster strikes')

    def slash(self):
        print('The monster slashes')

    def kick(self):
        print('The monster kicks')

# Create a monster object and give it one of the attack methods from the attack class
attacks = Attack().bite
monster = Monster(func=attacks)
monster.func()

monster = Monster(func=Attack().kick)
monster.func()