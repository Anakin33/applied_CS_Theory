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


2. Name one downside of using sets and dictionaries.
Set: no index so you cant keep track of things
Dictionary:
Again there is no index


3. For a list, how long does it take to look up a member by its index? How long to look it up by its value (e.g. find the number 3)?
index is instant.
value is much longer because we have to do a for loop or binary search if we sort the list.


4. You want to store someone's GPS coordinates (latitude and longitude). Which data structure would be most appropriate? Why?
DataClass. You can compare them where you can not do that with dicts. They also require much less code. You can use .dot notation vs bracket


5. You want to store the number of underwear, socks, shirts, and pants that a person owns. Which data structure would be most appropriate? Why?
dictionary: You want to be able to look up that info and the best way to do that is with a key value pair


6. You want to store the items of your reading list in order of when you added it. Which data structure would be most appropriate? Why?
list. it would be easiest to append an item and then use the index for order.


7. You want to store the ID numbers for your employees. Which data structure would be most appropriate? Why?
You would use a tuple. Since we know everyone has a name and an id we could save memeory by only worrying about those two elements.


8. Dictionaries can be used for the same purpose as dataclasses.
What are some situations and reasons where you should use a dataclass instead of a dictionary?
When you want to compare to dataclasses.
__init__(), .__repr__(), and .__eq__() implemented for you.
easier to add data
its nice you declare your variable types ahead of inputtingdata


9. What does Optional mean? When should you use it?

'''
'''
### Code challenges

P1. Given [1, 2, 3, 4, 5], write a list comprehension that multiplies every member of the list by 3.

'''
list1 = [1,2,3,4,5]
multiplied = [item*3 for item in list1]
#print(multiplied)
'''

P2. Given [-2, 0, -1, 5, 2], write a list comprehension that filters out any number <= 0 and adds 9 to each of the remaining members.

'''
list2 = [-2, 0, -1, 5, 2]
filtered = [x+9 for x in list2 if x <= 0]
#print(filtered)
'''

P3. Given [-2, 0, -1, 5, 2], write a list comprehension that adds 9 to each member if it is > 0 or subtracts 3 if it is <= 0.
'''
l = [-2, 0, -1, 5, 2]
filteredA = [v+9 if v > 0 else v-3 for v in l]
#print(filteredA)

'''
P4. Return [2, 1, 0, -1, -2] reversed.

'''
ll = [2, 1, 0, -1, -2]
ll.reverse()
#print(ll)
'''

P5. Return "Hello World" sorted alphabetically.
'''
h = 'Hello World'
b = ''.join(sorted(h.lower()))
#print(b)

'''

P6. Convert ["a", "b", "c"] to a set.

'''
listy = ["a", "b", "c"]
#print(set(listy))

'''
P7. Given {"english": "hello", "spanish": "hola", "french": "bonjour"}, return all the greetings (without their corresponding language).

'''
given = {"english": "hello", "spanish": "hola", "french": "bonjour"}
#print(given.keys())

'''
P8. Given {"english": "hello", "spanish": "hola", "french": "bonjour"}, return all the languages (without their corresponding greeting).
'''
#print(given.values())

'''

P9. Given {"english": "hello", "spanish": "hola", "french": "bonjour"}, invert the keys and values so that the greeting is the key, and the language is the value. 
Use a dictionary comprehension to do this.

'''
given2 = {"english": "hello", "spanish": "hola", "french": "bonjour"}
dict_variable = {value:key for (key,value) in given2.items()}
#print(dict_variable)


'''

P10. Given ["a", "b", "c", "d"], return the letter "c".

'''
sen = ["a", "b", "c", "d"]
#print(sen[2])

'''

P11. Given ("a", "b", "c", "d"), return the letter "c".
'''

senc = ("a", "b", "c", "d")
list(senc)
#print(senc[2])
'''


P12. Given ["a", "b", "c", "d"], print each letter along with its corresponding index.

'''
lister = ["a", "b", "c", "d"]
printer = [v for v in lister]
#print(printer)

'''
P13. Write a function that takes as input a number x and tries to return 1/x. Consider what should happen when x == 0? 
What should the function's return data type be?

'''
def divide(x):
    if x != 0:
        return 1/x
print(divide(-44))

#Return is a float.