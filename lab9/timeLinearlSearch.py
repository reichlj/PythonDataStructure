# timeLinearSearch.py
"""Times the iterative sequential search repeatedly"""

from time import clock
from linearSearch import linearSearch

testSize = 10000                       # Number of items to search consisting of
evenList = list(range(0, 2*testSize, 2))     # even numbers from 0 to 2*(testSize-1)


start = clock()
for target in range(2*testSize):
    linearSearch(target, evenList)
# end for
end = clock()
runTime = end - start
print( "Time to run Iterative linearSearch to locate targets 0 to %d is %.4f sec." % \
      (2*testSize - 1, runTime))




