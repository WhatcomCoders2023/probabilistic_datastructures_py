"""Class for Bloom Filter."""

import math
import mmh3
from bitarray import bitarray


class BloomFilter:
    """Bloom Filter is a probablistic data structure for set membership.

    Attributes:
        capacity: Total expected number of element in bloom filter.
        fp_prob: False positive probability or error rate (0.0-1.0).
        size: Size of bit array.
        bit_array: Bit array or array whose index are True and False.
        num_of_hash_functions: Total of hash functions used.
    """

    def __init__(self, capacity: int, fp_prob: float):
        self.capacity = capacity
        self.fp_prob = fp_prob
        self.size = self._get_size_of_bit_array()
        self.bit_array = bitarray(self.size)
        self.num_of_hash_functions = self._get_num_of_hash_functions()

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

    def add(self, item: str) -> None:
        """Adds item to bloom filter.
        
        Item is passed through a series of hash functions. The hash 
        value is used to determine which index(s) to set True. This
        series of True values constitute our element. 

        Collisions are possible and are set by our fp_prob parameter.

        Args:
            item: String value of item to be placed in bloom filter.
        """
        for i in range(self.num_of_hash_functions):
            hash_index = mmh3.hash(item, i) % self.size
            self.bit_array[hash_index] = True

    def exists(self, item: str) -> None:
        """Checks existence of item in bloom filter.

        Item is passed through a series of hash functions. If
        any index in the bit array is false, this means that
        the item is definitely not in the set. 

        Otherwise, the item may possibly exist in the set.
        Args:
            item: String value of item to be placed in bloom filter.
        """
        for i in range(self.num_of_hash_functions):
            hash_value = mmh3.hash(item, i) % self.size
            if self.bit_array[hash_value] == False:
                return False
        return True