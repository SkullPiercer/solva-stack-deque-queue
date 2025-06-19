class BracketValidator:
    """
    Задача: Проверка правильности скобочной последовательности.

    Реализуйте класс BracketValidator с методом is_valid(), который принимает строку, содержащую только
    символы '(', ')', '[', ']', '{', '}', и определяет, является ли она корректной.

    Условия корректности:
    - Каждая открывающая скобка должна иметь соответствующую закрывающую скобку того же типа.
    - Скобки должны быть закрыты в правильном порядке.

    Примеры:
    >>> BracketValidator().is_valid("()[]{}") -> True
    >>> BracketValidator().is_valid("([{}])") -> True
    >>> BracketValidator().is_valid("([)]") -> False
    >>> BracketValidator().is_valid("(") -> False
    """

    def is_valid(self, s: str) -> bool:
        raise NotImplementedError
