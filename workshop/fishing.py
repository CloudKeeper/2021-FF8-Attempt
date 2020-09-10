"""
Fishing - TO BE TESTED

Fish in a suitable room.


"""

import time
from django.conf import settings
from evennia.utils import utils, evmenu
from evennia import CmdSet
from evennia.utils.create import create_object
from typeclasses.objects import Object

COMMAND_DEFAULT_CLASS = utils.class_from_module(settings.COMMAND_DEFAULT_CLASS)

# ------------------------------------------------------------------------------
# Camera Commands - Calls the camera.use_object() function
# ------------------------------------------------------------------------------


class CmdUse(COMMAND_DEFAULT_CLASS):
    """
    Use an object with the at_use() hook.

    Usage:
        use <obj> [on/with <target>, <target>] =['say message][:pose message][:'say message]

    The command simply sanity checks arguments before calling the objects
    at_use() function.
    """
    key = "use"
    aliases = ["read"]
    locks = "cmd:all()"
    help_category = "General"

    def func(self):
        """Use an object."""

        # Set up function variables.
        caller = self.caller
        args = self.lhs
        for splitter in (" on ", " with "):  # try each delimiter
            if splitter in args:  # to find first successful split
                args = self.lhs.split(splitter)
                break
        obj = args[0].strip() if len(args) >= 1 else None
        targets = [arg.strip() for arg in args[1](",")] if len(args) > 1 else None

        # No target
        if not obj:
            caller.msg("Use what?")
            return

        # Can't find target
        obj = caller.search(obj)
        if not obj:
            return

        # Unsuitable target
        if not getattr(obj, "at_use", None):
            caller.msg("You cannot use this object.")
            return

        # If targets given: find targets.
        if targets:
            subjectlist = []
            for target in targets:
                subject = self.caller.search(target)
                if not subject:
                    caller.msg("'{}' could not be located.".format(target))
                    return
                subjectlist.append(subject)

        # # Handle roleplay
        # if self.rhs:
        #     _roleplay(self, caller, self.rhs.split(":"))

        # Call use_object hook on object.
        obj.at_use(caller, subjectlist)

# ------------------------------------------------------------------------------
# Camera Object - Creates photographs when used.
# ------------------------------------------------------------------------------


class Rod(Object):

    def at_use(self, bait):

        # Call rooms fishing Function (rod, bait)

# ------------------------------------------------------------------------------
# Photograph Object - Uses menus to mimic location when photograph taken.
# ------------------------------------------------------------------------------


class FishingRoom():
    """
    This is a mixin that provides object functionality for fishing.
    """

    def at_fish(self, detailkey):
        """
        This looks for an Attribute "obj_details" and possibly
        returns the value of it.

        Args:
            detailkey (str): The detail being looked at. This is
                case-insensitive.

        """
        # Accumulate value of bait
        # Run through odds and get winnings.
        # Match result against table
        # Return random result from table
