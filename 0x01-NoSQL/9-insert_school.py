#!/usr/bin/env python3
""" insert school """


def insert_school(mongo_collection, **kwargs):
    """ insert document to collection """
    insert = mongo_collection.insert_one(kwargs)
