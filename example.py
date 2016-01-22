def add_numbers(f1, f2):
    return f1 + f2


def test_add_numbers():
    assert (add_numbers(1.0, 2.0) == 3.0)


def subtract_numbers(f1, f2):
    return f1 - f2


def test_subtract_numbers():
    assert (subtract_numbers(1.0, 2.0) == -1.0)


def multiply_numbers(f1, f2):
    return f1*f2
