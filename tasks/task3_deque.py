class SlidingWindowMax:
    """
    Задача: Максимум в скользящем окне.

    Реализуйте класс SlidingWindowMax с методом compute(),
    который принимает список чисел и размер окна k,
    и возвращает список максимумов для каждого окна при скольжении слева направо.

    Требуется использовать дек для оптимизации (O(n)).

    Примеры:
    >>> SlidingWindowMax().compute([1,3,-1,-3,5,3,6,7], 3) -> [3,3,5,5,6,7]
    >>> SlidingWindowMax().compute([1], 1) -> [1]
    >>> SlidingWindowMax().compute([9, 11], 2) -> [11]
    """

    def compute(self, nums: list[int], k: int) -> list[int]:
        raise NotImplementedError
