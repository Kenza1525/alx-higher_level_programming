#!/usr/bin/python3

""" A class Node that defines a singly linked list
And a class SinglyLinkedList that traverse and sort
a list """


class Node:
    """ Defines data and next_node attributes """

    def __init__(self, data, next_node=None):
        """ Initialize the instance attribute """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Retrieves data attribute """
        return self.__data

    @data.setter
    def data(self, value):
        """ Allows modification of data value """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ Retrieves next_node attribute """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Allows modification of next_node """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ Traverses and sorts a list, defines head attribute """

    def __init__(self):
        """ Initializes the head attribute """
        self.__head = None

    def __str__(self):
        """ Prints the list in string format """
        string = ""
        temp = self.__head

        while temp is not None:
            string += str(temp.data)
            temp = temp.next_node
            if temp is not None:
                string += "\n"
        return string

    def sorted_insert(self, value):
        """ Inserts a new Node into the correct sorted position in the list """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
            return
        if self.__head.data > new_node.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        temp = self.__head
        while temp.next_node is not None and temp.next_node.data < new_node.data:
            temp = temp.next_node
        new_node.next_node = temp.next_node
        temp.next_node = new_node
