#!/usr/bin/env python3
"""
Module for MongoDB operations with Python
"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection
    
    Args:
        mongo_collection: The pymongo collection object
        
    Returns:
        List of all documents or empty list if no document
    """
    if mongo_collection is None:
        return []
    
    return list(mongo_collection.find())
