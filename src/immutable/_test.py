import unittest
from hypothesis import given
import hypothesis.strategies as st
# from demotable_v import *
from imnode import *


class TestImnode(unittest.TestCase):
    def test_size(self):
        self.assertEqual(size(None), 0)
        self.assertEqual(size(cons(Node(1,None,None),Node(1,'a',None))), 2)
        # self.assertEqual(size(cons('a', cons('b', None))), 2)

    def test_cons(self):
        self.assertEqual(cons(Node(1,None,None),Node(1,'a',None)), Node(1,None, Node(1,'a',None)))
        #self.assertEqual(cons('a', cons('b', None)), Node('a', Node('b', None)))

    def test_remove(self):
        head = Node(1,None,None)
        head.next = Node(1,'a',None)
        head.next.next = Node(2,'b',None)
        self.assertEqual(remove(cons(Node(1,None,None),Node(1,'a',None)),'a'), Node(1,'a',None))


    def test_head(self):
        # self.assertRaises(AssertionError, lambda: head(None))
        self.assertEqual(head(Node(1,'a',None)), 'a')

    def test_tail(self):
        # get the next node
        #self.assertRaises(AssertionError, lambda: tail(None))
        head = Node(1, None, None)
        nodea = Node(1, 'a', None)
        nodeb = Node(1, 'b', None)
        head.next = nodea
        nodea.next = nodeb
        self.assertEqual(tail(nodeb), None)
        self.assertEqual(tail(head), nodea)

    #
    def test_reverse(self):
        head = Node(1, None, None)
        nodea = Node(1, 'a', None)
        nodeb = Node(1, 'b', None)
        head.next = nodea
        nodea.next = nodeb
        self.assertEqual(reverse(None), None)
        self.assertEqual(reverse(nodea), Node(1,'b',Node(1,'a',None)))
        # self.assertEqual(reverse(cons('a', cons('b', None))), cons('b', cons('a', None)))

    #
    def test_mconcat(self):
        self.assertEqual(mconcat(None, None), None)
        self.assertEqual(mconcat(cons('a', None), None), cons('a', None))
        self.assertEqual(mconcat(None, cons('a', None)), cons('a', None))
        self.assertEqual(mconcat(cons('a', None), cons('b', None)), cons('a', cons('b', None)))

    #
    def test_to_list(self):
        self.assertEqual(to_list(None), [])
        self.assertEqual(to_list(cons('a', None)), ['a'])
        self.assertEqual(to_list(cons('a', cons('b', None))), ['a', 'b'])

    #
    def test_from_list(self):
        test_data = [
            [],
            ['a'],
            ['a', 'b']
        ]
        for e in test_data:
            self.assertEqual(to_list(from_list(e)), e)

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, a):
        self.assertEqual(to_list(from_list(a)), a)

    @given(st.lists(st.integers()))
    def test_monoid_identity(self, lst):
        a = from_list(lst)
        self.assertEqual(mconcat(mempty(), a), a)
        self.assertEqual(mconcat(a, mempty()), a)

    def test_iter(self):
        x = [1, 2, 3]
        lst = from_list(x)
        tmp = []
        try:
            get_next = iterator(lst)
            while True:
                tmp.append(get_next())
        except StopIteration:
            pass
        self.assertEqual(x, tmp)
        self.assertEqual(to_list(lst), tmp)
        get_next = iterator(None)
        self.assertRaises(StopIteration, lambda: get_next())

    def test_hash_Function(self):
        node1 = Node(10, None)
        node2 = Node(15, None)
        self.assertEqual(hash_Function(node1, 5), hash_Function(node2, 5))

    def test_insert_hash(self):
        buckets = [0, 1, 2, 3, 4]
        node1 = Node(10, None)
        node2 = Node(15, None)
        self.assertEqual(insert_hash(node1, buckets), insert_hash(node2, buckets))

    def test_remove_hash(self):
        buckets = [
            Node(0, None),
            Node(1, None),
            Node(2, None),
            Node(3, None),
            Node(4, None),
        ]
        node1 = Node(20, None)
        node2 = Node(5, None)
        node3 = Node(10, None)
        node4 = Node(15, None)
        buckets[0].next = node1
        node1.next = node2
        node2.next = node3
        node3.next = node4
        hash_Function(node1, len(buckets))
        hash_Function(node2, len(buckets))
        hash_Function(node3, len(buckets))
        hash_Function(node4, len(buckets))
        # for i in range(1,5):
        #     s='node'+str(i)
        #     hash_Function(s,len(buckets))
        self.assertEqual(remove_hash(node1, buckets), 1)


if __name__ == '__main__':
    unittest.main()
