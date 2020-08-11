def gcd(a,b):
    if a == 0:
        return b
    elif a < b:
        return gcd(b,a)
    else:
        return gcd(a-b,b)

def gcd1(a,b):
    if b == 0:
        return a
    else:
        return gcd1(b,a%b)


if __name__ == '__main__':
    print('4,2:',gcd(4,2),gcd1(4,2))
    print('15,3:',gcd(15,3),gcd1(15,3))
    print('5,5:',gcd(5,5),gcd1(5,5))
    print('55,11:',gcd(55,11),gcd1(55,11))
