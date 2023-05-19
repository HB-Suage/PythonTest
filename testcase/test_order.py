# -*- coding = utf-8 -*-
# @Time : 2023/5/18 13:29
# @Author : LiangBoQing
# @File : test_order


import pytest


@pytest.mark.run(order=2)
@pytest.mark.m1
# @pytest.mark.skip(reason="test_skip")
def test_1():
  assert True



@pytest.mark.run(order=1)
# @pytest.mark.skipif(True, reason="test_skip")
@pytest.mark.m2
def test_2():
  assert True