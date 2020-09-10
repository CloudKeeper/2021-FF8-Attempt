"""
Room

Rooms are simple containers that has no location of their own.

"""

from evennia import DefaultRoom
from features import detail_system, ambience_system


class Room(DefaultRoom, detail_system.DetailRoom, ambience_system.AmbientRoom):
    """
    Rooms are like any Object, except their location is None
    (which is default). They also use basetype_setup() to
    add locks so they cannot be puppeted or picked up.
    (to change that, use at_object_creation instead)

    See examples/object.py for a list of
    properties and methods available on all Objects.
    """
    
    # Connected up Detail System.
    # Connect up Ambience System.
    pass
