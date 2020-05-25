from mutable_linked_list import LinkedList
from mutable_node import Node

# A Hashmap that uses LinkedLists to handle collisions (chaining)
class Hashmap(object):

    # Creates a Hashmap that contains a List of LinkedList objects with given length and stores length
    # buckets = list of Linked List Objects
    # length = length of the bucket list
    def __init__(self, length=5):
        listBuckets = []
        for i in range(length):
            head = Node(None,None)
            head.key = i
            listBuckets.append(LinkedList(head))
        self.buckets = listBuckets
        self.length = length
    def to_list(self):
        list = []
        for i in range(self.length):
            linked = self.buckets[i]
            # if isinstance(linked, LinkedList):
            #     linked = linked.head
            res = linked.to_list()
            del res[0]
            list.append(res)
        return list
    def from_list(self,list):

        # for i in range(self.length):
        #     head = Node(None,None)
        #     head.key = i
        #     listBucket.append(LinkedList(head))
        for lst in list:
            linked = LinkedList()
            linked.from_list(lst)
            key = lst[0][0]
            self.buckets[key] = linked

            # for j in len(key):
            #     node = Node(data[j], None)
            #     cur = listBucket[key[j]]
            #     while cur.next is None:
            #         cur.next = node

    # Calculates the key to find a location in the Hashmap for a Node
    # data = the data of the Node given for insertion or removal
    # Returns: key = location of LinkedList to insert or remove a Node
    def hashFunction(self, data):
        key = data % self.length
        return key

    # Places a Node in a Hashmap based off the key
    # Gets the key to find out where to place the Node
    # Then adds Node to that LinkedList
    def insert(self, node):
        key = self.hashFunction(node.data)
        node.key = key
        pushOutput = self.buckets[key].add_to_tail(node)
        return pushOutput

    # Removes a Node in the Hashmap
    # Finds the key to the location of the Node
    # Then iterates through the Linked List until
    # it finds correct Node to remove
    def remove(self, data):
        key = self.hashFunction(data)
        removedOutput = self.buckets[key].remove(data)
        return removedOutput

    # Formal String representation of a Hashmap
    def __repr__(self):
        return '<Hashmap %r>' % self.buckets
