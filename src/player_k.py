# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:

    name = None
    current_room = None
    items = []

    def __init__(self, name, current_room, items=[]):
        self.name = name
        self.current_room = current_room
        self.items = items

    def cheer(self):
        return 'huzzah'

    def on_take(self, item):
        # player.items.append(player.current_room.items.pop(iter))
        self.items.append(item)
        self.current_room.items.remove(item)

        print(f'You took {item.name}')

    def on_drop(self, item):
        self.items.remove(item)
        self.current_room.items.append(item)

        print(f'You dropped {item.name}')

