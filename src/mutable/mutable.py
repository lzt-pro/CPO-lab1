
class Node(object):

    def __init__(self, data=None, next=None):
        self.key = None
        self.data = data
        self.next = next

    def __repr__(self):
        if self.key != None:
            return "<Node key: %s data: %s>" % (self.key, self.data)
        else:
            return "<Node key: %s data: %s>" % (self.key, self.data)

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.current = None

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

    def to_list(self):
        list = []
        cur = self.head
        if cur is not None and cur.data != 'head':
            list.append([None, 'head'])
        while cur is not None:
            list.append([cur.key, cur.data])

            cur = cur.next
        return list

    def from_list(self, lst):
        if len(lst) == 0:
            self.head = None
            return
        root = Node('head', None)
        cur = root
        for d in lst:
            node = Node(d[1], None)
            node.key = d[0]
            cur.next = node
            cur = cur.next
        self.head = root

    def _last_node(self):
        assert self.head is not None
        self.current = self.head
        while self.current is not None:
            self.current = self.current.next
        return self.current

    def map(self, f):
        self.current = self.head
        while self.current is not None:
            self.current.data = f(self.current.data)
            self.current = self.current.next

    def reduce(self, f, initial_state):
        state = initial_state
        cur = self.head
        while cur is not None:
            if cur.data is 'head':
                cur = cur.next
            else:
                state = f(state, cur.data)
                cur = cur.next

        return state

    def add_to_tail(self, node):
        self.current = self.head
        if self.head is None:
            self.head = node
            return self.head
        else:
            while self.current.next != None:
                self.current = self.current.next
            self.current.next = node
        return self.current

    def add_to_head(self, node):
        self.current = self.head
        if self.head is None:
            self.head = node
            return self.head
        else:
            self.head = node
            self.head.next = self.current
        return self.head

    def __len__(self):
        return self.size()

    def __str__(self):
        return '<LinkedList: %d nodes>' % self.size()

    def __repr__(self):
        nodes = []
        node = self.head
        while not node is None:
            nodes.append(repr(node))
            node = node.next
        return 'LinkedList: Nodes: %r' % nodes

    def remove(self, value):
        previous = None
        self.current = self.head
        if self.current is None:
            return 'Linked List is empty, value of: %d is not here' % value
        else:
            while self.current != None:
                if self.current.data == value:
                    if len(self) is 1:
                        previous = None
                        self.current = None
                        self.head = None
                    else:
                        previous.next = self.current.next
                        self.current = None
                    return 'Node with the value: %d was removed from the LinkedList' % value
                else:
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

# A Hashmap that uses LinkedLists to handle collisions (chaining)
class Hashmap(object):

    def __init__(self, length=5):
        listBuckets = []
        for i in range(length):
            head = Node(None, None)
            head.key = i
            listBuckets.append(LinkedList(head))
        self.buckets = listBuckets
        self.length = length

    def to_list(self):
        list = []
        for i in range(self.length):
            linked = self.buckets[i]
            res = linked.to_list()
            del res[0]
            list.append(res)
        return list

    def from_list(self, list):

        for lst in list:
            linked = LinkedList()
            linked.from_list(lst)
            key = lst[0][0]
            self.buckets[key] = linked

    def hashFunction(self, data):
        key = data % self.length
        return key

    def insert(self, node):
        key = self.hashFunction(node.data)
        node.key = key
        pushOutput = self.buckets[key].add_to_tail(node)
        return pushOutput

    def remove(self, data):
        key = self.hashFunction(data)
        removedOutput = self.buckets[key].remove(data)
        return removedOutput

    def __repr__(self):
        return '<Hashmap %r>' % self.buckets
