#!/usr/bin/env python3
""" find one """


def schools_by_topic(mongo_collection, topic):
    """ finde topic """
    docs = mongo_collection.find({"topic": topic})
    return docs
