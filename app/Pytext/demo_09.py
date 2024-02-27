import pytest


def data():
    return [1, 2, 3]


@pytest.mark.parametrize('a', data())
def test_aa(a):
    print('11111')
    print('a=%', a)
    assert a == 2


@pytest.mark.parametrize('a, b ', [(1, 2), (3, 3), (1, 3)])
def test_01(a, b):
    print('aaaaaaaaaaaa')
    print('a=%', a)
    print('b=%', b)
    assert a == b


if __name__ == '__main__':
    pytest.main(['-s', 'demo_09.py'])
