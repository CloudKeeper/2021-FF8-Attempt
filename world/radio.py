# 
from evennia import create_object
from typeclasses import rooms, exits, characters
from features import radio_objects
from evennia.utils import search

radio = create_object(radio_objects.RadioObj, key="Radio", location=caller.location)
radio.db.radio_switch = True
channel = search.search_channel("Public")[0]
channel.connect(radio)