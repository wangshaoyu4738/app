import pytest


# 函数要以test开头
def test_01():
    print('aaaaaaaaaaaa')
    assert 1


def test_02():
    print('sssssssssssss')
    assert 0


class Test_01():

    def test_a(self):
        print('sssssssssssss')

    def test_b(self):
        print('sssssssssssss')


if __name__ == '__main__':
    pytest.main(['-s', 'demo_01.py'])



