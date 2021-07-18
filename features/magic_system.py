"""
Magic handler module.

The `MagicHandler` provides an interface to manipulate a Characters's Magic
whilst respecting the various hooks and calls required. The handler is
instantiated as a property on the Character typeclass. It looks for the 
Magic properties on the Character to initialize itself and provide persistence.

Config Requirements:
    obj.db.magic (dict): List and number of magic held by the Character.

Setup:
    To use the MagicHandler, add it to a Character typeclass as follows:

    from typeclass.hander_magic import MagicHandler
      ...
    @property
    def magic(self):
        return MagicHandler(self)

Example usage:
    > self.magic.list
    [<magic>, <magic>]
"""

import time
from trainers.handler_party import PartyHandler
from defaults.characters import Character
from evennia.utils.evmenu import EvMenu
from evennia.utils import lazy_property, utils, dbserialize

# MAGIC LIST -----------------------------------------------------------------

magic_list = {
    "Fire" : "Fire",
    "Fira" : "Fira",
    "Firaga" : "Firaga",
    "Blizzard" : "Blizzard",
    "Blizzara" : "Blizzara",
    "Blizzaga" : "Blizzaga",
    "Thunder" : "Thunder",
    "Thundara" : "Thundara",
    "Thundaga" : "Thundaga",
    "Water" : "Water",
    "Aero" : "Aero",
    "Bio" : "Bio",
    "Demi" : "Demi",
    "Quake" : "Quake",
    "Tornado" : "Tornado",
    "Holy" : "Holy",
    "Flare" : "Flare",
    "Meteor" : "Meteor",
    "Ultima" : "Ultima",
    "Cure" : "Cure",
    "Cura" : "Cura",
    "Curaga" : "Curaga",
    "Life" : "Life",
    "Full-life" : "Full-life",
    "Regen" : "Regen",
    "Esuna" : "Esuna",
    "Scan" : "Scan",
    "Sleep" : "Sleep",
    "Blind" : "Blind",
    "Silence" : "Silence",
    "Confuse" : "Confuse",
    "Berserk" : "Berserk",
    "Break" : "Break",
    "Zombie" : "Zombie",
    "Death" : "Death",
    "Double" : "Double",
    "Triple" : "Triple",
    "Dispel" : "Dispel",
    "Protect" : "Protect",
    "Shell" : "Shell",
    "Reflect" : "Reflect",
    "Float" : "Float",
    "Drain" : "Drain",
    "Haste" : "Haste",
    "Slow" : "Slow",
    "Stop" : "Stop",
    "Meltdown" : "Meltdown",
    "Pain" : "Pain",
    "Aura" : "Aura",
    "Apocalypse" : "Apocalypse"
}

# MAGIC CHARACTER MIXIN ------------------------------------------------------

class MagicCharacterMixin():
    """
    This is a mixin that provides Magic functionality for Characters.

    """

    @lazy_property
    def magic(self):
        """Handler for Pokemon Party."""
        return MagicHandler(self)

    def at_object_creation(self):
        """
        Called only once, when object is first created
        """
        super().at_object_creation()

        # Values for the PartyHandler
        self.db.magic = {} # {"Fire" : 100, "Blizzard" : 100}

# MAGIC HANDLER --------------------------------------------------------------

class MagicException(Exception):
    """
    Base exception class for MagicHandler.

        Args:
            msg (str): informative error message
    """
    def __init__(self, msg):
        self.msg = msg


class MagicHandler(object):
    """Handler for a Character's Magic.

    Args:
        obj (Character): The Parent Character object.

    Properties
        magic (dict): List and number of magic held by the Character.

    Methods:
        list (list): list of magic with at least 1 
        add (str): add x magic to given spell, or creates spell if didn't exist.
        remove (str): remove x magic from given spell, or spell itself if at 0.
        amount (int): Return amount of Magic left for given spell.
    """

    def __init__(self, obj):
        """
        Save reference to the parent typeclass and check appropriate attributes

        Args:
            obj (typeclass): Pokemon typeclass.
        """
        self.obj = obj

        if not self.obj.attributes.has("magic"):
            msg = '`MagicHandler` requires `db.magic` attribute on `{}`.'
            raise MagicException(msg.format(obj))

    @property
    def list(self):
        """
        Returns list of Magic kmown to the Character.

        Returns:
            magic (list): List of current Magic known to Character.

        Returned if:
            obj.magic.list
        """
        return self.obj.db.magic.keys()

    # def __str__(self):
    #     """
    #     Returns current party.

    #     Returns:
    #         party (list): List of current Pokemon objects in party.

    #     Returned if:
    #         str(obj.party)
    #     """
    #     return ', '.join(pokemon.key for pokemon in self.obj.db.party)

    # def __iter__(self):
    #     """
    #     Iterates through party.

    #     Returns:
    #         pokemon (<Pokemon>): Values of party iterated through.

    #     Returned if:
    #         for pokemon in obj.party
    #     """
    #     return self.obj.db.party.__iter__()

    def __len__(self):
        """
        Returns number of Magic known to Character.

        Returns:
            length (int): Number of Magic known to Character.

        Returned if:
            len(obj.magic)
        """
        return len(self.obj.db.magic)

    def __nonzero__(self):
        """
        Support Boolean comparison for Magic held by Character.

        Returns:
            Boolean: True if holds Magic, False if no Magic.

        Returned if:
            if obj.magic
        """
        return bool(self.obj.db.magic)

    def amount(self, magic):
        """
        Returns the number of selected <magic> held by the Character.

        Returned if:
            obj.magic.amount("Fire")
        """
        try:
            return self.obj.db.magic[magic]
        except:
            return 0
        
    def add(self, magic, number):
        """
        Increase selected <magic> by <number> respecting limit of 100.

        Returned if:
            obj.magic.add("Fire", 10)
        """
        try:
            self.obj.db.magic[magic] = self.obj.db.magic[magic] + number
        except:
            msg = "Arguments passed to `MagicHandler.add()` caused an error."
            raise MagicException(msg)
        
        if self.obj.db.magic[magic] > 100:
            self.obj.db.magic[magic] = 100
        return

    def remove(self, magic, number = 1):
        """
        Reduce selected <magic> by <number>, removing <magic> if 0.

        Returned if:
            obj.magic.remove("Fire", 10)
        """
        try:
            self.obj.db.magic[magic] = self.obj.db.magic[magic] - number
        except:
            msg = "Arguments passed to `MagicHandler.remove()` caused an error."
            raise MagicException(msg)
        
        if self.obj.db.magic[magic] < 1:
            self.obj.db.magic.remove(magic)
        return True

    # def __sub__(self, pokemon):
    #     """
    #     Remove Pokemon from party. If party would equal zero it fails.

    #     Returns:
    #         True (Boolean): Pokemon was removed from party successfully.
    #         False (Boolean): Pokemon could not be removed.

    #     Returned if:
    #         obj.party - <Pokemone>
    #     """
    #     if len(self.obj.db.party) > 1:
    #         self.obj.db.party.remove(pokemon)
    #         return True
    #     else:
    #         return False

    # def swap(self, pokemon1, pokemon2):
    #     """
    #     Swap Pokemon positions within party.

    #     Returns:

    #     Returned if:
    #         obj.party.swap(<Pokemon>, <Pokemon>)
    #     """
    #     party = self.list
    #     pokemon1, pokemon2 = party.index(pokemon1), party.index(pokemon2)
    #     party[pokemon2], party[pokemon1] = party[pokemon1], party[pokemon2]

    # def __eq__(self, value):
    #     """
    #     Support equality comparison for party length.

    #     Returns:
    #         Boolean: True if equal, False if not.

    #     Returned if:
    #         obj.party == 5
    #     """
    #     if isinstance(value, int):
    #         return len(self.obj.db.party) == value
    #     else:
    #         return NotImplemented

    # def __ne__(self, value):
    #     """
    #     Support non-equality comparison for party length.

    #     Returns:
    #         Boolean: True if not equal, False if equal.

    #     Returned if:
    #         obj.party != 5
    #     """
    #     if isinstance(value, int):
    #         return len(self.obj.db.party) != value
    #     else:
    #         return NotImplemented

    # def __lt__(self, value):
    #     """
    #     Support less than comparison for party length.

    #     Returns:
    #         Boolean: True if less than, False if not.

    #     Returned if:
    #         obj.heatlh < 5
    #     """
    #     if isinstance(value, int):
    #         return len(self.obj.db.party) < value
    #     else:
    #         return NotImplemented

    # def __le__(self, value):
    #     """
    #     Support less than or equal to comparison for party length.

    #     Returns:
    #         Boolean: True if less than or equal, False if not.

    #     Returned if:
    #         obj.party <= 5
    #     """
    #     if isinstance(value, int):
    #         return len(self.obj.db.party) <= value
    #     else:
    #         return NotImplemented

    # def __gt__(self, value):
    #     """
    #     Support greater than comparison for party length.

    #     Returns:
    #         Boolean: True if greater than, False if not.

    #     Returned if:
    #         obj.party > 5
    #     """
    #     if isinstance(value, int):
    #         return len(self.obj.db.party) > value
    #     else:
    #         return NotImplemented

    # def __ge__(self, value):
    #     """
    #     Support greater than or equal to comparison for party length.

    #     Returns:
    #         Boolean: True if greater than or equal, False if not.

    #     Returned if:
    #         obj.party >= 5
    #     """
    #     if isinstance(value, int):
    #         return len(self.obj.db.party) >= value
    #     else:
    #         return NotImplemented
