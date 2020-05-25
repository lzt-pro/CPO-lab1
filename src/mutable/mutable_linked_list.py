from mutable_node import Node


# A Linked List of Node Objects
class LinkedList(object):

    # head = pointer to the first Node in the Linked List
    # current = pointer to current Node in list, used when Traversing Linked List
    def __init__(self,head = None):
        self.head = head
        self.current = None

    # Returns amount of Node objects in the Linked List
    def size(self):
        length = 1
        if self.head is None:
            return length
        else:
            length = 1
            self.current = self.head
            while self.current.next != None:
                self.current = self.current.next
                length = length + 1
            return length
    # To_list traverses the linked list, storing the node in the list of res
    def to_list(self):
        # 将链表转换为两个list，一个为key,一个为
        list = []
        cur = self.head
        if cur is not None and cur.data != 'head':
            list.append([None,'head'])
        while cur is not None:
            list.append([cur.key,cur.data])

            cur = cur.next
        return list
    # From_list converts a list to a chain phenotype
    def from_list(self,lst):
        # 后插法，返回的head节点为（None,None,node1)
        if len(lst)==0:
            self.head=None
            return
        root = Node('head',None)
        cur = root
        for d in lst:
            node = Node(d[1],None)
            node.key = d[0]
            cur.next = node
            cur = cur.next
        self.head = root
    # Find the last node in the list
    def _last_node(self):
        assert self.head is not None
        self.current = self.head
        while self.current is not None:
            self.current = self.current.next
        return self.current
    # The map mapping function transforms the data value of each node into f
    def map(self,f):
        self.current = self.head
        while self.current is not None:
            self.current.data = f(self.current.data)
            self.current = self.current.next

    # Reduce function, the value of all nodes in the linked list is executed according to f operation
    def reduce(self,f,initial_state):
        state = initial_state
        cur = self.head
        while cur is not None:
            if cur.data is 'head':
                cur = cur.next
            else:
                state = f(state, cur.data)
                cur = cur.next

        return state
    # Adds a Node to the end of a Linked List
    # Returns the Node that was added
    def add_to_tail(self, node):
        self.current = self.head
        # Add to front of List if it is Empty
        if self.head is None:
            self.head = node
            return self.head
        else:
            # Iterate through Nodes until reached the end
            while self.current.next != None:
                self.current = self.current.next
            self.current.next = node
        return self.current
    # Adds a Node to the fisrt of a Linked List
    # Returns the Node that was added
    def add_to_head(self, node):
        self.current = self.head
        # Add to front of List if it is Empty
        if self.head is None:
            self.head = node
            return self.head
        else:
            self.head = node
            self.head.next = self.current
        return self.head

    # Returns the length of a Linked List Object
    def __len__(self):
        return self.size()

    # Returns informal String representation of a Linked List
    def __str__(self):
        return '<LinkedList: %d nodes>' % self.size()

    # Returns formal String represention of Linked List and its Nodes
    def __repr__(self):
        nodes = []
        node = self.head
        while not node is None:
            nodes.append(repr(node))
            node = node.next
        return 'LinkedList: Nodes: %r' % nodes



    # Removes a Node from the Linked List with the given value
    # value = Data of the Node object you would like to remove from the Linked List
    def remove(self, value):
        previous = None
        self.current = self.head
        # Attempted to Remove from Empty Linked List
        if self.current is None:
            return 'Linked List is empty, value of: %d is not here' % value
        else:
             while self.current != None:
                if self.current.data == value:
                    # Remove the value from the Linked List
                    if len(self) is 1:
                        previous = None
                        self.current = None
                        self.head = None
                    else:
                        previous.next = self.current.next
                        self.current = None
                    return 'Node with the value: %d was removed from the LinkedList' % value
                else:
                    # Specified Value was not in the Linked List
                    previous = self.current
                    self.current = self.current.next
        return 'Node is not in LinkedList'

    def __iter__(self):
        return LinkedList(self.head)

    def __next__(self):
        if self.head is None:
            raise StopIteration
        tmp = self.head.data
        self.head = self.head.next
        return tmp
