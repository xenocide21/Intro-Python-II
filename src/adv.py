from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Declare all items

adv_item = {
    'axe': Item("Axe", "Capable to be thrown."),
    'sword': Item("Sword", "Able to slice and dice."),
    'dagger': Item("Dagger", "Stealthy, yet deadly."),
    'bow': Item("Bow", "Shoot with precision, needs arrows to work."),
    'arrows': Item("Arrows", "Ammo for bow. Unlimited."),
    'potion': Item("Potion", "Drink for health.")
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
room['outside'].items.append(adv_item['axe'])
room['outside'].items.append(adv_item['arrows'])
room['foyer'].items.append(adv_item['potion'])
room['foyer'].items.append(adv_item['bow'])
room['narrow'].items.append(adv_item['dagger'])
room['treasure'].items.append(adv_item['dagger'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player('Bob', room['outside'])

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

def printNameAndDescription(player):
    print(player.current_room.name)
    print(player.current_room.description)
    room_items = "--"
    for item in player.current_room.items:
        room_items += f"{item.name}--"
    print(f"Items in room: {room_items}")

while(True):
    printNameAndDescription(player)
    print("---")
    userInput = input("Move [N]orth\nMove [S]outh\nMove [E]ast\nMove [W]est\n\n[Take <item>] to take item\n[Get <item>] to get item\n[Drop <item>] to drop item in room\nSee [I]nventory\n[Q] to quit\nEnter: ")
    print("---")
    userInput = userInput.lower().strip()
    if userInput == 'q':
        break
    elif userInput == 'i' or userInput == 'inventory':
        player.inventory()
    elif userInput == 'n':
        try:
            player.current_room = player.current_room.n_to
            printNameAndDescription(player)
        except:
            print("Invalid direction pressed. Please try another direction.\n---")
    elif userInput == 's':
        try:
            player.current_room = player.current_room.s_to
            printNameAndDescription(player)
        except:
            print("Invalid direction pressed. Please try another direction.\n---")
    elif userInput == 'w':
        try:
            player.current_room = player.current_room.w_to
            printNameAndDescription(player)
        except:
            print("Invalid direction pressed. Please try another direction.\n---")
    elif userInput == 'e':
        try:
            player.current_room = player.current_room.e_to
            printNameAndDescription(player)
        except:
            print("Invalid direction pressed. Please try another direction.\n---")
    elif len(userInput.split(" ")) == 2:
        verb, item = userInput.split(" ")
        found = False
        if verb == "take" or verb == "get":
            for room_item in player.current_room.items:
                if item == room_item.name.lower():
                    player.current_room.items.remove(adv_item[item])
                    player.items.append(adv_item[item])
                    found = True
                    adv_item[item].on_take()
                    break
            if found == False:
                print("Item isn't in the room. Please try again.\n---")
        elif verb == "drop":
            for player_item in player.items:
                if item == player_item.name.lower():
                    player.items.remove(adv_item[item])
                    player.current_room.items.append(adv_item[item])
                    found = True
                    adv_item[item].on_drop()
                    break
            if found == False:
                print("Player doesn't have item. Please try again.\n---")
        else:
            print("Invalid action. Please try again.\n---")
    else:
        print("Invalid response. Please try again.\n---")
