# define hashmap
'''
1. define listBuckets of hashmap
2. hash mapping function
3. insert a node
4. delete a node
'''


# length is the length of listbuckets of hashmap
def hash_Function(node, length):
    key = node.value % length
    node.key = key
    return key


# insert the node into the head of hasmap
def insert_hash(node, buckets):
    key = hash_Function(node, len(buckets))
    node.key = key
    add_node = cons(buckets[key],node)
    if add_node:
        return 1
    else:
        return 0


# remove hashnode
def remove_hash(node, buckets):
    key = hash_Function(node, len(buckets))
    remove_node = remove(buckets[key], node.value)
    if remove_node:
        return 1
    else:
        return 0


def size(node):
    if node is None:
        return 0
    else:
        return 1 + size(node.next)


# add a new node to head of the list
def cons(head, node):
    # Pass the header node, and the key value of the node to be added
    """add new element to head of the list"""
    # cur = head
    # while cur.next is not None :
    #     cur = cur.next
    # cur.next = Node(None,tail,None)
    # return head
    # node = Node(tail_key,tail_value,head.next)
    node.next = head.next
    head.next = node
    return head


#  delete the value of element of the list, return the node that we deleted
def remove(head, element):
    # node is the first node in the list, and it stand for the list
    # assert node is not None, "element should be in list"
    # if node.value == element:
    #     return node.next
    # else:
    #     return cons(node.value, remove(node.next, element))
    cur = head.next
    p = head

    while cur is not None:
        if cur.value == element:
            deleted = cur
            p.next = cur.next
            cur = cur.next
        else:
            cur =cur.next
    return deleted



# get the value of the node
def head(node):
    assert type(node) is Node
    return node.value


# get the next node
def tail(node):
    assert type(node) is Node
    return node.next





def mempty():
    return None


def mconcat(head1, head2):
    if head1.next is None:
        return head2
    if head2.next is None:
        return head1
    else:
        cur = head1
        while cur.next is not None:
            cur = cur.next
        cur.next = head2.next
    return head1




def to_list(head):
    list = []
    # list_keys = []
    cur = head.next
    while cur is not None:
        list.append([cur.key,cur.value])
        # list_keys.append(cur.key)
        cur = cur.next
    return list

    # From_list converts a list to a chain phenotype
def from_list(nodes):
    head = Node(None,None,None)
    root = None
    if len(nodes) == 0:
        return head
    for d in reversed(nodes):
        root = Node(d[0],d[1], root)
    head.next = root
    return head
    # self.head = root

def iterator(head):
    if head is not None:
        cur = head.next

        def foo():
            nonlocal cur
            if cur is None:
                raise StopIteration
            tmp = [cur.key, cur.value]
            cur = cur.next
            return tmp

        return foo
    else:
        raise StopIteration



class Node(object):
    def __init__(self,key=None,value=None, next=None):
        """node constructor"""
        self.key = key
        self.value = value
        self.next = next

    def __repr__(self):
        if self.key != None:
            return "<Node key: %d data: %d>" % (self.key, self.value)
        else:
            return "<Node key: %s data: %d>" % (self.key, self.value)

    def __str__(self):
        """for str() implementation"""
        if type(self.next) is Node:
            return "{}: {} : {}".format(self.key, self.value, self.next)
        return "{} : {}".format(self.key,self.value)

    def __eq__(self, other):
        """for write assertion, we should be abel for check list equality (list are equal, if all elements are equal)."""
        if other is None:
            return False
        if self.value != other.value:
            return False
        if self.key != other.key:
            return False
        return self.next == other.next


# if __name__ == '__main__':
#     n1 = Node(0, None)
#     n2 = Node(1, None)
#     n3 = Node(2, None)
#     n4 = Node(3, None)
#     buckets = [n1, n2, n3]
#     # test = tail(n3)
#     # rev = reverse(n3, acc=None)
#     print(len(buckets))
#     # print(buckets[1].value)
#     resn4 = insert_hash(n4, buckets)
#     print(resn4.value)
