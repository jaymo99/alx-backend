#!/usr/bin/env python3
"""
1-simple_pagination module
"""

import csv
import math
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple containing a start index and an end index
    corresponding to the range of indexes for particular
    pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns a page from a dataset
        """
        assert isinstance(page, int), "argument 'page' must be an integer"
        assert isinstance(page_size, int), \
            "argument 'page_size' must be an integer"
        assert page > 0, "argument 'page' must be greater than zero"
        assert page_size > 0, "Argument 'page_size' must be greater than zero"

        start_index, end_index = index_range(page, page_size)
        return self.dataset()[start_index: end_index]
