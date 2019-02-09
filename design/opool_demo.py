from threading import Thread, Barrier
from time import sleep
from random import random
import uuid

from design.opool import Pool


def worker(n, barrier, pool):
    # Wait till all threads are ready.
    barrier.wait()
    # Just to emulate a real behaviour
    sleep(random()/15)
    # Lease an object from the pool
    # Context manager is the way to use it.
    with pool.lease() as val:
        print("worker {} got resource {}"
                .format(n, val.id)
            )

class Demo:
    def __init__(self):
        self.id = uuid.uuid4()

if __name__ == '__main__':
    n = 10
    barrier = Barrier(n)
    pool = Pool([
        Demo(),
        Demo(),
        Demo(),
        ])

    for i in range(n):
        Thread(
            target=worker,
            args=(i, barrier, pool)
            ).start()