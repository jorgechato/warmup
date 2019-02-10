import unittest
from unittest.mock import Mock
from design.opool import Pool
from design.opool import Resource


class PoolTest(unittest.TestCase):
    def test_lease_multiple(self):
        actual = Pool([1, 2, 3])
        expected = Mock()
        attrs = {'lease.side_effect': [1, 2, 3, 1, 2]}
        expected.configure_mock(**attrs)

        for i in range(len(attrs['lease.side_effect'])):
            with actual.lease() as val_a:
                self.assertEqual(expected.lease(), val_a, msg="Objects should be equals")

    def test_add_obj(self):
        actual = Pool([1, 2])
        actual.add_obj(3)
        expected = Mock()
        attrs = {'lease.side_effect': [1, 2, 3]}
        expected.configure_mock(**attrs)

        for i in range(len(attrs['lease.side_effect'])):
            with actual.lease() as val_a:
                self.assertEqual(expected.lease(), val_a, msg="Objects should be equals")

    def test_lease(self):
        actual = Pool([1, 2, 3])
        expected = Mock()
        attrs = {'lease.side_effect': [1, 2, 3]}
        expected.configure_mock(**attrs)

        for i in range(len(attrs['lease.side_effect'])):
            with actual.lease() as val_a:
                self.assertEqual(expected.lease(), val_a, msg="Objects should be equals")


if __name__ == '__main__':
    unittest.main()
