"""
an AlinaSet contains no duplicates.
the contents of an AlinaSet are unordered
"""
class AlinaSet(object):
    """
    an AlinaSet can be optionally initialized with a list
    
    example:
    a = AlinaSet([1,2,3]) 
    a.size -> 3
    """
    def __init__(self, x = []):
        self.my_dict = {}

    """
    BONUS - try after the rest

    __repr__() is invoked when you simply write object's name on interactive
    python console and press enter: https://stackoverflow.com/a/19597196
    """
    def __repr__(self):
        pass

    """
    defines behavior for membership tests using in and not in.

    ex: 4 in [1, 2, 4] -> True
    ex: 5 in [1, 2, 3] -> False
    """
    def __contains__(self, x):
        pass

    """
    adds a member to the AlinaSet
    """
    def add(self,x):
        pass

    """
    removes a member to the AlinaSet
    """
    def remove(self, x):
        pass

    """
    returns the number of members of the AlinaSet
    """
    def size(self):
        pass

    """
    returns an AlinaSet that contains all elements of self that also belong to
    the passed in AlinaSet
    """
    def intersection(self, x):
        pass

    """
    returns an AlinaSet that contains all elements of self that also belong to
    the passed in AlinaSet
    """
    def union(self, x):
        pass


"""
TESTS GO HERE
"""

# an initialized AlinaSet is empty
a = AlinaSet()
a.my_dict[4] = 'butt'
print(a.my_dict)
# assert(a.size() == 0)

# you can add to an AlinaSet
# a = AlinaSet()
# a.add(4)
# assert(a.contains(4) is True)

# you can remove from an AlinaSet
# ...etc