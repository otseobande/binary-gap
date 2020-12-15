from app import binary_gap

def test_binary_gap():
    assert binary_gap(1041) == 5
    assert binary_gap(32) == 0
    assert binary_gap(529) == 4
