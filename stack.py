class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        result = "Stack - Size=" + str(self.size())
        for i in range(self.size()-1,-1,-1):
            result += '\n  '+ str(self.items[i]) + '  Type: ' + str(type(self.items[i]))
        return result


if __name__ == '__main__':
    st = Stack()
    st.push(3)
    print(st)