'''>>>>Tuples are an ordered sequence. They are expressed as comma separated elements within parentheses.Tuples are immutable which means we can't change them.

strings, integer, float. They can all be contained in a tuple but the typeof the variable is tuple.Ex:Tuple = (1, 'There', 5.0). print(type(tuple).He show 'Tupla'

Each element of a tuple can be accessed via an index. following the stages: The first element can be accessed by the name of the tuple followed by a square bracket with the index number,
in this case zero. Ex: print(Tuple[0]). He show '1'

We can also access the last element. In Python we can use negative index.
The relationship is as follows.Each element in Tuple have her negative index. Ex: Tuple = (1, 'There', 5,0). The '1' Will be in positive index, 0, but in index negative her be '-3'. A sequence between the numbers of negative index is the last -1, and the previously numbers -2, -3, -4...-x.

 We can concatenate or combine tuples by adding them.The result is the following with the following index. tuple1 = (1, 'There'), tuple2 = (2, 3) + tuple1. Equal to tuple2 = (2, 3, 1, 'There'). Keeping the order index, ex: 2 = [0] and There[3]

If we would like multiple elements from a tuple we could also slice. Ex: tuple2[1] = '3'. Or len(tuple2) = 4

As a consequence of immutability, if we would like to manipulate a tuple
we must create a new tuple instead. A tuple can contain other tuples as well as other complex data types. This is called nesting. We can access these elements using the standard indexing methods. Ex: tuple = (1, 2, (3, 4), (5, 6), (7, (8, 9))). print(tuple[4][1][0]). Show = '8'

****Lists are also an ordered sequence, he is represented with square brackets('[]'). In many respects lists are like tuples. One key difference is they are mutable. Lists can contain strings, floats, integers. We can nest other lists. We also nest tuples and other data structures. Like tuples, each element of a list can be accessed via an index. The index conventions for lists and tuples are identical.

can change them. For example, we apply the method extends by adding a do followed by the name of the method then parentheses. The argument insidethe parentheses is a new list that we are going to concatenate to the original list. In this case, instead of creating a new list, "L1," the original list, "L," is modified by adding two new elements. L = [1,2,3] L1.extended([4,5]),Now L = [1,2,3,4,5]

But we apply L = [1,2,3] L1.append([4,5]),Now L = [1,2,3,[4,5]]. Change the index

Every time we apply a method the list changes.If we apply extend, we add two new elements to the list. The list L is modified by adding two new elements. If we append the string A, we further change the list > L = [1,2,3] L1.extend([4,5]),Now L = [1,2,3,4,5] and L2.append[6], L = [1,2,3,4,5,6]

we can change the first element as follows.
L = [1,2,3] L[0]=5, L = [5,2,3]

We can delete an element of a list using the del command. We simply indicate the list item we would like to remove as an argument.
L = [1,2,3] delL[0] L = [2,3]

We can convert a string to a list using split. For example, the method split converts every group of characters separated by a space.
L = 'Hello rock'
L.split()
L = ['Hello', 'Rock']

'1,2,3,4'.split('.') = [1.2.3.4]

*****Aliasing Multiple names referring to the same object is known as aliasing.
a = [1,2,3,4]
a=b
a[0] = 6  b[0]  = 7
a = [7,2,3,4]

******Clone
a = [1,2,3,4]
b=a[:]
if we change a, b not will change

Use help(a) in a list



'''
tuple = (1, 2, (3, 4), (5, 6), (7, (8, 9)))
print(tuple[4][1][0])

