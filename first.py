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
An optional allow for an input of none, along with another class. If there is a chance you could have a none input.
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
reversed(ll)
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
#print(given.values())

'''
P8. Given {"english": "hello", "spanish": "hola", "french": "bonjour"}, return all the languages (without their corresponding greeting).
'''
#print(given.keys())

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
printer = [v for v in enumerate(lister)]

#print(printer)


'''
P13. Write a function that takes as input a number x and tries to return 1/x. Consider what should happen when x == 0? 
What should the function's return data type be?

'''
from typing import Optional
def divide(x: int) ->Optional[float]:
    if x == 0:
        return None
    return 1/x
#print(divide(-44))

#Return is a float.

'''
### Project
Design and implement the data structures for an inventory management system for Whole Foods.

Each item in the inventory should include its
name, 
its SKU, 
its price, 
its shelf, 
its category (e.g. produce, dairy), 
and its quantity, 
along with optional discount, 
vegan classification (none, vegetarian, or vegan), 
gluten-free classification (yes or no), 
and any other thing you think is relevant.

Decide which data structure you would use to collect all of the different inventory items together. 
You don't need to group by any attribute, e.g. don't group by shelf or by category.

Once you have this all designed, create 5-10 fake items to help with the below.

--
'''

from dataclasses import dataclass
from enum import Enum
from typing import List, Dict


class GroceryTypes(Enum):
    COLD = 'cold'
    PACKAGE = 'package'
    LUX = 'lux'

@dataclass
class groceryItem:
    sku: str
    price: float
    shelf: str
    category: GroceryTypes
    quantity: int
    discount: Optional[float] = None
    vegan_class: Optional[str] = None
    gluten_free: bool = False


romaine = groceryItem("lettuce", 1, "veggies", GroceryTypes.COLD, 10, .05, 'vegan', True)
steak = groceryItem("steakers", 50, "meat", GroceryTypes.COLD, 100, .01, 'none', True)
almonds = groceryItem("almonds", 5.99, "nuts", GroceryTypes.PACKAGE, 10000, .50, 'vegan', True)
cheese = groceryItem("cheese", 100, "dairy", GroceryTypes.COLD, 1, .15, 'vegetarian', True)
bread = groceryItem("bready", .99, "junk", GroceryTypes.PACKAGE, 2, .33, 'vegan', False)
spice = groceryItem("pepper", 100000, "spice", GroceryTypes.LUX, 0, .10, 'vegan', True)
coffee = groceryItem("stumptown", 10, "coffee", GroceryTypes.LUX, 0, .33, 'vegan', True)
tea = groceryItem("green tea ", 20, "coffee", GroceryTypes.LUX, 3, .33, 'vegan', True)
chocolate = groceryItem("dark chocolate", 30, "coffee", GroceryTypes.LUX, 2, .33, 'none', True)

grocery = [romaine, steak, almonds, cheese, bread, coffee, spice, tea, chocolate]

from itertools import groupby
import math


def sort_to_shelf(listy):
    sorted_list = sorted(listy, key=lambda x: x.shelf)
    return groupby(sorted_list, lambda x: x.shelf)


def get_average(listy):
    start = sort_to_shelf(listy)
    return {shelf: math.floor(sum(grocery.price for grocery in groceries)/len(grocery)) for shelf,groceries in start}



print(get_average(grocery))

"""
for key, group in groupby(things, lambda x: x[0]):
    listOfThings = " and ".join([thing[1] for thing in group])
    print key + "s:  " + listOfThings + "."
    
"""


"""
Write a function that will find the average price per each shelf of food.
It should take as an argument whichever collection you decide to use to collect all the inventory items,
and return a mapping of each category to its average price.

Need to group all of the dicts that have the same key value pairs and then add up there prices and divide by the total number of dicts


"""

def is_vegan(listy):
    start = sort_to_shelf(listy)
    return {shelf: any(grocery.vegan_class == 'vegan' for grocery in groceries)for shelf,groceries in start}


print(is_vegan(grocery))


"""

Write a function that will find for each shelf if any of the items are vegan.
It should take as an argument whichever collection you decide to use to collect all the inventory items, 
and return a mapping of each shelf to a boolean if it has any vegan item or not.
---

"""
def find_low_q (listy: List[groceryItem]) -> List[groceryItem]:
    return [xx.sku for xx in listy if xx.quantity <= 1]

print(find_low_q(grocery))



"""

Write a function that will find which item(s) you only have 1 or less quantity of. 
It should take as an argument whichever collection you decide to use to collect all the inventory items, 
and return a collection of the matched items.

--

Include type hints throughout the project.

__Note: in the real world, this would be hooked up to a database. But this is an exercise that you would have to do regardless.__

"""