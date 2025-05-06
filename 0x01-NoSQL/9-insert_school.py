## 9-insert_school.py

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection with the given keyword arguments.

    Parameters:
    mongo_collection -- the pymongo collection object
    **kwargs -- the document attributes to insert

    Returns:
    The new _id of the inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
