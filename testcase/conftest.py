# -*- coding = utf-8 -*-
# @Time : 2023/5/19 16:36
# @Author : LiangBoQing
# @File : conftest
import inspect

import pytest


def get_current_code_info():
  # 获取当前文件名
  current_file = inspect.getfile(inspect.currentframe())

  # 获取当前类名（如果存在）
  current_class = None
  stack = inspect.stack()
  for frame_info in stack:
    frame = frame_info[0]
    if 'self' in frame.f_locals:
      current_class = frame.f_locals['self'].__class__.__name__
      break

  # 获取调用get_current_code_info()的函数名
  caller_frame = stack[1]
  caller_function = inspect.getframeinfo(caller_frame[0]).function

  # 构造包含信息的字典
  code_info = {
    'current_file': current_file,
    'current_class': current_class,
    'caller_function': caller_function
  }

  return code_info['caller_function']


@pytest.fixture(
  scope='function',
  params=['sdffg', 'dfgf', 'ewqtrtpjd'],
  # autouse='',
  # ids='',
  # name=''
)
def t_fixture(request):
  print(get_current_code_info())
  yield request.param
  print("aba")
