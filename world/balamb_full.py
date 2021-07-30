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
elevator_service_room = create_object(rooms.Room, key="Elevator Service Room")
exhaust_tunnel = create_object(rooms.Room, key="Exhaust Tunnel")
exhaust_release_room = create_object(rooms.Room, key="Exhaust Release Room")
engine_chamber = create_object(rooms.Room, key="Engine Chamber")
engine_control = create_object(rooms.Room, key="Engine Control Room")


# FLOOR 1

front_gate = create_object(rooms.Room, key="Front Gate")
front_courtyard = create_object(rooms.Room, key="Front Courtyard")
parade_ground = create_object(rooms.Room, key="Parade Ground")
reception = create_object(rooms.Room, key="Reception")
lobby = create_object(rooms.Room, key="Lobby")
upper_lobby = create_object(rooms.Room, key="Upper Lobby")

infirmary_hallway = create_object(rooms.Room, key="Infirmary Hallway")
infirmary = create_object(rooms.Room, key="Infirmary")
treatment_room = create_object(rooms.Room, key="Treatment Room")
recovery_room = create_object(rooms.Room, key="Recovery Room")
store_room = create_object(rooms.Room, key="Store Room")
infirmary_courtyard = create_object(rooms.Room, key="Infirmary Courtyard")

quad_stairs = create_object(rooms.Room, key="Quad Stairs")
quad = create_object(rooms.Room, key="Quad")
quad_garden = create_object(rooms.Room, key="Quad Garden")
quad_courtyard = create_object(rooms.Room, key="Quad Courtyard")

ballroom_lobby = create_object(rooms.Room, key="Ballroom Lobby")
ballroom = create_object(rooms.Room, key="Ballroom")
ballroom_balcony = create_object(rooms.Room, key="Ballroom Balcony")

cafeteria_hallway = create_object(rooms.Room, key="Cafeteria Hallway")
cafeteria = create_object(rooms.Room, key="Cafeteria")
cafeteria_kitchen = create_object(rooms.Room, key="Cafeteria Kitchen")

dormitory_hallway = create_object(rooms.Room, key="Dormitory Hallway")
common_room = create_object(rooms.Room, key="Dormitory Common Room")
sports_ground = create_object(rooms.Room, key="Sports Ground")

parking_hallway = create_object(rooms.Room, key="Parking Hallway")
parking = create_object(rooms.Room, key="Parking")

training_centre_hallway = create_object(rooms.Room, key="Training Centre Hallway")
training_centre_entrance = create_object(rooms.Room, key="Training Centre Entrance")
forest_track = create_object(rooms.Room, key="Forest Track")
mountain_track = create_object(rooms.Room, key="Mountain Track")
river_track = create_object(rooms.Room, key="River Track")
training_centre_lookout = create_object(rooms.Room, key="Training Centre Lookout")
Laboratory = create_object(rooms.Room, key="Laboratory")

library_hallway = create_object(rooms.Room, key="Library Hallway")
library = create_object(rooms.Room, key="Library")
library_study = create_object(rooms.Room, key="Library Study")


# FLOOR 2

classroom_hallway = create_object(rooms.Room, key="Classroom Hallway")
classroom_alpha = create_object(rooms.Room, key="Classroom Alpha")
classroom_bravo = create_object(rooms.Room, key="Classroom Bravo")
classroom_charlie = create_object(rooms.Room, key="Classroom Charlie")
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
# ELEVATOR SERVICE ROOM
###############################################################################

"""
Elevator Service Room

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Elevator Service Room")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS

###############################################################################
# EXHAUST TUNNEL
###############################################################################

"""
Exhaust Tunnel

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Exhaust Tunnel")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS

###############################################################################
# EXHAUST RELEASE ROOM
###############################################################################

"""
Exhaust Release Room

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Exhaust Release Room")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS

###############################################################################
# ENGINE CHAMBER
###############################################################################

"""
Engine Chamber

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Engine Chamber")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS

###############################################################################
# ENGINE CONTROL ROOM
###############################################################################

"""
Engine Control Room

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Engine Control Room")

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
# PARADE GROUND
###############################################################################

"""
Parade Ground

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Parade Ground")

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
# UPPER LOBBY
###############################################################################

"""
Upper Lobby

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Upper Lobby")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS

###############################################################################
# INFIRMARY HALLWAY
###############################################################################

"""
Infirmary Hallway

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Infirmary Hallway")

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
# TREATMENT ROOM
###############################################################################

"""
Treatment Room

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Treatment Room")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS

###############################################################################
# RECOVERY ROOM
###############################################################################

"""
Recovery Room

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Recovery Room")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS

###############################################################################
# STORE ROOM
###############################################################################

"""
Store Room

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Store Room")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS

###############################################################################
# INFIRMARY COURTYARD
###############################################################################

"""
Infirmary Courtyard

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Infirmary Courtyard")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS

###############################################################################
# QUAD STAIRS
###############################################################################

"""
Quad Stairs

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Quad Stairs")

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
# QUAD GARDEN
###############################################################################

"""
Quad Garden

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Quad Garden")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS

###############################################################################
# QUAD COURTYARD
###############################################################################

"""
Quad Courtyard

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Quad Courtyard")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS

###############################################################################
# BALLROOM LOBBY
###############################################################################

"""
Ballroom Lobby

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Ballroom Lobby")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS

###############################################################################
# BALLROOM
###############################################################################

"""
Ballroom

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Ballroom")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS

###############################################################################
# BALLROOM BALCONY
###############################################################################

"""
Ballroom Balcony

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Ballroom Balcony")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS

###############################################################################
# CAFETERIA HALLWAY
###############################################################################

"""
Cafeteria Hallway

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Cafeteria Hallway")

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
# CAFETERIA KITCHEN
###############################################################################

"""
Cafeteria Kitchen

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Cafeteria Kitchen")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS

###############################################################################
# DORMITORY HALLWAY
###############################################################################

"""
Dormitory Hallway

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Dormitory Hallway")

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
# SPORTS GROUND
###############################################################################

"""
Sports Ground

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Sports Ground")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS

###############################################################################
# PARKING HALLWAY
###############################################################################

"""
Parking Hallway

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Parking Hallway")

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
# TRAINING CENTRE HALLWAY
###############################################################################

"""
Training Centre Hallway

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Training Centre Hallway")

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
# River Track
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
# TRAINING ROOM LABORATORY
###############################################################################

"""
Laboratory

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Laboratory")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS

###############################################################################
# LIBRARY HALLWAY
###############################################################################

"""
Library Hallway

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Library Hallway")

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
# LIBRARY STUDY
###############################################################################

"""
Library Study

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Library Study")

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
# CLASSROOM ALPHA
###############################################################################

"""
Classroom Alpha

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Classroom Alpha")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS

###############################################################################
# CLASSROOM BRAVO
###############################################################################

"""
Classroom Bravo

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Classroom Bravo")

front_lobby.db.details = {}
front_lobby.db.details["detail"] = ("Test Detail")

front_lobby.db.ambient_msgs = {}
front_lobby.db.ambient_msgs["Test Ambient Message"] = 1

# ROOM OBJECTS


# ROOM EXITS

###############################################################################
# CLASSROOM CHARLIE
###############################################################################

"""
Classroom Charlie

Details:


Objects:


Features:

    
Exits


"""
front_lobby.db.desc = ("Classroom Charlie")

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