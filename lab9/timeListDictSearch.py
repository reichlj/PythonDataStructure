# timeListDictSearch.py
"""Times the searching of the ListDict that uses a Python
list to hold entries"""

from time import clock
from list_dictionary import ListDict

print( "WARNING:  This timing takes a while...")
testSize = 10000                   # Number of items to search consisting of
evens = ListDict()
for i in range(0, 2*testSize, 2):  # even numbers from 0 to 2*(testSize-1)
    evens[i] = i
print( "Done entering values in ListDict -- Begining accesses")
start = clock()
for target in range(2*testSize):
    value = evens[target]
# end for
end = clock()
runTime = end - start
print( "Time to use a ListDict (Python list holds entries) of %d size to locate targets 0 to %d is %.6f sec." % \
      (testSize, 2*testSize - 1, runTime))




