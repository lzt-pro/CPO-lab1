# define hashmap
'''
1. define listBuckets of hashmap
2. hash mapping function
3. insert a node
4. delete a node
'''
# length is the length of listbuckets of hashmap
def hashFunction(node,length):
    key = node.value % length
    node.key = key
    return key
# 头插法插入hashmap当中
def insert_hash(node,buckets):
    key = hashFunction(node,len(buckets))
    node.key = key
    add_node = cons(node,buckets[key])
    return add_node
# 删除 hashnode
def remove_hash(node,buckets):
    key = hashFunction(node,buckets)
    remove_node = remove(buckets[key],node.value)
    return remove_node

def size(n):
        if n is None:
            return 0
        else:
            return 1+size(n.next)
# 添加新元素
def cons(head, tail):
    """add new element to head of the list"""
    return Node(head,tail)
# 删除在list中的element值
def remove(n,element):
    assert n is not None,"element should be in list"
    if n.value == element:
        return n.next
    else:
        return  cons(n.value,remove(n.next,element))
# 当前node节点的值
def head(n):
    assert type(n) is Node
    return n.value
# 获取node节点的下一个
def tail(n):
    assert type(n) is Node
    return n.next
# 链表倒置
def reverse(n,acc=None):
    if n is None:
        return acc
    return reverse(tail(n),Node(head(n),acc))

def mempty():
    return None

def mconcat(a,b):
    if a is None:
        return b
    tmp = reverse(a)
    res =b
    while tmp is not None:
        res = cons(tmp.value, res)
        tmp=tmp.next
    return  res

def to_list(n):
    res = []
    cur = n
    while cur is not None:
        res.append(cur.value)
        cur = cur.next
    return res

def from_list(lst):
    res = None
    for e in reversed(lst):
        res = cons(e, res)
    return res

def iterator(lst):
    cur = lst
    def foo():
        nonlocal cur
        if cur is None: raise StopIteration
        tmp = cur.value
        cur = cur.next
        return tmp
    return foo

class Node(object):
    def __init__(self, value,next):
        """node constructor"""
        self.key = None
        self.value = value
        self.next = next

    def __repr__(self):
        if self.key != None:
            return "<Node key: %d data: %d>" % (self.key, self.value)
        else:
            return "<Node key: %s data: %d>" % (self.key, self.value)

if __name__ == '__main__':
    n1 = Node(0,None)
    n2 = Node(1,None)
    n3 = Node(2,None)
    n4 = Node(3,None)
    buckets = [n1,n2,n3]
    # test = tail(n3)
    # rev = reverse(n3, acc=None)
    print(len(buckets))
    # print(buckets[1].value)
    resn4 = insert_hash(n4,buckets)
    print(resn4.value)