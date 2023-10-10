# HASH TABLES

## Table of Contents

- [About](#about)
- [Hash function](#hash function)
- [Collisions handling](#collision handling)
- [Python dictionary](#python dictionary)

## about

A hash table is a data structure that uses a list/array to store the key-value pairs and uses a hash function to determine the index for storing and retrieving the data associated with a given key.

## hash function

A hash function uses any algorithm that generates an index from a given key.It essentially converts a string or any other non-numeric data type into a number that can then be used as an index to store thekey value pair in the list/array

## collision handling
Collisions occur when two different keys produce the same hash value orindex. There are several techniques to handle collisions in hash tables:

- Chaining: In chaining, each index in the array contains a linked list (or some other data structure like a binary search tree) to store multiple key-value pairs that have the same hash value. When a collision occurs, the new key-value pair is appended to the linked list at that index.

- Open Addressing: Open addressing involves finding the next available slot (usually through a probing sequence) when a collision occurs and storing the key-value pair there. There are different probing methods like linear probing, quadratic probing, and double hashing.

- Robin Hood Hashing: Robin Hood hashing aims to minimize the impact of collisions by trying to evenly distribute key-value pairs and reducing the displacement of keys with a smaller difference in their ideal and current positions.

- Cuckoo Hashing: Cuckoo hashing is another technique that deals with collisions by having multiple hash functions and allowing keys to be relocated to different slots if a collision occurs. It can lead to rehashing the entire table if a cycle is detected.

> for this project we will use chain Hashing where for all keys colliding we will maintain linked lists and store different k,v pairs with simillar hash

## python dictionaries
In Python, the built-in dictionary data structure is an example of a hash table. Python dictionaries are highly optimized and efficient, providing constant-time average complexity for operations like inserting, accessing, and deleting key-value pairs.

You can use Python dictionaries as follows:
```
# Creating a dictionary
my_dict = {'key1': 'value1', 'key2': 'value2'}

# Accessing values
value = my_dict['key1']

# Adding a new key-value pair
my_dict['key3'] = 'value3'

# Removing a key-value pair
del my_dict['key2']

```
Python dictionaries handle collisions and resizing of the underlying array automatically, making them a convenient choice for hash table functionality in most cases.
