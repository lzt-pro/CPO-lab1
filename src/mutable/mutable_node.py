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
