# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.items = []

    def inventory(self):
        player_items = ''
        for item in self.items:
            player_items += f'=={item.name}\n'
        print(f'Items in inventory:\n{player_items}==========================================\n')

    def __str__(self):
        return f'Player(name: {self.name}, location: {self.location})'
