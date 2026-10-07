# Class create to be able to create new objects -new characters- just using this as a template.
# This can be done by calling the function and providing a name and number of items (seeds and money).

class Character:
    def __init__(self, name, seeds, money):
        self.name = name
        self.seeds = seeds
        self.money = money
