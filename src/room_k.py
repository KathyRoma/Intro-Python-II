# Implement a class to hold room information. This should have name and
# description attributes.


#  Room("Grand Overlook", """A steep cliff appears before you, falling
# into the darkness. Ahead to the north, a light flickers in
# the distance, but there is no way across the chasm.""")

class Room:

    name = None
    description = None
    n_to = None 
    s_to = None
    e_to = None
    w_to = None
    items = []

    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items
