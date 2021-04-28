class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __contains__(self, value):
        """
        allow use of in operator
        """
        return self.data == value

    def __mul__(self, number: int):
        """
        allow multiple Nodes to simultaneously be created/copies
        """
        n = []
        i = 0
        while i < number:
            n.append(Node(self.data, self.next))
            i += 1
        return n

    def __rmul__(self, number):
        """
        allow reverse order multiplication
        """
        return self * number  # call the normal multiplication

    def __eq__(self, item):
        """
        return True if data value is equivalent
        """
        if item.__class__ == Node:
            return self.data == item.data

    def __str__(self):
        return f"{self.data}, -> {self.next}"

    def __repr__(self):
        return str(self)


if __name__ == "__main__":
    m = Node(4)
    s = 5 * m
    print(m)
    print(type(s))
    print(s)
    f = 3 in m
    print(type(f))
