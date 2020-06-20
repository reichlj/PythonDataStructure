from lab2.advanced_die import AdvancedDie

class MoreAdvancedDie(AdvancedDie):
    """A more Advanced die class that allows to set the value of a roll"""

    def __init__(self, sides = 6):
        # call Die parent class constructor
        super().__init__(sides)

    def setRoll(self,value):
        """Sets the die's value to a given value
           Precondition: value must be an in between 1 and number of sides
           Postcondition: current roll set to the given value"""
        if not isinstance(value,int):
            raise TypeError('value must be an integer')
        if value<0 or value> self._numSides:
            raise ValueError('value must be between 1 and {0}'.format(self._numSides))
        self._currentRoll = value

if __name__ == '__main__':
    mad = MoreAdvancedDie(10)
    mad.setRoll(7)
    print('7 expected ',mad.getRoll())
    try:
        mad.setRoll(12)
    except ValueError as e:
        print(e)
    try:
        mad.setRoll('ooto')
    except TypeError as e:
        print(e)

