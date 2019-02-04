
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
    google about python magic methods and look around for __contains__

    ex: 4 in [1, 2, 4] -> True
    ex: 5 in [1, 2, 3] -> False
    """
    def __contains__(self, x):

        """
        defines behavior for membership tests using in and not in.

     a.contains(4) -> True/False
        """

    def contains(self, x):

        if x in self.my_dict:
            return True

        """
        adds a member to the AlinaSet
        """
    def add(self, member):
        self.my_dict[member] = True

    """
    removes a member to the AlinaSet
    """
    def remove(self, member):
        del self.my_dict[member]

    """
    returns the number of members of the AlinaSet
    """
    def size(self):
        return len(self.my_dict)

    """
    returns an AlinaSet that contains all elements of self that also belong to
    the passed in AlinaSet
    """
    def intersection(self, x):
        new_set = set()

        for i in A: #A set declared before

            if i in B: #B set declared before
                new_set.add(i)

        return new_set

        # new_set = set()

        # for num in x:

        #     if num in self.my_dict:

        #         new_set.add(num)

        # return new_set

    """
    returns an AlinaSet that contains all elements of self that also belong to
    the passed in AlinaSet
    """
    def union(self, x):

        A = AlinaSet() #A set declared b4!
        for i in x: 
            A.add(i)
        return A

                   
"""
TESTS GO HERE
"""

# an initialized AlinaSet is empty
a = AlinaSet()
assert(a.size() == 0)

# you can add to an AlinaSet
a = AlinaSet()
a.add(4)
assert(a.size() == 1)

# you can remove from an AlinaSetgit 
a = AlinaSet()
a.add(10)
a.remove(10)
assert(a.size() == 0)

# test that add guarantees uniqueness
a = AlinaSet()
a.add(2)
a.add(2)
assert(a.size() == 1)

#test to check existence
a = AlinaSet()
a.add(15)
assert(a.contains(15) == True)

#test for intersection 
a = AlinaSet()
A = {1,2,3}
B = {1,2,4}
a.add(A)
a.add(B)
assert(a.intersection(B) == {1,2})

#test for union
a = AlinaSet({1,2,3})
A = {1,2,3}
x = {1,2,4}
a.add(A)
a.add(x)
assert(A.union(x) == {1,2,3,4})
