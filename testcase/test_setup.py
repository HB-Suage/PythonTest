class TestSetup:
  num = 0

  @staticmethod
  def setup_class():
    # TestSetup.num += 1
    pass

  @staticmethod
  def setup_method():
    # TestSetup.num += 1
    pass

  def test_setup(self):
    # assert TestSetup.num == 3
    pass

  def test_setup1(self):
    # assert TestSetup.num == 3
    pass

  def test_setup2(self, t_fixture):
    print(f"...........{t_fixture}")
    assert 'w' in t_fixture

  def test_setup3(self):
    # assert TestSetup.num == 3
    pass

  @staticmethod
  def teardown_method():
    print("结束!")
