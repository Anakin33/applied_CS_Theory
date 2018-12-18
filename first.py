'''Reminder that the core data structures used in Python are:
* Lists
* Tuples
* Sets
* Dictionaries
* Dataclasses & NamedTuples
* Enums
* Optional

### Free response

1. Both sets and dictionaries use hashing. What does this mean? Explain what happens when you add a new member to the collection.
Explain what happens when you look up a pre-existing member.
You take a larger amount of data and process it through algo to give you consistent a smaller chunk. Every input should be processed into the same input.
Ex:
1010101 -> algorithm  -> eggs
1010103 -> algorithm  -> bacon
1010101 -> algorithm  -> eggs
key value pairs

print(101010)
eggs

When you add a new nember, it creates a new bucket to store that member.
When you look up that pre existing member it calls the has function and retrieves what is in the bucket


1. Name one downside of using sets and dictionaries.
Set: no index so you cant keep track of things
Dictionary:
Again there is no index


1. For a list, how long does it take to look up a member by its index? How long to look it up by its value (e.g. find the number 3)?
index is instant.
value is much longer because we have to do a for loop or binary search if we sort the list.


1. You want to store someone's GPS coordinates (latitude and longitude). Which data structure would be most appropriate? Why?
DataClass. Not 100% sure what the benefits are. I think its due to ease of structure. less code then a dict.


1. You want to store the number of underwear, socks, shirts, and pants that a person owns. Which data structure would be most appropriate? Why?
dictionary: You want to be able to look up that info and the best way to do that is with a key value pair


1. You want to store the items of your reading list in order of when you added it. Which data structure would be most appropriate? Why?
list. it would be easiest to append an item and then use the index for order.


1. You want to store the ID numbers for your employees. Which data structure would be most appropriate? Why?
You would use a tuple. Since we know everyone has a name and an id we could save memeory by only worrying about those two elements.


1. Dictionaries can be used for the same purpose as dataclasses. What are some situations and reasons where you should use a dataclass instead of a dictionary?


1. What does Optional mean? When should you use it?
'''


