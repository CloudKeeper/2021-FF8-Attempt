"""
Pose System - To be Tested

Pose system to set room-persistent poses, visible in room descriptions and 
when looking at the person/object.  This is a simple Attribute that modifies 
how the characters is viewed when in a room as sdesc + pose. Moving to a 
new room resets your pose to the default.

NOTES:
-Use Handler instead?

"""
from evennia import DefaultObject
from django.conf import settings
from evennia.utils import utils

COMMAND_DEFAULT_CLASS = utils.class_from_module(settings.COMMAND_DEFAULT_CLASS)


class PoseMixin(DefaultObject):
    """
    This class implements the base functionality for poses.
    
    PoseMixin - Overwrites:
        (super) at_object_creation
        get_display_name
        return_appearance
    """

    def at_object_creation(self):
        """
        Called at initial creation.
        """
        super().at_object_creation()

        # emoting/recog data
        self.db.pose = ""
        self.db.pose_default = ""
        
    def get_display_name(self, looker, **kwargs):
        """
        Displays the name of the object in a viewer-aware manner.

        Args:
            looker (TypedObject): The object or account that is looking
                at/getting inforamtion for this object.

        Kwargs:
            pose (bool): Include the pose (if available) in the return.

        Returns:
            name (str): A string containing the name of the object, DBREF for
                        builers and above, and pose if requested.

        """
        dbref = "(#%s)" % self.id if self.access(looker, access_type="control") else ""
        pose = " %s" % (self.db.pose or "") if kwargs.get("pose", False) else ""
        return "%s%s%s" % (self.name, dbref, pose)

    def return_appearance(self, looker):
        """
        This formats a description. It is the hook a 'look' command
        should call.

        Args:
            looker (Object): Object doing the looking.
        """
        if not looker:
            return ""
        # get and identify all objects
        visible = (con for con in self.contents if con != looker and con.access(looker, "view"))
        exits, users, things = [], [], []
        for con in visible:
            key = con.get_display_name(looker, pose=True)
            if con.destination:
                exits.append(key)
            elif con.has_account:
                users.append(key)
            else:
                things.append(key)
        # get description, build string
        string = "|c%s|n\n" % self.get_display_name(looker, pose=True)
        desc = self.db.desc
        if desc:
            string += "%s" % desc
        if exits:
            string += "\n|wExits:|n " + ", ".join(exits)
        if users or things:
            string += "\n " + "\n ".join(users + things)
        return string

    def at_after_move(self, source_location, **kwargs):
        """
        Called after move has completed, regardless of quiet mode or
        not.  Allows changes to the object due to the location it is
        now in.
        Args:
            source_location (Object): Wwhere we came from. This may be `None`.
            **kwargs (dict): Arbitrary, optional arguments for users
                overriding the call (unused by default).
        """
        super().at_object_creation(source_location, **kwargs)
        self.db.pose = self.attributes.get("pose_default", default = "")



class CmdPose(COMMAND_DEFAULT_CLASS):
    """
    Set a static pose

    Usage:
        pose <pose> # Sets pose
        pose/default # Resets pose
        pose/default <pose> # Set pose to be reset to
        pose obj = <pose> # Pose another object
        pose/default obj # Reset another objects pose
        pose/default obj = <pose> # Set objects pose to reset to

    Examples:
        pose leans against the tree
        pose is talking to the barkeep.
        pose box = is sitting on the floor.

    """

    key = "pose"
    # aliases = [""]
    switch_options = ("default")

    def func(self):
        "Create the pose"
        args = self.args
        caller = self.caller
        switches = self.switches
        
        # Reset target/self to default pose
        if any(switch in switches for switch in ["reset"]):
            if args:
                target = caller.search(args)
                if not target:
                    return
            else:
                target = caller
            
            # Is caller permitted to do this?
            if not target.access(caller, "edit"):
                caller.msg("You can't pose that.")
                return
            
            if not target.attributes.has("pose"):
                caller.msg(f"{target.name} cannot be posed.")
                return
            
            target.db.pose = target.attributes.get("pose_default", default = "")
            return
        
        # Handle no arguments
        if not self.args:
            caller.msg("Usage: pose <pose> OR pose obj = <pose>")
        
        pose = self.rhs if self.rhs else self.lhs
        target = self.lhs if self.rhs else None
        
        # Dress up the pose string
        if not pose.endswith("."):
            pose = f"{pose}."
        
        # Set target to target or self.
        if target:
            target = caller.search(target)
            if not target:
                return
            if not target.access(caller, "edit"):
                caller.msg("You can't pose that.")
                return
            if not target.attributes.has("pose"):
                caller.msg(f"{target.name} cannot be posed.")
                return
        else:
            target = self.caller
            
        # Length check pose.
        if len(target.name) + len(pose) > 60:
            caller.msg(f"Your pose '{pose}' is too long.")
            return
            
        # Set new default pose
        if any(switch in switches for switch in ["default"]):
            target.db.pose_default = pose
            caller.msg(f"Default pose is now '{target.get_display_name()}'.")
            return
        
        # Setting new temporary pose.
        target.db.pose = pose
        caller.msg(f"Pose will read '{target.name} {pose}'.")
