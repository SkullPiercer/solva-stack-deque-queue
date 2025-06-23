class FirstUniqueCharFinder:
    """
    Задача: Поиск первого уникального символа.

    Реализуйте класс FirstUniqueCharFinder с методом find(),
    который принимает строку из строчных букв
    и возвращает первый символ, встречающийся
    только один раз. Если таких нет — возвращает '_'.

    Используйте очередь.

    Примеры:
    >>> FirstUniqueCharFinder().find("leetcode") -> 'l'
    >>> FirstUniqueCharFinder().find("aabbccdd") -> '_'
    >>> FirstUniqueCharFinder().find("abaccdeff") -> 'b'

    Подсказка: Из библиотеки collection используй Counter
    """

    def find(self, s: str) -> str:
        raise NotImplementedError
