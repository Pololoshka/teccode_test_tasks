"""
Написать программу, которая сортирует список строк по длине,
сначала по возрастанию, а затем по убыванию.
"""


def sort_ascending(data: list[str]) -> list[str]:
    return sorted(data, key=len)


def sort_descending(data: list[str]) -> list[str]:
    return sorted(data, key=len, reverse=True)


if __name__ == "__main__":
    assert sort_ascending([]) == []
    assert sort_ascending(["asdf", "asd", "as"]) == ["as", "asd", "asdf"]
    assert sort_ascending(["asdf", "as", "asd"]) == ["as", "asd", "asdf"]

    assert sort_descending([]) == []
    assert sort_descending(["as", "asd", "asdf"]) == ["asdf", "asd", "as"]
    assert sort_descending(["as", "asdf", "asd"]) == ["asdf", "asd", "as"]
