"""
Batchcode for Balamb Garden.

"""

from evennia import create_object
from typeclasses import rooms, exits, characters

###############################################################################
# INITIATE ROOMS
###############################################################################

# FLOOR 1

# Entrance Rooms
front_gate = create_object(rooms.Room, key="Front Gate")
front_courtyard = create_object(rooms.Room, key="Front Courtyard")
reception = create_object(rooms.Room, key="Reception")
front_lobby = create_object(rooms.Room, key="Lobby")
upper_lobby = create_object(rooms.Room, key="Upper Lobby")

# Debug
placeholder = create_object(rooms.Room, key="Placeholder", attributes=("desc", "To Do."))

###############################################################################
# FRONT GATE
###############################################################################

"""
Front Gate

Details:
    Gargoyles
    View?

Objects:
    Gardens

Features:
    Bus stop / Pick up area for vehicles.
    Can see into Front Courtyard.
    
Exits
    Gate - Exit object. Open when can be used. Closed when it can't.

"""
front_lobby.db.desc = ("Out the front of the Balamb Garden Front Gate.")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS


###############################################################################
# FRONT COURTYARD
###############################################################################

"""
Front Courtyard

Ambience:
    Kinetic Art Instulation.
    Water falls.

Details:
    Lights

Objects:
    Gardens
    Draw Point

Features:
    Bus stop / Pick up area for vehicles.
    Can see into Front gate.
    
Exits:
    Gate - Exit object. Open when can be used. Closed when it can't.
    To Reception

"""
front_lobby.db.desc = ("Just inside the Front gate, on the path leading to the Garden")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS


###############################################################################
# RECPETION
###############################################################################

"""
Reception

Features
    Bridge room.

"""
front_lobby.db.desc = ("Test")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS


###############################################################################
# LOBBY
###############################################################################

"""
Lobby


"""
front_lobby.db.desc = ("Test")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS


###############################################################################
# FRONT GATE
###############################################################################

"""
Upper Lobby

Ambience:
    Fountains below

Details:
    Lights

Objects:
    Lounges

Features:
    Vantage Point for the Lobby
    'watch' for updates in lobby

"""
front_lobby.db.desc = ("Test")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS


###############################################################################

caller.msg(str(front_lobby.dbref) + "created")