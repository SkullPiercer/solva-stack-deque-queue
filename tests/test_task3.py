from tasks import SlidingWindowMax


def test_sliding_window():
    swm = SlidingWindowMax()
    assert swm.compute([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
    assert swm.compute([1], 1) == [1]
    assert swm.compute([9, 11], 2) == [11]
    assert swm.compute([4, -2], 2) == [4]

def test_edge_cases():
    swm = SlidingWindowMax()
    assert swm.compute([], 3) == []
    assert swm.compute([1, 2], 0) == []
