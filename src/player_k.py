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

