import unittest

from sum import sum

class SumTests(unittest.TestCase):
  def test_adding_1_2(self):
    self.assertEqual(sum(1, 2), 3)

  @unittest.skip("skipping")
  def test_adding_3_2(self):
    self.assertEqual(sum(3, 2), 5)

if __name__ == '__main__':
  unittest.main()