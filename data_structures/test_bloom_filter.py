import unittest
from bloom_filter import BloomFilter


class TestBloomFilter(unittest.TestCase):

    def setUp(self):
        capacity = 10
        false_positive_rate = 0.1
        self.bloom_filter = BloomFilter(capacity, false_positive_rate)

    def test_size_of_bit_array(self):
        expected_size_of_bloom_filter = 48
        bloom_filter_size = len(self.bloom_filter.bit_array)
        self.assertEqual(bloom_filter_size, expected_size_of_bloom_filter)


if __name__ == '__main__':
    unittest.main()