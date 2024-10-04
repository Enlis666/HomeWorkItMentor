import pytest

@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5]

@pytest.fixture
def sample_dict():
    return {"key1": "value1", "key2": "value2"}
