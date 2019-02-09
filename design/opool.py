"""
Object pool library
Constrains:
    - Assuming you have a limited N number of object to be share.

In this iteration let's assume a user story for database connections.
We are going to create a queue system.

Context manager makes the resource handling automatic so clients
don't need to remember to return the object.
"""
from queue import Queue


class Resource:
    """
    Wraps original object.
    Return the object to the pool.
    """
    def __init__(self, obj, pool):
        self.obj = obj
        self.pool = pool

    def __enter__(self):
        return self.obj

    def __exit__(self, typ, val, tb):
        self.pool.add_obj(self.obj)


class Pool:
    def __init__(self, objects):
        self.pool = Queue()
        for obj in objects:
            self.pool.put(obj)

    def lease(self):
        """
        Lease an object from the pool.
        """
        return Resource(self.pool.get(), self)

    def add_obj(self, obj):
        """
        Resource is in charge of adding a new object to the pool.
        """
        self.pool.put(obj)