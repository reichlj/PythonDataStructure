from lab2.advanced_die import AdvancedDie

die10_1 = AdvancedDie(10)
die10_2 = AdvancedDie(10)
count = 0
n = 100000
for k in range(n):
    count = count + die10_1.getRoll() + die10_2.getRoll()
    die10_1.roll()
    die10_2.roll()
print('Avg=',count/n)
