from node import Node


class Linked:
    def __init__(self, data=None):
        if not data:
            self._head = None
        else:
            self._head = Node(data)
        self._tail = self._head

    def setHead(self, node: Node):
        if node.__class__ == Node:
            self._head = node

    def getHead(self):
        return self._head

    def getTail(self):
        return self._tail

    def setTail(self, node: Node):
        if node.__class__ == Node:
            self._tail = node

    def isEmpty(self):
        return not self._head

    def append(self, data):
        """
        @param data value to set to new tail node
        append a new node with the passed value as data
        """
        if self.isEmpty():
            self._head = Node(data)
            self._tail = self._tail
        elif self._head is self._tail:
            self._tail = Node(data)
            self._head.next = self._tail
        else:
            pre_tail = self._tail
            self._tail = Node(data)
            pre_tail.next = self._tail

    def prepend(self, data):
        if self.isEmpty():
            self._head = Node(data)
            self._tail = self._tail
        elif self._head is self._tail:
            self._head = Node(data)
            self._head.next = self._tail
        else:
            pre_head = self._head
            self._head = Node(data)
            self._head.next = pre_head

    def pointerTo(self, rank: int):
        """
        returns a pointer to the node at the rank chosen
        """
        if not self.isEmpty() and rank >= 0:
            if rank == 0:
                return self._head
            else:
                loc = self._head
                try:
                    for i in range(0, rank):
                        loc = loc.next  # move to next location
                        if not loc:  # None type reached
                            raise IndexError
                except IndexError as ie:
                    print("Index error, rank higher than possible")
                finally:
                    return loc
        else:
            print("invalid rank")

    def removeBack(self):
        """
        remove tail and return it
        """
        if self.isEmpty():
            print("Underflow error")
            return
        elif self._tail is self._head:
            item = self._head
            self._tail = None
            self._head = self._tail
            return item
        elif self._head.next is self._tail:
            item = self._tail
            self._head.next = None
            self._head = self._tail
            return item
        else:
            item = self._tail
            loc = self._head
            while loc.next:
                # increment until last before tail
                self._tail = loc
                loc = loc.next
            return item

    def removeFront(self):
        """
        remove head and return it
        """
        if self.isEmpty():
            print("Underflow error")
            return
        elif self._head is self._tail:
            item = self._head
            self._tail = None
            self._head = self._tail
            return item
        else:
            item = self._head
            self._head = self._head.next
            return item

    def insertAfter(self, data, after_this: Node):
        """
        insert a new node containing 'data' after Node and return pointer to inserted node
        """
        if after_this is self._tail:
            self.append(data)
        else:
            insert_this = Node(data)
            prev_after = after_this.next
            after_this.next = insert_this
            insert_this.next = prev_after
            return insert_this

    def insertBefore(self, data, before_this: Node):
        if before_this is self._head:
            self.prepend(data)
        else:
            previous = self._head
            while previous.next is not before_this:
                previous = previous.next
                if not previous:
                    print("Node not in this list")
                    return
            return self.insertAfter(data, previous)

    def __str__(self):
        """
        return a string format of the data contained in the list
        """
        message = ""
        if self.isEmpty():
            print("Underflow: nothing in list")
        else:
            loc = self._head
            while loc.next:
                message = message + str(loc.data) + " -> "
                loc = loc.next
            message += str(self._tail.data)
            return message

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        """
        shortcut append
        """
        return self.append(other)

    def __radd__(self, other):
        """
        shortcut prepend
        """
        return self.prepend(other)


if __name__ == "__main__":
    attempt = Linked(6)
    print(attempt.getHead())
    print(attempt.getTail())
    attempt.prepend(5)
    print(attempt.getHead())
    print(attempt.getTail())
    attempt.append(7)
    print(attempt.getHead())
    print(attempt.getTail())
    t = attempt.pointerTo(2)
    print(t)
    attempt.insertBefore(6.5, t)
    t = attempt.pointerTo(2)
    print(attempt)
    attempt.insertAfter(6.75, t)
    print(attempt)
    attempt += "last"
    print(attempt)
    attempt = "first" + attempt
    print(attempt)
