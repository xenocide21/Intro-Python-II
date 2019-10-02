# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def inventory(self):
        player_items = "--"
        for item in self.items:
            player_items += f"{item.name}--"
        print(f"Items on player: {player_items}\n---")