"""
Health handler module.

The `HealthHandler` provides an interface to manipulate a Pokemon's health
whilst respecting the various hooks and calls required. The handler is
instantiated as a property on a pokemon typeclass, with the pokemon passed
as an argument. It looks for the health properties in the character's db
attributes handler to initialize itself and provide persistence. The Pokemon's
max health is calculated when required rather than stored.

Config Properties:
    current (int): Current health of the Pokemon.

Config Requirements:
    obj.db.health (int): Current health of the Pokemon.

Setup:
    To use the HealthHandler, add it to a pokemon typeclass as follows:

    from typeclass.hander_health import HealthHandler
      ...
    @property
    def heatlh(self):
        return HealthHandler(self)

Use:
    Health is added and subtracted using the `heal` and `dmg` methods or
    regular arithmetic operators.

Example usage:
    # Say self is a Pokemon.
    > @py self.msg(str(self.health.current))
    5
    > @py self.msg(self.health.max)
    10
    > @py self.msg(self.health.percentage)
    50%
    > @py self.msg(self.health.dmg(2))
    3
    > @py self.msg(self.health.heal(4))
    7
    > @py self.msg(self.health-5)
    2
    > @py self.msg(self.health+5)
    7
    > @py self.msg(self.health.full())
    10
"""
# from world.rules import calculate_health

class HealthException(Exception):
    """
    Base exception class for HealthHandler.

        Args:
            msg (str): informative error message
    """
    def __init__(self, msg):
        self.msg = msg


class HealthHandler(object):
    """Handler for a characters health.

    Args:
        obj (Character): parent Pokemon object.

    Properties
        health (integer): returns current health
        condition (list): returns a list of conditions

    Methods:

        add (str): add a condition to the character's condition list.
        remove (str): remove a condition to the character's condition list.
    """

    def __init__(self, obj):
        """
        Save reference to the parent typeclass and check appropriate attributes

        Args:
            obj (typeclass): Pokemon typeclass.
        """
        self.obj = obj

        if not self.obj.attributes.has("health"):
            msg = '`HealthHandler` requires `db.health` attribute on `{}`.'
            raise HealthException(msg.format(obj))

    @property
    def current(self):
        """
        Shows current health.

        Returns:
            current_health (str): Characters current health.

        Returned if:
            obj.heatlh.current
        """
        return int(self.obj.db.health)

    def __str__(self):
        """
        Shows current health.

        Returns:
            current_health (str): Characters current health.

        Returned if:
            str(obj.health)
        """
        return str(self.obj.db.health)

    @property
    def percentage(self):
        """
        Shows current health formatted as a percentage.

        Returns:
            Health (str): Characters current health as percentage of max.

        Returned if:
            obj.heatlh.percent
        """
        return "{}%".format(int(self.current * 100.0 / self.max))

    @property
    def max(self):
        """
        Calculate Pokemon's max health.

        Returns:
            max_health (int): Max health determined by rules.

        Returned if:
            obj.heatlh.max
        """
        # return int(calculate_health(self.obj.pokedex("stat")[0],
        #                             self.obj.db.iv[0], self.obj.db.ev[0],
        #                             self.obj.db.level))
        return 10

    def full(self):
        """
        Resets health to maximum.

        Returns:
            health (int): Current health after fill.

        Returned if:
            obj.heatlh.full()
        """
        self.obj.db.health = self.max
        return self.obj.db.health

    def heal(self, value):
        """
        Support addition between between health and int, capping at max health.

        Returns:
            health (int): Current health after addition.

        Returned if:
            obj.heatlh.heal(5)
        """
        if isinstance(value, int):
            if (self.obj.db.health + value) > self.max:
                self.obj.db.health = self.max
                return self.obj.db.health
            else:
                self.obj.db.health += value
                return self.obj.db.health
        else:
            return NotImplemented

    def __add__(self, value):
        """
        Support addition between between health and int, capping at max health.

        Returns:
            health (int): Current health after addition.

        Returned if:
            obj.heatlh+= 5
        """
        if isinstance(value, int):
            if (self.obj.db.health + value) > self.max:
                self.obj.db.health = self.max
                return self.obj.db.health
            else:
                self.obj.db.health += value
                return self.obj.db.health
        else:
            return NotImplemented

    def dmg(self, value):
        """
        Support subtraction between health and int, capping at 0

        Returns:
            health (int): Current health after subtraction.

        Returned if:
            obj.heatlh.dmg(5)
        """
        if isinstance(value, int):
            if (self.obj.db.health - value) < 0:
                self.obj.db.health = 0
                # TODO Faint hook
                return self.obj.db.health
            else:
                self.obj.db.health -= value
                return self.obj.db.health
        else:
            return NotImplemented

    def __sub__(self, value):
        """
        Support subtraction between health and int, capping at 0

        Returns:
            health (int): Current health after subtraction.

        Returned if:
            obj.heatlh-5
        """
        if isinstance(value, int):
            if (self.obj.db.health - value) < 0:
                self.obj.db.health = 0
                # TODO Faint hook
                return self.obj.db.health
            else:
                self.obj.db.health -= value
                return self.obj.db.health
        else:
            return NotImplemented

    def __mul__(self, value):
        """
        Support multiplication between health and int.

        Returns:
            health (int): Current health after multiplication.

        Returned if:
            obj.heatlh*= 5
        """
        if isinstance(value, int):
            if (self.obj.db.health * value) > self.max:
                self.obj.db.health = self.max
                return self.obj.db.health
            else:
                self.obj.db.health *= value
                return self.obj.db.health
        else:
            return NotImplemented

    def __floordiv__(self, value):
        """
        Support division between health and int.

        Returns:
            health (int): Current health after division.

        Returned if:
            obj.heatlh/= 5
        """
        if isinstance(value, int):
            return self.obj.db.health // value
        else:
            return NotImplemented

    def __bool__(self):
        """
        Support Boolean comparison of health.

        Returns:
            Boolean: True if not zero, False 0.

        Returned if:
            if obj.heatlh
        """
        return bool(self.obj.db.health)

    def __eq__(self, value):
        """
        Support equality comparison between health and int.

        Returns:
            Boolean: True if equal, False if not.

        Returned if:
            obj.heatlh == 5
        """
        if isinstance(value, int):
            return self.obj.db.health == value
        else:
            return NotImplemented

    def __ne__(self, value):
        """
        Support non-equality comparison between health and int.

        Returns:
            Boolean: True if not equal, False if equal.

        Returned if:
            obj.heatlh != 5
        """
        if isinstance(value, int):
            return self.obj.db.health != value
        else:
            return NotImplemented

    def __lt__(self, value):
        """
        Support less than comparison between health and int.

        Returns:
            Boolean: True if less than, False if not.

        Returned if:
            obj.heatlh < 5
        """
        if isinstance(value, int):
            return self.obj.db.health < value
        else:
            return NotImplemented

    def __le__(self, value):
        """
        Support less than or equal to comparison between health and int.

        Returns:
            Boolean: True if less than or equal, False if not.

        Returned if:
            obj.heatlh <= 5
        """
        if isinstance(value, int):
            return self.obj.db.health <= value
        else:
            return NotImplemented

    def __gt__(self, value):
        """
        Support greater than comparison between health and int.

        Returns:
            Boolean: True if greater than, False if not.

        Returned if:
            obj.heatlh > 5
        """
        if isinstance(value, int):
            return self.obj.db.health > value
        else:
            return NotImplemented

    def __ge__(self, value):
        """
        Support greater than or equal to comparison between health and int.

        Returns:
            Boolean: True if greater than or equal, False if not.

        Returned if:
            obj.heatlh >= 5
        """
        if isinstance(value, int):
            return self.obj.db.health >= value
        else:
            return NotImplemented
