## 10-update_topics.py

def update_topics(mongo_collection, name, topics):
    """
    Update the topics of a school document.

    Parameters:
    mongo_collection -- the pymongo collection object
    name -- the name of the school to update
    topics -- the new list of topics to set

    Returns:
    The number of documents modified.
    """
    result = mongo_collection.update_one(
        {"name": name},       ## filter to find the document
        {"$set": {"topics": topics}}  ## update operation
    )
    return result.modified_count
