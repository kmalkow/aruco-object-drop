from aruco_object_drop.src.main import add_numbers


def test_add_numbers():
    """Short description."""

    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
