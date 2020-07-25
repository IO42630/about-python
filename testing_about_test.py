from unittest import TestCase


class TestingAboutTest(TestCase):
    def test_do(self):
        from testing_about import A
        self.assertTrue(A.do(self, number=5))
