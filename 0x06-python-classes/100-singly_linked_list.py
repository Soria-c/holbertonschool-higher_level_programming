#!/usr/bin/python3
"""In this module classes Node and SinglyLinkedList are defined"""


class Node:
    """Class to create a node object"""
    def __init__(self, data, next_node=None):
        """Initialization of a new Node"""
        if not(isinstance(data, int)):
            raise TypeError("data must be an integer")
        if (isinstance(next_node, Node)) or not next_node:
            self.__next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")
        self.__data = data

    @property
    def data(self):
        """Getter method for self.__data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method for self.__data"""
        if not(isinstance(value, int)):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter method for self.__next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method for self.__next_node"""
        if (isinstance(value, Node)) or not value:
            self.__next_node = value
            return
        raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Class to create a SinglyLinkedList object"""
    def __init__(self):
        """Initialization of a SinglyLinkedList object"""
        self.__head = None

    def sorted_insert(self, value):
        """Add node sorted instance method"""
        new = Node(value)
        new.data = value
        new.next_node = None
        if not(self.__head):
            self.__head = new
            return
        if (new.data < self.__head.data):
            new.next_node = self.__head
            self.__head = new
        else:
            if (new.next_node):
                self.__head.next_node = new
                return
            tmp = self.__head
            while(tmp.next_node and (new.data > tmp.next_node.data)):
                tmp = tmp.next_node
            if not(tmp.next_node):
                tmp.next_node = new
                return
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Custom implementation of the __str__ magic method"""
        r = []
        h = self.__head
        while (h):
            r.append(str(h.data))
            h = h.next_node
        return "\n".join(r)
