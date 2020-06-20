"""
File:  diceOutcomes.py
Description:  Rolls two dice 1,000 times to determine the outcome(s) with
the highest percentage.
"""
from random import randint

# Global Constants
NUMBER_OF_ROLLS = 10
DIE_SIDES = 6

def main():
    """ Main program provides an outline of program """
    displayWelcome()
    mostFrequentRolls, highestCount = calculateFrequentRolls()
    displayResults(mostFrequentRolls, highestCount)


def displayWelcome():
    """ Displays welcome message for the user """
    print("This programs rolls two {0}-sided dice {1} times to".format(DIE_SIDES,NUMBER_OF_ROLLS))
    print("determine the outcome(s) with the highest percentage.")
    print()


def calculateFrequentRolls():
    """Rolls the dice the correct number of times, tallies the outcomes, and
       returns a list of outcomes with highest counts and highest count."""

    # initialize outcomeCounts to all 0s.  The index corresponds to the outcome
    # NOTE:  index positions 0 and 1 are not possible
    outcomeCounts = dict()
    for count in range(DIE_SIDES*2+1):
        outcomeCounts[count] = 0

    rollAndTallyOutcomes(outcomeCounts)

    print("outcomeCounts:",outcomeCounts)    # For debugging

    highestCount = max(outcomeCounts.values())

    mostFrequentRolls = findOutcomes(outcomeCounts, highestCount)

    print("mostFrequentRolls:", mostFrequentRolls,
          "and highestCount:",highestCount)    # For debugging

    return mostFrequentRolls, highestCount


def rollAndTallyOutcomes(outcomeCounts):
    """Rolls the dice the correct number of times and tallies the outcomes 
       in the outcomeCounts list of tallies with the index being the outcome."""
##    ADD CODE HERE
    for k in range(NUMBER_OF_ROLLS):
        t = randint(1,6) + randint(1,6)
        outcomeCounts[t] = outcomeCounts[t] +1


def findOutcomes(outcomeCounts, highestCount):
    """Returns a list of outcomes with the highest count."""
    highestOutcomesList = []
##  ADD CODE HERE
    for index in outcomeCounts:
        if outcomeCounts[index] == highestCount:
            highestOutcomesList.append(index)

    return highestOutcomesList


def displayResults(mostFrequentRolls, highestCount):
    """ Displays the outcome(s) with the highest percentage"""
    print("The highest percentage is %3.1f for outcome(s): "
          % (highestCount*100/NUMBER_OF_ROLLS), end="")
    for index in range(len(mostFrequentRolls)):
        print(mostFrequentRolls[index], end=" ")
    print()
    
main()
    
        
    
    


