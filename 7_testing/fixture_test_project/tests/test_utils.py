from scr.utils import multiply


def test_multiply_with_sample_dict(sample_dict):
    assert multiply(len(sample_dict), 2) == 4
    assert multiply(len(sample_dict), 3) == 6
