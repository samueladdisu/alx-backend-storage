#!/usr/bin/env python3
""" lists all docs """


def list_all(mongo_collection):
    """ list all docs """
    list = mongo_collection.find()
    if list.count() == 0:
        return []
    return list
