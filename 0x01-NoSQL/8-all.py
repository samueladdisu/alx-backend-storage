#!/usr/bin/env python3
""" lists all docs """
def list_all(mongo_collection):
    list = mongo_collection.find()
    if list:
        return list
    else:
        return []
