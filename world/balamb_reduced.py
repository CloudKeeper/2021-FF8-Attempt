"""
Batchcode for Balamb Garden.

"""

from evennia import create_object
from typeclasses import rooms, exits, characters

###############################################################################
# INITIATE ROOMS
# Rooms are created first, as adding exits and details will cross refer to 
# different locations which would otherwise not be instantiated yet.
###############################################################################


# BASEMENT

underground_chamber = create_object(rooms.Room, key="Underground Chamber")
garden_masters_office = create_object(rooms.Room, key="Garden Master's Office")


# FLOOR 1

front_gate = create_object(rooms.Room, key="Front Gate")
front_courtyard = create_object(rooms.Room, key="Front Courtyard")
reception = create_object(rooms.Room, key="Reception")
lobby = create_object(rooms.Room, key="Lobby")

infirmary = create_object(rooms.Room, key="Infirmary")

quad = create_object(rooms.Room, key="Quad")

cafeteria = create_object(rooms.Room, key="Cafeteria")

common_room = create_object(rooms.Room, key="Dormitory Common Room")

parking = create_object(rooms.Room, key="Parking")

training_centre_entrance = create_object(rooms.Room, key="Training Centre Entrance")
forest_track = create_object(rooms.Room, key="Forest Track")
mountain_track = create_object(rooms.Room, key="Mountain Track")
river_track = create_object(rooms.Room, key="River Track")
training_centre_lookout = create_object(rooms.Room, key="Training Centre Lookout")

library = create_object(rooms.Room, key="Library")

# FLOOR 2

classroom_hallway = create_object(rooms.Room, key="Classroom Hallway")
classroom = create_object(rooms.Room, key="Classroom")
escape_balcony = create_object(rooms.Room, key="Escape Balcony")


# FLOOR 3

headmasters_lobby = create_object(rooms.Room, key="Headmaster's Lobby")
headmasters_office = create_object(rooms.Room, key="Headmaster's Office")

###############################################################################
#
# BASEMENT
#
###############################################################################

###############################################################################
# UNDERGROUND CHAMBER
###############################################################################

"""
Underground Chamber

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Underground Chamber")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS

###############################################################################
# GARDEN MASTERS OFFICE
###############################################################################

"""
Garden Master's Office

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Garden Master's Office")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS

###############################################################################
#
# FLOOR 1
#
###############################################################################

###############################################################################
# FRONT GATE
###############################################################################

"""
Front Gate

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Front Gate")

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

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Front Courtyard")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS

###############################################################################
# RECEPTION
###############################################################################

"""
Reception

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Reception")

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

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Lobby")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS

###############################################################################
# INFIRMARY
###############################################################################

"""
Infirmary

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Infirmary")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS

###############################################################################
# QUAD
###############################################################################

"""
Quad

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Quad")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS

###############################################################################
# CAFETERIA
###############################################################################

"""
Cafeteria

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Cafeteria")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS

###############################################################################
# DORMITORY COMMON ROOM
###############################################################################

"""
Dormitory Common Room

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Dormitory Common Room")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS

###############################################################################
# PARKING
###############################################################################

"""
Parking

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Parking")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS

###############################################################################
# TRAINING CENTRE ENTRANCE
###############################################################################

"""
Training Centre Entrance

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Training Centre Entrance")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS

###############################################################################
# FOREST TRACK
###############################################################################

"""
Forest Track

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Forest Track")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS

###############################################################################
# MOUNTAIN TRACK
###############################################################################

"""
Mountain Track

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Mountain Track")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS

###############################################################################
# RIVER TRACK
###############################################################################

"""
River Track

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("River Track")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS

###############################################################################
# TRAINING CENTRE LOOKOUT
###############################################################################

"""
Training Centre Lookout

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Training Centre Lookout")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS

###############################################################################
# LIBRARY
###############################################################################

"""
Library

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Library")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS

###############################################################################
# CLASSROOM HALLWAY
###############################################################################

"""
Classroom Hallway

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Classroom Hallway")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS

###############################################################################
# CLASSROOM
###############################################################################

"""
Classroom

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Classroom")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS

###############################################################################
# ESCAPE BALCONY
###############################################################################

"""
Escape Balcony

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Escape Balcony")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS

###############################################################################
# HEADMASTERS LOBBY
###############################################################################

"""
Headmaster's Lobby

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Headmaster's Lobby")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS

###############################################################################
# HEADMASTERS OFFICE
###############################################################################

"""
Headmaster's Office

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Headmaster's Office")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS

##############################################################################

caller.msg(str(front_lobby.dbref) + "created")