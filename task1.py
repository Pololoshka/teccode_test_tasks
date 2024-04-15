"""
Написать функцию, которая принимает на вход список целых чисел и возвращает новый список,
содержащий только уникальные элементы из исходного списка.
"""

from typing import Counter


def filter_unique_elements(data: list[int]) -> list[int]:
    counter = Counter(data)
    return [el for el in data if counter[el] == 1]


if __name__ == "__main__":
    assert filter_unique_elements([1, 1, 2]) == [2]
    assert filter_unique_elements([]) == []
    assert filter_unique_elements([1, 1, 2, 2]) == []
    assert filter_unique_elements([1, 2, 3]) == [1, 2, 3]
