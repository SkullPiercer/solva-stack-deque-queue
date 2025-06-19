from tasks import FirstUniqueCharFinder


def test_unique_chars():
    finder = FirstUniqueCharFinder()
    assert finder.find("leetcode") == 'l'
    assert finder.find("abaccdeff") == 'b'

def test_no_unique_char():
    finder = FirstUniqueCharFinder()
    assert finder.find("aabbccdd") == '_'

def test_single_char():
    finder = FirstUniqueCharFinder()
    assert finder.find("z") == 'z'
