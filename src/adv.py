from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

item_list = {
    'robe_of_protection': Item("Robe_of_Protection", "A robe enchanted with magical powers."),
    'silver_dagger': Item("Silver_Dagger", "A dagger that deals enhanced damage to undead creatures."),
    'ring_of_lightning_bolt': Item("Ring_of_Lightning_Bolt", "A powerful ring that casts a bolt of lightning at your enemies."),
    'lesser_healing_potion': Item("Lesser_Healing_Potion", "A potion that grants a small amount of health."),
    'lesser_mana_potion': Item("Lesser_Mana_Potion", "A potion that regenerates a small amount of Mana."),
    'night_vision_potion': Item("Night_Vision_Potion", "Grants enhanced vision in the dark.")
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Link items to rooms
room['outside'].items.append(item_list['night_vision_potion'])
room['outside'].items.append(item_list['silver_dagger'])
room['foyer'].items.append(item_list['robe_of_protection'])
room['overlook'].items.append(item_list['ring_of_lightning_bolt'])
room['narrow'].items.append(item_list['lesser_healing_potion'])
room['narrow'].items.append(item_list['lesser_mana_potion'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Ashley', room['outside'])


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
def print_player_details(player):
    print(player.location.name)
    print(player.location.description)
    items = '=='
    for item in player.location.items:
        items += f'{item.name}=='
    print(f'Items in room: {items}')


while True:
    print('==========================================')
    print('==========================================')
    print_player_details(player)
    user_input = input(
        'Move [North]\nMove [South]\nMove [East]\nMove [West]\n\n[Get <item>] to get item\n[Drop <item>] to drop item\nOpen [Inventory]\n[Quit] to quit\nWhat do you want to do?')
    user_input = user_input.lower().strip()

    if user_input == 'q' or user_input == 'quit':
        break
    elif user_input == 'i' or user_input == 'inventory':
        player.inventory()
    elif user_input == 'n' or user_input == 'north':
        try:
            player.location = player.location.n_to
            print_player_details(player)
        except:
            print("Invalid direction pressed. Please try another direction.\n---")
    elif user_input == 's' or user_input == 'south':
        try:
            player.location = player.location.s_to
            print_player_details(player)
        except:
            print("Invalid direction pressed. Please try another direction.\n---")
    elif user_input == 'w' or user_input == 'west':
        try:
            player.location = player.location.w_to
            print_player_details(player)
        except:
            print("Invalid direction pressed. Please try another direction.\n---")
    elif user_input == 'e' or user_input == 'east':
        try:
            player.location = player.location.e_to
            print_player_details(player)
        except:
            print("Invalid direction pressed. Please try another direction.\n---")
    elif len(user_input.split(" ")) == 2:
        verb, item = user_input.split(" ")
        found = False
        if verb == "get":
            for room_item in player.location.items:
                if item == room_item.name.lower():
                    player.location.items.remove(item_list[item])
                    player.items.append(item_list[item])
                    found = True
                    item_list[item].on_take()
                    break
            if not found:
                print("Item isn't in the room. Please try again.\n---")
        elif verb == "drop":
            for player_item in player.items:
                if item == player_item.name.lower():
                    player.items.remove(item_list[item])
                    player.location.items.append(item_list[item])
                    found = True
                    item_list[item].on_drop()
                    break
            if not found:
                print("Player doesn't have item. Please try again.\n---")
        else:
            print("Invalid action. Please try again.\n---")
    else:
        print("Invalid response. Please try again.\n---")
