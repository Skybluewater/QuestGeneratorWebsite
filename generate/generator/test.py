import unittest
from .solve import solvable
from .OriginRequest import BiTree, QuestGenerator


class QuesTest(unittest.TestCase):
    def setUp(self) -> None:
        self.question = QuestGenerator()

    def tearDown(self) -> None:
        pass

    def test_ques1(self):
        questions = self.question.generate(10, 5, 0, 0, 0, 9)
        print(questions)

    def test_ques2(self):
        questions = self.question.generate(10, 5, 1, 0, 0, 9)
        print(questions)

    def test_ques3(self):
        questions = self.question.generate(10, 5, 0, 1, 0, 9)
        print(questions)

    def test_ques4(self):
        questions = self.question.generate(10, 5, 0, 0, 1, 9)
        print(questions)

    def test_ques5(self):
        questions = self.question.generate(5, 8, 0, 0, 0, 15)
        print(questions)

    def test_ques6(self):
        questions = self.question.generate(1000, 5, 1, 1, 1, 9)
        print(questions)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(QuesTest('test_ques1'))
    suite.addTest(QuesTest('test_ques2'))
    suite.addTest(QuesTest('test_ques3'))
    suite.addTest(QuesTest('test_ques4'))
    suite.addTest(QuesTest('test_ques5'))
    suite.addTest(QuesTest('test_ques6'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
