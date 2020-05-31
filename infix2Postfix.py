from stack import Stack

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for k, token in enumerate(tokenList):
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
                  print('***',infixexpr, ':',k, token, 'out'," ".join(postfixList))
            opStack.push(token)
        print(opStack)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

#assert infixToPostfix("A + B * C ") == 'A B C * +'
assert infixToPostfix("A * B + C * D") == 'A B * C D * +'
#assert infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )") == 'A B + C * D E - F G + * -'
#assert infixToPostfix("A + B + C + D") == 'A B + C + D +'
#assert infixToPostfix("A + B + C * D") == 'A B + C D * +'
#assert infixToPostfix("A * B / C") == 'A B * C /'
