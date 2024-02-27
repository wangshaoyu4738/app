import pytest


@pytest.fixture(params=[1, 2, 3])
def test_aa(request):
    return request.param


# 函数要以test开头
def test_01(test_aa):
    print('aaaaaaaaaaaa')
    print('test_aa:', test_aa)
    assert test_aa == 3


def test_02():
    print('bbbbbbbbbbbb')
    assert 1


if __name__ == '__main__':
    pytest.main(['-s', 'demo_06.py'])
