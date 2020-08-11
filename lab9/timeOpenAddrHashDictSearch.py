# timeOpenAddrHashDictSearch.py
"""Times the searching of the OpenAddrHashDict that uses a hash table with
   linear probing"""

from time import clock
from open_addr_hash_dictionary import OpenAddrHashDict

testSize = 3000                   # Number of items to search consisting of

evenHashTable = OpenAddrHashDict(2**14, hash, True)   # Linear probing
#evenHashTable = OpenAddrHashDict(2**14, hash, False)  # Quadratic probing

for i in range(0, 2*testSize, 2):  # even numbers from 0 to 2*(testSize-1)
    evenHashTable[i] = i
print( "Done entering values in OpenAddrHashDict -- Beginning accesses")
start = clock()
for target in range(2*testSize):
    value = evenHashTable[target]
# end for
end = clock()
runTime = end - start
print ("Time to use a OpenAddrHashDict with linear probing of %d size to locate targets 0 to %d is %.6f sec." % \
      (2**14, 2*testSize-1, runTime))
##print ("Time to use a OpenAddrHashDict with quadratic probing of %d size to locate targets 0 to %d is %.6f sec." % \
##      (2**14, 2*testSize-1, runTime))




