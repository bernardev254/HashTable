#!/usr/bin/python3
from HashTable import HashTable
from data import generate_key_value


BHT = HashTable(100)
"""
for k,v in generate_key_value():
    BHT.insert(k,v)
"""
BHT.insert("leak",1234)
BHT.insert("leke",4567)
BHT.insert("laek",47)
BHT.insert("lake",567)
BHT.insert("lkae",457)
BHT.insert("lkea",5667)

BHT.find("lake")
BHT.update("Bernard", 705157194)
BHT.list_all()
