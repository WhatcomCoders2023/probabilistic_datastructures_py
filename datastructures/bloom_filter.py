"""Class for Bloom Filter."""

import math
from bitarray import bitarray


class BloomFilter:
    """Bloom Filter is a probablistic data structure for set membership.

    Attributes:
        capacity: Total expected number of element in bloom filter.
        fp_prob: False positive probability or error rate (0.0-1.0).
    """

    def __init__(self, capacity: int, fp_prob: float):
        self.capacity = capacity
        self.fp_prob = fp_prob
        self.size = self._get_size_of_bit_array()
        self.bit_array = bitarray(self.size)
        self.num_of_hash_functions = self._get_hash_count()

    def _get_size_of_bit_array(self) -> int:
        """Create size of bit array. 
        
        Formula is based on required number of bits or capacity
        and desired false positive probability.

        https://en.wikipedia.org/wiki/Bloom_filter#Optimal_number_of_hash_functions
        """

        size_of_bit_array = -(self.capacity * math.log(self.fp_prob) /
                              math.log(2)**2)

        size_of_bit_array = math.ceil(size_of_bit_array)
        return size_of_bit_array

    def _get_num_of_hash_functions(self) -> int:
        """Determine the optimal number of hash functions to use. 

        The fp_prob primarily determines the number of hash functions. Lower 
        fp_prob = more hash functions and vice versa. This is because the size 
        of the bit array is based on (capacity * fp_prob)

        https://en.wikipedia.org/wiki/Bloom_filter#Optimal_number_of_hash_functions
        """
        num_of_hash_functions = (self.size / self.capacity) * math.log(2)
        num_of_hash_functions = round(num_of_hash_functions, 0)
        return int(num_of_hash_functions)
