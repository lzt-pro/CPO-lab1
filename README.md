# CPO-lab1
Computational Process Organization lab1 
## title: hash-map
Hash-map (collision resolution: separate chaining, for array and bucket you can use built-in list) based set.
## list of group members
- Zhentao Liu 
  
  - ID: 192050212
  - Email : lztkystu@163.com
  
- Shuo Cui
 
  -  ID: 192050212
  - Email:13652027261@163.com

  

## laboratory work number: 4
## variant description
Hash-map (collision resolution: separate chaining, for array and bucket you can use built-in list) based set.



## synopsis 

work of Zhentao Liu :

1. Design and develop a mutable version

2. realize the hash-map by using the mutable version

3. This is a Hash-map that is designed to be a list where each element of the list is a Linked-List. Each element in the Hash-map has a key, which takes you to a specific Linked List. There you have access to the first element of the list. The Hash-map was designed this way in order to utilize the chaining method of resolving collisions.  When two elements are supposed to be inserted to the same key, instead of having to calculate a new location (in a basic Hash-map without Linked Lists), we just add them both to the Linked List.  

   

work of ShuoCui:

1. Design and develop a immutable version
2. realize the hash-map by using the immutable version
3. this is a hash-map that is designed to be  n linked-lists(it is not the real one,it just makes up by the node in immutable version  ),and the hash key is saved in each  head node of the  linked-lists,so the other operation just like adding ,removing and finding can execute in each linked-list .



##  descriptions of  modules

immutable_node: In  this module we define the immutable node to implement  linked list hash map,also there are some methods to construct list and realize the main function for it and hash,just like insert,remove for hash and list.

### immutable

###### In the immutable_node.py, We have design three classes, Node and use the node to implement  linked_list,hashmap,the simple desciption as following :

- class Node(object):
      def __init__(self, value, next):
          """node constructor"""
          self.key = None
          self.value = value
          self.next = next

  the node has the properties value,next and key;

- def list_size(list): get the length of list and the item of list is node
- def append_node(lst,nod): add a new node to the hail of linked_list
- def list_size(list):get the length of list and the item of list is node
- def append_node(lst,nod):add a new node to the hail of liked_list

- def remove(node, element): delete the value of element of the list

- def head(node): get the value of the node

- def tail(node): get the next node

- def reverse(node, acc=None): reverse the linked_list

- def mconcat(node1, node2): concat node1 and node2

- def to_list(node): change the linked_list to list[]

- def hash_Function(node, length): give the inserting node a key

- def insert_hash(node, buckets): insert the node into the head of hasmap

- def remove_hash(node, buckets):remove hashnode

- def from_hashmap(bukets, testdat: change the Built-in list to hashmap

- def hasmap_to_list(buket): change hasmap to list[]

```
#1 get the length of list and the item of list is node
def list_size(list):

#2 add a new node to the head of liked_list
def cons(head, tail):
   
#3 add a new node to the hail of liked_list
def append_node(lst,nod):

#4 delete the value of element of the list
def remove(node, element):
    
#5 get the value of the node
def head(node):

#6 get the next node
def tail(node):
    
#7 reverse the linked_list
def reverse(node, acc=None):
  
#8 return a empty object
def empty():

#9 concat node1 and node2
def mconcat(node1, node2):   

#10 iterator
def iterator(lst):

#11 change list[] to the linked_list
def from_list(lst):    
    
#12 change the linked_list to list[]
def to_list(node):      
    
#13 give the inserting node a key
def hash_Function(node, length):

#14 insert the node into the head of hasmap
def insert_hash(node, buckets):


#15 remove hashnode
def remove_hash(node, buckets):

#16 change hasmap to list[]
def hasmap_to_list(buket):

#17 change the list to hashmap
def from_hashmap(bukets, testdata):

```




###### in the module immutable_test.py , we test the all method in  immutable_node.py.



### mutable

In the mutable.py, We have design three classes, Node, LinkedList and Hashmap, the simple desciption as following :

```
class Node(object):

    def __init__(self, data=None, next=None):
        self.key = None
        self.data = data
        self.next = next
 class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.current = None
 class Hashmap(object):

    def __init__(self, length=5):
        listBuckets = []
        for i in range(length):
            head = Node(None, None)
            head.key = i
            listBuckets.append(LinkedList(head))
        self.buckets = listBuckets
        self.length = length
```

**Class Node:** 

- I have designed key, data and next. Key as the hashmap key,  the value is stored in the data field, and next node in next field.

**Class LinkedList:** 

- In the Class LinkedList, I designed 9 functions for developing hashmap. 

- size : Returns the length of the current linkedlist. 

- to_list: Convert linkedlist to list

- from_list: Convert list to linkedlist

- _last_node: return the last node in linkedlist.

- hash_map: Map the data value according to the function passed in

- hash_reduce: Reduce each value in the linkedlist

- add_to_tail: Add a node to the tail of linkedlist.

- add_to_head: Add a node to the head of linkedlist

- remove: Delete the node where data is a specific field

**Class Hashmap:** 

- In the Class LinkedList, I designed 5 functions.

- to_list: Convert buckets in hashmap to list

- from_list: Convert list to buckets 

- hashFunction: Mapping the data to key,  as the primary step for collision resolution

- insert: Add a node to hashmap 

- remove: Delete the node where data is s pecific field 
- data_find_node: Look up the node based on the data
- filter_key: Look up the linkedlist by key
- mempty: Set up the hashmap buckets empty list
- mconcat: Adds node to the buckets of the hashmap

```
# 1. add a new element
def add_to_tail(self, node）
def add_to_head(self, node)
# 2. remove an element
def remove(self, value) 
def remove(self, data) 
# 3. size
def size(self) 

# 4. conversion from and to python lists
def to_list(self)  
def from_list(self, lst) 
def to_list(self) 
def from_list(self, list)

# 5. ﬁnd element by speciﬁc predicate
def data_find_node(self,data) 

# 6. ﬁlter data structure by speciﬁc predicate
def filter_key(self,key) 

# 7. map structure by speciﬁc function
def hash_map(self, str) 

# 8. reduce – process structure elements to build a return value by speciﬁc functions
def hash_reduce(self, f:lambda st, e: st + e, 0, initial_state) 

# 9. mempty and mconcat
def mempty(self)
def mconcat(self)
# 10. iterator
def __iter__(self) 
def __next__(self) 
```





## conclusion 

Mutable object: the value of the object stored in the address will not be changed (a change is to create a new address and put the value of the new object in the new address and the original object will not change).Just like  the type dictionary,list;

Immutable object: the value of the object in its address changes in place. Just like the type: string,int,tuple,float;