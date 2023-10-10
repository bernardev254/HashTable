#!/usr/bin/python3
from linkedList import LinkedList, Node
"""
a module for a basic hash table class
"""
class HashTable():
    """Basic hash table class"""
    def __init__(self,max_size):
        self.data_list = [None] * max_size
        

    def insert(self, key, value):
        """insert a key value pair into the data_list"""
        index = self.get_valid_index(self.data_list, key)
        if self.data_list[index] == None:
            self.data_list[index] = key,value
        
        elif type(self.data_list[index]) == tuple:
            data_linkedList = LinkedList()
            previous_kv = self.data_list[index]
            data_linkedList.append(previous_kv)
            data_linkedList.append((key,value))
            self.data_list[index] = data_linkedList
        else:
            self.data_list[index].append((key,value))


    def find(self, key):
        """find the value given a key"""
        index = self.get_valid_index(self.data_list, key)
        if type(self.data_list[index]) == tuple:
            try:
                k_vPair = self.data_list[index]
                print(k_vPair[1])
                return k_vPair[1]
            except:
                print(None)
                return None
            
        elif type(self.data_list[index]) == LinkedList:
            current = self.data_list[index].head
            while current:
                if current.data[0] == key:
                    print(current.data[1])
                    return current.data[1]
                current = current.next
            print(None)
            return None
        else:
            return None

    def update(self, key, value):
        """update the value in the data_list with new value"""
        index = self.get_valid_index(self.data_list, key)
        if type(self.data_list[index]) == tuple:
            #print("UPDATED")
            self.data_list[index] = key,value
        elif type(self.data_list[index]) == LinkedList:
            current = self.data_list[index].head
            while current:
                if current.data[0] == key:
                    current.data[1] = value
                current = current.next
        

    def list_all(self):
        """list all the keys stored in the data_list"""
        mylist = []
        for item in self.data_list:            
            if item:
                if type(item) == LinkedList:
                    current = item.head
                    while current:
                        mylist.append(current.data[0])
                        current = current.next
                if type(item) == tuple:
                    mylist.append(item[0])
        print(mylist)
        return mylist

    @staticmethod
    def get_index(data_list:list,key:str)-> int:
        weight = 0
        for char in key:
            weight += ord(char)
        index = weight % len(data_list)
        return index
    @staticmethod
    def get_valid_index(data_list:list,key:str)-> int:
        index = hash(key) % len(data_list)
        return index