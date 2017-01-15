import initialization

class Unit(object):
    """A unit of measurement for a substance or supplement. e.g. capsule,
    tablet, drop, or milligram, etc."""

    # In the future we will need to track relationships between different units.
    # e.g. a 'gram' consists of 1000 'milligrams'.

    def __init__(self, singular, plural=None, abbrev=None):
        self.singular = singular
        if plural:
            self.plural = plural
        # If plural is not specified, just tack an 's' on to the singular.
        else:
            self.plural = singular + 's'
        if abbrev:
            self.abbrev = abbrev
        else:
            self.abbrev = self.plural

    def __str__(self):
        return self.abbrev

    def __repr__(self):
        return self.abbrev

class Amount(object):
    """An amount consists of a numeric qty and a unit.

    This could be used to represent a dose (e.g. 2 tablets),
    or a quantity of a substance in a dose (e.g. a pill contains 50 mg)"""
    def __init__(self, qty, unit):
        self.qty = float(qty)

        assert unit.__class__.__name__ == 'Unit', 'Specified Unit is invalid.'
        self.unit = unit

    def __str__(self):
        return str(self.qty) + ' ' + self.unit.abbrev

    def __repr__(self):
        return str(self.qty) + ' ' + self.unit.abbrev

class Substance(object):
    """A specific substance. e.g. Vitamin D, or Biotin."""

    def __init__(self)

class Supplement(object):
    """A specific supplement product. e.g. """

    # To start, this will be generic. We'll track a single object for 'Vitamin
    # D'. However, ultimately, we'll want to track different brands, etc.

    def __init__(self, name, brand, units, amt_per_unit=None):
        self.name = name
        self.brand = brand
        assert units.__class__.name__ == 'Unit', units + ' is not a Unit object.'
        self.units = units
        self.description = ''

        if amt_per_unit:
            assert amt_per_unit.__class__.__name__ == 'Amount', """amt_per_unit
            is not valid."""
            self.amt_per_unit = amt_per_unit
        else:
            self.amt_per_unit = None

    def __str__(self):
        return self.name + ' ' + str(self.amt_per_unit)
