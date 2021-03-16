'''Let's cover sets. They are also a type of collection. Sets are a type of collection.Unlike lists and tuples, they are unordered. This means sets do not record element position. Sets only have unique elements. This means there is only one of a particular element in a set.

To define a set, you use curly brackets('{}'). You place the elements of a set within the curly brackets. You notice there are duplicate items. When the actual set is created, duplicate items will not be present.

You can convert a list to a set by using the function set, this is called type casting. You simply use the list as the input to the function set. The result will be a list converted to a set.Ex:
album = [1, 1, 2, 3]
set = set(album)
print(set) = return {1,2,3}

To adition on Set. Ex:
set = {3,2}
set.add('1')
print(set). Return: '3,2,1'. if you repeat the same numbers, nothing will happen

To Remove on Set. Ex:
set = {3,2}
set.remove('2')
print(set). Return: '3'.

To Verify on Set. Ex:
set = {3,2}
'3' in set
Return:True

The intersection of two sets is a new set containing elements which are in both of those sets. To find the String on the both sets, we use '&'
Ex:
Set={1,2,3}
Set1={2,4,5}
Set2=Set & Set1
Print(Set2). Return: '2'

The union of two sets is the new set of elements which contain all the items in both sets. Ex:
Set={1,2,3}
Set1={2,4,5}
Set2=Set.union(Set1)
Print(Set2). Return: '1,2,3,4,5'

We can check if a set is a subset using the issubset method.Ex:
Set={1,2,5,4,3}
Set1={2,4,5}
Set1.issubset(Set) Return: 'True'


'''