# CPO-lab1
Computational Process Organization lab1 
## title: hash-map
Hash-map (collision resolution: separate chaining, for array and bucket you can use built-in list) based set.
## list of group members
Zhentao Liu 
Shuo Cui

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

immutable_test: in this module we define the test method for the function in the immutable_node;

mutable_node: define the class Node;

mutable_Linked_List: define the class LinkedList and its method,properties;

mutable_hash_map: in this module, 





## conclusion 

Mutable object: the value of the object stored in the address will not be changed (a change is to create a new address and put the value of the new object in the new address and the original object will not change).Just like  the type dictionary,list;

Immutable object: the value of the object in its address changes in place. Just like the type: string,int,tuple,float;