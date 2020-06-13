import timeit

def recDC(coinValueList,change,knownResults):
    minCoins = change
    if change in coinValueList:
       knownResults[change] = 1
       return 1
    elif knownResults[change] > 0:
       return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
          numCoins = 1 + recDC(coinValueList, change-i, knownResults)
          if numCoins < minCoins:
             minCoins = numCoins
             knownResults[change] = minCoins
    return minCoins

def recDC1(coinValueList,change,knownResults):
    if knownResults[change] > 0:
       return knownResults[change]
    else:
        minCoins = change
        for i in [c for c in coinValueList if c <= change]:
          numCoins = 1 + recDC1(coinValueList, change-i, knownResults)
          if numCoins < minCoins:
             minCoins = numCoins
             knownResults[change] = minCoins
        return minCoins

print(recDC([1,5,10,25],63,[0]*64))
nr = [0]*64
nr[1]=1
nr[5]=1
nr[10]=1
nr[25]=1
print(recDC1([1,5,10,25],63,nr))

t1 = timeit.Timer("recDC([1,5,10,25],999,[0]*1000)", "from __main__ import recDC")
print('recDC ', t1.timeit(number=1), 'microseconds')
init = "from __main__ import recDC1; nr = [0]*1000; nr[1]=1; nr[5]=1; nr[10]=1; nr[25]=1"
t1 = timeit.Timer("recDC1([1,5,10,25],999,nr)", setup=init)
print('recDC1', t1.timeit(number=1), 'microseconds')
