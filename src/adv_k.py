from room_k import Room
from player_k import Player
from items import Item

# Items
knife = Item('knife', 'hunting')
plate = Item('plate', 'dirty')
book = Item('book', 'constitution')
hat = Item('hat', 'fedora')

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", items=[knife, book]),

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


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

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

# Declare gameplay variables
player = Player(None, room["outside"], items=[knife, hat])
user_input = None
new_room = None



#gamplay loop

while not user_input == "q":
    
    if user_input != None and len(user_input.split(' '))>1:
        print('two words')
        user_input_w = user_input.split(' ')

        got_thing = None
        iter = 0

        for thing in player.current_room.items:
            if user_input_w[0] == 'get' and user_input_w[1] == thing.name:
                print(f'got {thing.name} ')
                got_thing = True
            

                break        
            iter = iter+1
        if got_thing != True:
                
            print(f"There's no {user_input_w[1]} in the room")
        else:
            player.items.append(player.current_room.items.pop(iter))
            # player.current_room.items.pop(iter)
            print(', '.join([thing.name for thing in player.items]))
            print(', '.join([thing.name for thing in player.current_room.items]))    

    #   * If it is there, remove it from the `Room` contents, and add it to the
    #    `Player` contents.      

    if player.name == None and user_input is not None:
        player.name = user_input
    
    if user_input == "n":
        new_room = player.current_room.n_to

    elif user_input == "s":
        new_room = player.current_room.s_to

    elif user_input == "e":
        new_room = player.current_room.e_to
        
    elif user_input == "w":
        new_room = player.current_room.w_to
    else:
        print("Invalid selection. Please try again.")

    if new_room == None:
        print(f"You hit a wall, you look around to assess the damage. Memory starts to slowly come back to you and you recognize this place.")
    else:
        # player made the right choice
        player.current_room = new_room

    # lets name the player 
    if player.name == None:
        user_input = str(input(f"What is your name? Keep it civil pls and don't drop your {' and '.join([predmet.description + ' ' + predmet.name  for predmet  in player.items])}.\n")).capitalize()
        # user_input = str(input(f"What is your name? Keep it civil pls and don't drop your {player.items[0].description} {player.items[0].name}.\n")).capitalize()
    else:        
        print(f"You are in {player.current_room.name}. {player.current_room.description}. There are some objects here: {', '.join([predmet.name for predmet  in player.current_room.items])}")
        user_input = str(input("[N]orth (remembers)    [S]outh    [E]ast    [W]est(eros)    [Q]uit\n")).lower()

    
