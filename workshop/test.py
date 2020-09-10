"""
Vehicles - TO BE TESTED

Automated Vehicles


"""

from evennia import utils, settings, CmdSet
from typeclasses.objects import Object

COMMAND_DEFAULT_CLASS = utils.class_from_module(settings.COMMAND_DEFAULT_CLASS)

# ------------------------------------------------------------------------------
# Vehicle Commands - Allows departing from vehicles.
# ------------------------------------------------------------------------------

class TestCmdSet(CmdSet):

    def at_cmdset_creation(self):
        self.add(CmdTest1())
        self.add(CmdTest2())
  
        
class CmdTest1(COMMAND_DEFAULT_CLASS):
    """
    entering the train

    Usage:
      board

    This will be available to players in the same location
    as the vehicle and allows them to embark.
    """

    key = "test"
    locks = "cmd:not cmdinside()"

    def func(self):
        self.caller.msg("You board the train.")


class CmdTest2(COMMAND_DEFAULT_CLASS):
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
        self.caller.msg("You must wait until you reach your destination.")
