import unittest
from reactive.observable.Reactive import Reactive
from reactive.observer.Watch import Watch
from reactive.observer.WatchAttr import WatchAttr

class TestWatchAttr(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("WatchAttr test start")
    
    @classmethod
    def tearDownClass(self):
        print("WatchAttr test end")

    def setUp(self):
        self.R1 = Reactive({"name": "John", "age": 20})
        self.R2 = Reactive({"name": "Steven", "age": 22})
        self._executed_1 = False
        def watchLambda1():
            print("R1 name:", self.R1.name, "R1 age:", self.R1.age)
            print("R2 name:", self.R2.name, "R2 age:", self.R2.age)
            self._executed_1 = True
        self.WA1 = WatchAttr(attributes = [self.R1, self.R2], effect = watchLambda1)
        self._executed_1 = False

        self.R3 = Reactive({"name": "Alan", "age": 27})
        self.R4 = Reactive({"name": "Max", "age": 32})
        self._executed_2 = False
        def watchLambda2():
            print("R3 name:", self.R3.name, "R3 age:", self.R3.age)
            print("R4 name:", self.R4.name, "R4 age:", self.R4.age)
            self._executed_2 = True
        self.WA2 = WatchAttr(attributes = [self.R3, self.R4], effect = watchLambda2)
        self._executed_2 = False

    def tearDown(self):
        self.R1 = None
        self.R2 = None
        self.WA1.stop()
        self.WA1 = None
        self._executed_1 = False

        self.R3 = None
        self.R4 = None
        self.WA2.stop()
        self.WA2 = None
        self._executed_2 = False
    
    def test_set_name_1(self):
        self.R1.name = "Mike"
        self.R3.name = "Steve"
        self.assertEqual(self._executed_1, True)
        self.assertEqual(self._executed_2, True)

    def test_set_age_1(self):
        self.R2.age = 25
        self.R4.age = 30
        self.assertEqual(self._executed_1, True)
        self.assertEqual(self._executed_2, True)

    def test_set_name_2(self):
        self.WA1.stop()
        self.WA2.stop()
        self.R1.name = "Jane"
        self.R4.name = "Zeka"
        self.assertEqual(self._executed_1, False)
        self.assertEqual(self._executed_2, False)

    def test_set_age_2(self):
        self.WA1.stop()
        self.WA2.stop()
        self.R2.age = 45
        self.R3.age = 60
        self.assertEqual(self._executed_1, False)
        self.assertEqual(self._executed_2, False)