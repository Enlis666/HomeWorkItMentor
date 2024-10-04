from scr.main_code import add

def test_add(sample_data):
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
