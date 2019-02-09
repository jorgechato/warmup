"""
Object pool library
Constrains:
    - Assuming you have a limited N number of object to be share.

This is a simple Pool, where the client is in charge of reuse and
create new objects if needed.
"""


class Pool:
    """
    Client objects
    """

    def __init__(self, size, obj):
        self._reusables = [obj() for _ in range(size)]

    def acquire(self):
        return self._reusables.pop()

    def release(self, reusable):
        self._reusables.append(reusable)


if __name__ == '__main__':
    class Te:
        id = 1

    pool = Pool(5, Te)
    reusable1 = pool.acquire()
    reusable1.id = 5

    reusable2 = pool.acquire()
    reusable2.id = 7

    pool.release(reusable1)
    pool.release(reusable2)

    for i in range(6):
        print(pool.acquire().id)
