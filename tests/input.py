from types import SimpleNamespace as o

input = o()

#
# case 1
# just a SimpleNamespace
#
input.case1 = o(aKey="a val")


#
# case 2
# array
#
input.case2 = [o(aKey="a val"), o(bKey="b val")]


# case 3
# dict and function
#
anArray = [o(aKey="a val"), o(bKey="b val")]


def c():
    pass


aDict = {"cKey": c, "dKey": 1}
input.case3 = o(anArray=anArray, aDict=aDict)


#
# case 4
# recursive reference root
#

child = o(name="billy")
parent = o(name="bob", child=child)
child.parent = parent

input.case4 = parent


#
# case 5
# recursive reference nested object
#

child = o(name="billy")
parent = o(name="bob", child=child)
child.parent = parent
grandparent = o(name="holdor", children=[o(bob=parent)])
superGrandparent = o(name="adam", child=grandparent)

input.case5 = superGrandparent


#
# case 6
# empty array and dict
#

input.case6 = o(someArray=[], someDict={})


#
# case 7
# keeps shallow refs (traverses breadth-first)
#

billy = o(name="billy")
bob = o(name="bob", child=billy)
holdor = o(name="holdor", child=bob)
adam = o(child=holdor, superGrandChild=billy, name="adam")

input.case7 = adam


#
# case 8
# ensure breadth-first traversal doesn't mess up array ordering
#

input.case8 = [o(complex=True), "simple"]
