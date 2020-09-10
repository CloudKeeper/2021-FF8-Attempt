"""
Vehicles - TO BE TESTED

Automated Vehicles


"""

from evennia import utils, settings, CmdSet
from typeclasses.objects import Object

COMMAND_DEFAULT_CLASS = utils.class_from_module(settings.COMMAND_DEFAULT_CLASS)

# ------------------------------------------------------------------------------
# Vehicle Object - Moves between one or more locations automatically
# ------------------------------------------------------------------------------

class AutomatedVehicle(Object):

    def at_object_creation(self):
        # We'll add in code here later.
        self.cmdset.add_default(VehicleCmdSet)


# ------------------------------------------------------------------------------
# Inside Lock Function - Returns True if object is characters location.
# ------------------------------------------------------------------------------

def cmdinside(accessing_obj, accessed_obj, *args, **kwargs):
    """
    Usage: cmdinside() 
    Used to lock commands and only allows access if the command
    is defined on an object which accessing_obj is inside of.     
    """
    return accessed_obj.obj == accessing_obj.location


# ------------------------------------------------------------------------------
# Vehicle Commands - Allows departing from vehicles.
# ------------------------------------------------------------------------------

class VehicleCmdSet(CmdSet):

    def at_cmdset_creation(self):
        self.add(CmdBoardVehicle())
        self.add(CmdDepartVehicle())
  
        
class CmdBoardVehicle(COMMAND_DEFAULT_CLASS):
    """
    entering the train

    Usage:
      board

    This will be available to players in the same location
    as the vehicle and allows them to embark.
    """

    key = "board"
    locks = "cmd:not cmdinside()"

    def func(self):
        train = self.obj
        self.caller.msg("You board the train.")
        self.caller.move_to(train)


class CmdDepartVehicle(COMMAND_DEFAULT_CLASS):
    """
    leaving the train

    Usage:
      depart

    This will be available to everyone inside the
    vehicle. It allows them to exit to the vehicle's
    current location.
    """

    key = "depart"
    locks = "cmd:cmdinside()"

    def func(self):
        train = self.obj
        parent = train.location
        if parent:
            self.caller.move_to(parent)
        else:
            caller.msg("You must wait until you reach your destination.")