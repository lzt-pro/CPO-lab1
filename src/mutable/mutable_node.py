class Node(object):

    def __init__(self, data=None, next=None):
        self.key = None
        self.data = data
        self.next = next
    # Computes the official String representation of Node Objects
    # Since we have not defined __str__ this is used for
    # informal string representation as well
    def __repr__(self):
        if self.key != None:
            return "<Node key: %d data: %d>" % (self.key, self.data)
        else:
            return "<Node key: %s data: %s>" % (self.key, self.data)
