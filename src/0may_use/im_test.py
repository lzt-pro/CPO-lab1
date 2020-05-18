import unittest
from hypothesis import given,settings
import hypothesis.strategies as st
# from demotable_v import *
from may_use.imnode import *


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

    #
    def test_mconcat(self):
        head1 = Node(1, None, None)
        nodea = Node(1, 'a', None)
        head2 = Node(2, None, None)
        nodeb = Node(2, 'b', None)
        head1.next = nodea
        head2.next = nodeb
        self.assertEqual(mconcat(head1,head2), Node(1,None,Node(1,'a',Node(2,'b',None))))



    def test_to_list(self):
        head = Node(1, None, None)
        nodea = Node(1, 'a', None)
        nodeb = Node(1, 'b', None)
        head.next = nodea
        nodea.next = nodeb
        self.assertEqual(to_list(head), [[1,'a'],[1,'b']])

    def test_from_list(self):
        test_data = [
            [],
            [[None, 'a']],
            [[None, 'a'], [None, 'b']]
        ]

        for e in test_data:
            list = []
            head = Node()
            for i in e:
                node = Node(i[0],i[1],None)
                head = cons(head,node)
                list.append([i[0],i[1]])
            list.reverse()
            self.assertEqual(to_list(head), list)

    @settings(max_examples=10)
    @given(k=st.integers(), d=st.integers())
    def test_from_list_to_list_equality(self, k, d):
        # head = Node()
        v=[[k,d]]
        head = from_list(v)

        ans = to_list(head)
        self.assertEqual(ans, v)

    @given(k=st.integers(), d=st.integers())
    def test_monoid_identity(self, k,d):
        node = Node(k,d,None)
        head1 = Node()
        head2 = Node()
        head2.next = node
        self.assertEqual(mconcat(head1, head2), head2)
        self.assertEqual(mconcat(head2, head1), head2)

    def test_iter(self):
        x = [[1,1], [2,2], [3,3]]
        head = from_list(x)
        tmp = []
        try:
            get_next = iterator(head)
            while True:
                tmp.append(get_next())
        except StopIteration:
            pass
        self.assertEqual(x, tmp)
        self.assertEqual(to_list(head), tmp)


    def test_hash_Function(self):
        node1 = Node(None,10, None)
        node2 = Node(None,15, None)
        self.assertEqual(hash_Function(node1, 5), hash_Function(node2, 5))

    def test_insert_hash(self):
        buckets = [Node(0,None,None), Node(1,None,None), Node(2,None,None)]

        node1 = Node(None,3, None)
        node2 = Node(None,6, None)
        self.assertEqual(insert_hash(node1, buckets), insert_hash(node2, buckets))

    def test_remove_hash(self):
        buckets = [
            Node(None,0, None),
            Node(None,1, None),
            Node(None,2, None),

        ]
        node1 = Node(None,2, None)
        node2 = Node(None,4, None)
        node3 = Node(None,6, None)
        node4 = Node(None,8, None)
        insert_hash(node1,buckets)
        insert_hash(node2, buckets)
        insert_hash(node3, buckets)
        insert_hash(node4, buckets)
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
