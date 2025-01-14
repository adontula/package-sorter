import pytest
from package_sort.sort import sort

def test_standard_package():
    assert sort(10, 10, 10, 5), "STANDARD"

def test_standard_package_small():
    assert sort(1, 1, 1, 1), "STANDARD"

def test_standard_package_large():
    assert sort(99.99, 99.99, 99.99, 19.99), "STANDARD"

def test_bulky_package_by_dimension():
    assert sort(150, 10, 10, 5), "SPECIAL"

def test_bulky_package_by_volume():
    assert sort(149, 149, 149, 5), "SPECIAL"

def test_heavy_package():
    assert sort(10, 10, 10, 20), "SPECIAL"

def test_very_heavy_package():
    assert sort(10, 10, 10, 200), "SPECIAL"

def test_rejected_package():
    assert sort(150, 10, 10, 20), "REJECTED"

def test_firmly_rejected_package():
    assert sort(1000, 1000, 1000, 200), "REJECTED"

def test_nonnumeric_input_errors():
    with pytest.raises(ValueError):
        sort("a", 10, 10, 5)

def test_zero_dimension_errors():
    with pytest.raises(ValueError):
        sort(0, 0, 0, 5)

def test_zero_mass_errors():
    with pytest.raises(ValueError):
        sort(10, 10, 10, 0)

def test_negative_dimension_errors():
    with pytest.raises(ValueError):
        sort(-10, 10, 10, 5)

def test_negative_mass_errors():
    with pytest.raises(ValueError):
        sort(10, 10, 10, -5)


if __name__ == "__main__":
    pytest.main()
