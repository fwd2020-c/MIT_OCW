def add(a, b):
    return a + b


def test_add():
    assert add(2, 3) == 4
    assert add('space', 'ship') == 'spaceship'
