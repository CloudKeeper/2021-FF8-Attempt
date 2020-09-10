"""
Radio Objects - Not Working

These objects, when subscribed to a channel, will echo messages either to the 
room they are in (like a radio) or to their own contents (like a loudspeaker).

"""
from evennia.comms.models import ChannelDB
from evennia.utils import utils
from evennia import DefaultObject, DefaultScript, TICKER_HANDLER
import random, sys


class RadioObj(DefaultObject):
    """
    Objects that subscribe to channels and relay the messages they receive
    to the room they are in or their contents.
    """

    def at_object_creation(self):
        """
        Adds Database Attributes:
            radio_switch (Bool): Will only echo messages if True
        """
        super(RadioObj, self).at_object_creation()
        self.db.radio_switch = False

    def msg(self, text=None, from_obj=None, session=None, options=None, **kwargs):
        """
        Channels send their messages with a marker. We check for the marker
        and echo it to the room if the marker is found and radio is on.
        """
        if options and self.db.radio_switch:
            if "from_channel" in options:
                # Radio Object
                if  self.location:
                    self.location.msg_contents(text, exclude=self)
                # Radio Room
                else:
                    self.msg_contents(text)
        super(RadioObj, self).msg()
