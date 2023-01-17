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

    def test_hash_function_count(self):
        expected_num_of_hash_functions = 3
        num_of_hash_functions = self.bloom_filter._get_num_of_hash_functions()
        self.assertEqual(num_of_hash_functions, expected_num_of_hash_functions)

    def test_add_and_check_item(self):
        values = ['these', 'are', 'random', 'strings']
        for value in values:
            self.bloom_filter.add(value)

        for value in values:
            self.assertFalse(not self.bloom_filter.exists(value))


if __name__ == '__main__':
    unittest.main()
