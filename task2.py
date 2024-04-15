"""
Написать функцию, которая принимает на вход два целых числа (минимум и максимум)
и возвращает список всех простых чисел в заданном диапазоне.
"""

from typing import Generator


def _primes_generator(min_num: int, max_num: int) -> Generator[int, None, None]:
    if min_num < 0 or max_num < 0:
        raise ValueError("Minimal and maximum numbers must be positive")
    
    primes = [2]
    if min_num <= 2:
        yield 2
    for num in range(3, max_num + 1):
        for prime in primes:
            if num % prime == 0:
                break
        else:
            primes.append(num)
            if num >= min_num:
                yield num


def get_simple_numbers(min_num: int, max_num: int) -> list[int]:
    return list(_primes_generator(min_num=min_num, max_num=max_num))


if __name__ == "__main__":
    assert get_simple_numbers(min_num=1, max_num=10) == [2, 3, 5, 7]
    assert get_simple_numbers(min_num=15, max_num=40) == [17, 19, 23, 29, 31, 37]
    assert get_simple_numbers(min_num=2, max_num=11) == [2, 3, 5, 7, 11]
