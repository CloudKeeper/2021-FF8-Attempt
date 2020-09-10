"""
Detail Objects - Needs Testing.

A Detail Object is an object which sits in a room holding either a descriptioni 
or a reference to a completely seperate room. It is effectively invisible but 
when 'look objname' is used, it will provide the description or the description
of the referenced room.

Like SeeThroughExit but without the exit.

View lock stops it from appearing in a rooms content list.
We make view lock stop the get command, whilst pretending there is no object.
We allow people to look at it but forward the target's appearance.

Attributes - Used if available:
    target - The room who's description will be displayed on look.
    desc - Will display instead of target's description.
    preamble - Displayed before destination's description.

"""

from evennia import DefaultObject
from evennia.utils import utils

# -----------------------------------------------------------------------------
# Ambient Message Storage
# -----------------------------------------------------------------------------

class DetailObjectMixin(DefaultObject):
    """
    A Vantage Point is an object which sits in a room holding a reference to a 
    completely seperate room. It is effectively invisible but when 'look objname' 
    is used, it will provide the description of the reference room.
    
    Attributes - Used if available:
        destination - The room who's description will be displayed on look.
        desc - Will display instead of target's description.
        preamble - Displayed before destination's description
    """
    
    def at_object_creation(self):
        super().at_object_creation()
        self.locks.add("view:false()")

    def return_appearance(self, looker):
        """
        This formats a description. It is the hook a 'look' command
        should call.

        Args:
            looker (Object): Object doing the looking.
        """
        if not looker:
            return ""
        
        string = ""
        
        # If exit has a description, use that instead.
        desc = self.db.desc
        if desc:
            string += "%s" % desc
            return string
        
        target = self.db.target
        # If no target, pretend nothings here.
        if not target:
            return f"Could not find '{target.key}'"
        
        # display preamble and it's description.
        preamble = self.attributes.get("preamble", 
                       default = "Looking in this direction you see:")
        string += f"{preamble}\n"
        
        # Add target description
        string += f"{looker.at_look(target)}"
        return string

    def at_before_get(self, getter, **kwargs):
        """
        Called by the default `get` command before this object has been
        picked up.

        Args:
            getter (Object): The object about to get this object.
            **kwargs (dict): Arbitrary, optional arguments for users
                overriding the call (unused by default).

        Returns:
            shouldget (bool): If the object should be gotten or not.

        Notes:
            If this method returns False/None, the getting is cancelled
            before it is even started.
        """
        # Default get lock gives away objects existance. It's more designed for
        # heavy objects, where you know it's there but you can't pick it up.
        # This uses the view lock to determine that you can't pick it up and 
        # pretends like there is no object there.
        if not self.access(getter, "view", default=True):
            getter.msg(f"Could not find '{self.key}'")
            return False
        return True
