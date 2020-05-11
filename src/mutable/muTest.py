import unittest
from hypothesis import given
import hypothesis.strategies as st
from muNode import Node
from muLinkedList import LinkedList
from muHashMap import Hashmap


class TestCaseNode(unittest.TestCase):
    #Sets the instructions to be executed before the test begins
    def setUp(self):
        self.node = Node(7,None)
    #Sets the instructions to execute after the test has started
    def tearDown(self):
        self.node = None
        del self.node


class TestNodeMethods(TestCaseNode):
    def test_init(self):
        # Check all of nodes attributes
        self.assertEqual(self.node.data, 7)
        self.assertEqual(self.node.key, None)
        self.assertEqual(self.node.next, None)

    def test_repr(self):
        # When Key is None
        reprString = repr(self.node)
        self.assertEqual(reprString, "<Node key: None data: 7>")

        # When Key is  number
        self.node.key = 45
        reprString = repr(self.node)
        self.assertEqual(reprString, "<Node key: 45 data: 7>")


class TestCaseMuLinkedList(unittest.TestCase):
    def setUp(self):
        self.linkedlist = LinkedList()

    def tearDown(self):
        del self.linkedlist


class TestLinkedListMethods(TestCaseMuLinkedList):
    def test_init(self):
        # Make Sure that LinkedList.head is None upon init
        self.assertEqual(self.linkedlist.head, None)

    def test_size(self):
        # empty Linked List returns 0 for length
        self.assertEqual(len(self.linkedlist), 0)

        # List with elements returns correct length
        for i in range(20):
            node = Node( i, None)
            self.linkedlist.add_to_tail(node)
        self.assertEqual(len(self.linkedlist), 20)

    def test_add_to_tail(self):
        # Adds element to an Empty Linked List
        node = Node(3,None)
        output = self.linkedlist.add_to_tail(node)

        self.assertEqual(repr(output), "<Node key: None data: 3>")

        # Adds element to end of Linked List with items already
        for i in range(7):
            node = Node(i,None)
            output = self.linkedlist.add_to_tail(node)
        self.assertEqual(repr(output), "<Node key: None data: 5>")

    def test_add_to_head(self):
        # Adds element to an Empty Linked List
        node = Node(3,None)
        output = self.linkedlist.add_to_head(node)

        self.assertEqual(repr(output), "<Node key: None data: 3>")

        # Adds element to first of Linked List with items already
        for i in range(7):
            node = Node(i,None)
            output = self.linkedlist.add_to_head(node)
        self.assertEqual(repr(output), "<Node key: None data: 6>")

    def test_remove(self):
        # Does not remove from an Empty Linked List
        node = Node(10,None)
        outputEmpty = self.linkedlist.remove(node.data)
        self.assertEqual(outputEmpty, "Linked List is empty, value of: 10 is not here")
        # Does not Remove anything if does not exist in Linked List
        for i in range(10):
            node = Node(i,None)
            self.linkedlist.add_to_head(node)
        outputNotHere = self.linkedlist.remove(11)
        self.assertEqual(outputNotHere, 'Node is not in LinkedList')

        # Removes correct element
        outputRemove = self.linkedlist.remove(5)
        self.assertEqual(outputRemove, 'Node with the value: 5 was removed from the LinkedList')

    def test_str(self):
        output = str(self.linkedlist)
        self.assertEqual(output, '<LinkedList: 0 nodes>')

    def test_repr(self):
        output = repr(self.linkedlist)
        self.assertEqual(output, 'LinkedList: Nodes: []')
    def test_to_list(self):
        self.assertEqual(LinkedList().to_list(), [])
        self.assertEqual(LinkedList(Node('a',None)).to_list(), ['a'])
        self.assertEqual(LinkedList(Node('a', Node('b',None))).to_list(), ['a', 'b'])
    def test_from_list(self):
        test_data = [
            [],
            ['a'],
            ['a', 'b']
        ]
        # for e in test_data:
        #     lst = LinkedList()
        #     lst.from_list(e)
        #     self.assertEqual(lst.to_list(), [])
        lst = LinkedList()
        self.assertEqual(lst.to_list(), [])
    def test_map(self):
        lst = LinkedList()
        lst.map(str)
        self.assertEqual(lst.to_list(), [])
        lst = LinkedList()
        lst.from_list([1, 2, 3])
        lst.map(str)
        self.assertEqual(lst.to_list(), ["1", "2", "3"])
    def test_reduce(self):
        # sum of empty list
        lst = LinkedList()
        self.assertEqual(lst.reduce(lambda st, e: st + e, 0), 0)
        # sum of list
        lst = LinkedList()
        lst.from_list([1, 2, 3])
        self.assertEqual(lst.reduce(lambda st, e: st + e, 0), 6)
        # size
        test_data = [
            [],
            ['a'],
            ['a', 'b']
        ]
        for e in test_data:
            lst = LinkedList()
            lst.from_list(e)
            self.assertEqual(lst.reduce(lambda st, _: st + 1, 0), lst.size())

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, a):
        lst = LinkedList()
        lst.from_list(a)
        b = lst.to_list()
        self.assertEqual(a, b)

    @given(st.lists(st.integers()))
    def test_python_len_and_list_size_equality(self, a):
        lst = LinkedList()

        lst.from_list(a)
        self.assertEqual(lst.size(), len(a))

    def test_iter(self):
        x = [1, 2, 3]
        lst = LinkedList()
        lst.from_list(x)
        tmp = []
        for e in lst:
            tmp.append(e)
        self.assertEqual(x, tmp)
        self.assertEqual(lst.to_list(), tmp)
        i = iter(LinkedList())
        self.assertRaises(StopIteration, lambda: next(i))
class TestCaseHashMap(unittest.TestCase):
    def setUp(self):
        self.hashmap = Hashmap()
    def tearDown(self):
        del self.hashmap
class TestHashmapMethods(TestCaseHashMap):
    def test_init(self):
        # Test length with default length
        self.assertEqual(self.hashmap.length, 100)
        # Test length with given length
        del self.hashmap
        self.hashmap = Hashmap(5)
        self.assertEqual(self.hashmap.length, 5)
        # Check that buckets are LinkedList Objects
        self.assertEqual(self.hashmap.buckets[3].head, None)

    def test_hashFunction(self):
        # hashes to correct key
        key = self.hashmap.hashFunction(1079)
        self.assertEqual(key, 80)

    def test_insert(self):
        # places into correct location in Hashmap
        node = Node(576,None)
        insertOutput = self.hashmap.insert(node)
        self.assertEqual(repr(insertOutput), '<Node key: 77 data: 576>')

    def test_remove(self):
        # does not remove from an empty List at specified key
        removeEmpty = self.hashmap.remove(5)
        self.assertEqual(removeEmpty, "Linked List is empty, value of: 5 is not here")

        # does not remove if it is not in List at specified key
        for i in range(10):
            node = Node(i,None)
            self.hashmap.insert(node)
        outputNotHere = self.hashmap.remove(505)
        self.assertEqual(outputNotHere, 'Node is not in LinkedList')

        # removes node from Linked List at specified key with one element
        outputRemove = self.hashmap.remove(5)
        self.assertEqual(outputRemove, 'Node with the value: 5 was removed from the LinkedList')

        # removes node from Linked List at specified key with multiple elements
        node = Node(205,None)
        self.hashmap.insert(node)
        node = Node(305,None)
        self.hashmap.insert(node)
        outputRemove = self.hashmap.remove(305)
        self.assertEqual(outputRemove, 'Node with the value: 305 was removed from the LinkedList')


if __name__ == '__main__':
    unittest.main()
