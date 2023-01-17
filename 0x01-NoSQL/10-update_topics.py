#!/usr/bin/env python3
""" update doc """


def update_topics(mongo_collection, name, topics):
    """ update topics """
    update = mongo_collection.update(
        {"name": name},
        {"$set": {"topics": topics}},
        {
            "multi": True
            }
    )
    return update
