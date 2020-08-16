""" File:  ordered_linked_list.py
    Description:  ordered List ADT implemented using singly-linked list.
"""

from lab5\
    .mynode import MyNode

class OrderedList(object):

    def __init__(self):
        """ Constructs an empty unsorted list.
            Precondition:  none
            Postcondition:  Reference to empty unsorted list returned.
        """
        self._head = None
        self._tail = None
        self._size = 0
        self._current = None
        self._previous = None
        self._currentIndex = 0

    def add(self, newItem):
        """ Adds the newItem to its sorted spot in the list.
            Precondition: newItem is not in the list.
            Postcondition:  newItem is added to the list.
        """
        if self.search(newItem):
            raise ValueError("Cannot not add since item is already in the list!")
               
        temp = MyNode(newItem)
        temp.setNext(self._current)
        if self._previous == None:
            self._head = temp
        else:
            self._previous.setNext(temp)
        if self._current == None:
            self._tail = temp
        self._size += 1


    def search(self, targetItem):
        """ Searches for the targetItem in the list.
            Precondition: none.
            Postcondition:  Returns True and makes it the current item if targetItem is in the list;
                            otherwise False is returned.
        """
        def searchHelper():
            """ Recursive helper function that moves down the linked list.
                It has no parameters, but uses self._current, self._previous, and
                self._currentIndex."""
            # ADD CODE HERE
            if self._current is None:
                return False
            elif self._current.getData() == targetItem:
                return True
            elif self._current.getData() > targetItem:
                return False
            else:
                self._currentIndex = self._currentIndex + 1
                self._previous = self._current
                self._current = self._current.getNext()
                return searchHelper()

        # START OF SEARCH - DO NOT MODIFY BELOW CODE
        if self._current != None and self._current.getData() == targetItem:
            return True
        
        self._previous = None
        self._current = self._head
        self._currentIndex = 0
        return searchHelper()

##    def search(self, targetItem):
##        """ Searches for the targetItem in the list.
##            Precondition: none.
##            Postcondition:  Returns True and makes it the current item if targetItem is in the list;
##                            otherwise False is returned.
##        """
##        if self._current != None and self._current.getData() == targetItem:
##            return True
##        
##        self._previous = None
##        self._current = self._head
##        self._currentIndex = 0
##        while self._current != None:
##            if self._current.getData() == targetItem:
##                return True
##            elif self._current.getData() > targetItem:
##                return False
##            else: #inch-worm down list
##                self._previous = self._current
##                self._current = self._current.getNext()
##                self._currentIndex += 1
##        return False

    def remove(self, item):
        """ Removes item from the list.
            Precondition:  item is in the list.
            Postcondition:  Item is removed from the list.
        """
        if not self.search(item):
            raise ValueError("Cannot remove item since it is not in the list!")

        if self._current == self._tail:
            self._tail = self._previous
            
        if self._current == self._head:
            self._head = self._head.getNext()
        else:
            self._previous.setNext(self._current.getNext())
        self._current = None
        self._size -= 1

    def isEmpty(self):
        """ Checks to see if the list is empty.
            Precondition:  none.
            Postcondition:  Returns True if the list is empty; otherwise returns False.
        """
        return self._size == 0

    def length(self):
        """ Returns the number of items in the list.
            Precondition:  none.
            Postcondition:  Returns the number of items in the list.
        """
        return self._size

    def index(self, item):
        """ Returns the position of item in the list.
            Precondition:  item is in the list.
            Postcondition:  Returns the position of item from the head of list.
        """
        if not self.search(item):
            raise ValueError("Cannot determine index since item is not in the list!")

        return self._currentIndex

    def pop(self, *pos):
        """ Removes and returns the item at position pos of the list.
            Precondition:  position pos exists in the list.
            Postcondition:  Removes and returns the item at position pos of the list.
        """
        if len(pos) == 0:
            pos = self._size - 1
        elif len(pos) != 1:
            raise TypeError("Too many parameters to pop")
        else:
            pos = pos[0]
        
        if not isinstance(pos, int):
            raise TypeError("Position must be an integer!")
        
        if pos >= self._size or pos < 0:
            raise IndexError("Cannot pop from index", pos, "-- invalid index!")

        self._current = self._head
        self._previous = None
        for count in range(pos):
            self._previous = self._current
            self._current = self._current.getNext()
            
        if self._current == self._tail:
            self._tail = self._previous
            
        if self._current == self._head:
            self._head = self._head.getNext()
        else:
            self._previous.setNext(self._current.getNext())
        returnValue = self._current.getData()
        self._current = None
        self._size -= 1
        return returnValue

    def __str__(self):
        """ Returns a string representation of the list with a space between each item.
            Precondition:  none
            Postcondition:  Returns a string representation of the list with a space between each item.
        """
        def strHelper(current):
            if current == None:
                return ""
            else:
                return str(current.getData()) + " " + strHelper(current.getNext())
        resultStr = "(head) " + strHelper(self._head) + "(tail)"
        return resultStr
    
##    def __str__(self):
##        """ Removes and returns the item at position pos of the list.
##            Precondition:  position pos exists in the list.
##            Postcondition:  Removes and returns the item at position pos of the list.
##        """
##        resultStr = "(head)"
##        current = self._head
##        while current != None:
##            resultStr += " " + str(current.getData())
##            current = current.getNext()
##        return resultStr + " (tail)"
    
    
if __name__ == '__main__':
    myList = OrderedList()
    assert myList.search('a') == False
    myList.add('3')
    myList.add('5')
    myList.add('7')
    assert myList.search('1') == False
    assert myList.search('3') == True
    assert myList.search('4') == False
    assert myList.search('5') == True
    assert myList.search('6') == False
    assert myList.search('7') == True
    assert myList.search('8') == False
    print("ALL SEARCH TESTS PASSED!!!")
    
        
        
        

        

    


        
        
                
                

        
    

    
        
    
