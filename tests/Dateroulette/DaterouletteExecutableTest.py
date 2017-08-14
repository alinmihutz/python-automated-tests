from selenium import webdriver
from core.executable.ExecutableTest import ExecutableTest


class DaterouletteExecutableTest(ExecutableTest):
    TEST_NAME = 'Dateroulette'

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_one(self):
        self.failUnlessEqual(1 + 1, 2, 'FAILED')

    def test_two(self):
        self.failUnlessEqual(1 + 1, 2, 'FAILED')
