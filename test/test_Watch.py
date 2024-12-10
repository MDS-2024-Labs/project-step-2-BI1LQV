import unittest
from reactive.observer.Watch import Watch
from reactive.observable.Reactive import Reactive

class TestWatch(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print('Watch test start')
    
    @classmethod
    def tearDownClass(self):
        print('Watch test end')

    def setUp(self):
        self.R1 = Reactive({"name": "John", "age": 20})
        self._executed_1 = False
        def watchLambda1():
            self.R1.name
            self.R1.age
            self._executed_1 = True
        self.W1 = Watch(watchLambda1)
        self._executed_1 = False

        self.R2 = Reactive({"name": "Steven", "age": 22})
        self._executed_2 = False
        def watchLambda2():
            self.R2.name
            self.R2.age
            self._executed_2 = True
        self.W2 = Watch(watchLambda2)
        self._executed_2 = False

    def tearDown(self):
        self.R1 = None
        self.W1.stop()
        self.W1 = None
        self._executed_1 = False

        self.R2 = None
        self.W2.stop()
        self.W2 = None
        self._executed_2 = False
    
    def test_name(self):
        self.R1.name = "Mike"
        self.R2.name = "Steve"
        self.assertTrue(self._executed_1)
        self.assertTrue(self._executed_2)

        self._executed_1 = False
        self._executed_2 = False
        self.W1.stop()
        self.W2.stop()
        self.R1.name = "Jane"
        self.R2.name = "Zeka"
        self.assertFalse(self._executed_1)
        self.assertFalse(self._executed_2)

    def test_age(self):
        self.R1.age = 25
        self.R2.age = 30
        self.assertTrue(self._executed_1)
        self.assertTrue(self._executed_2)

        self._executed_1 = False
        self._executed_2 = False
        self.W1.stop()
        self.W2.stop()
        self.R1.age = 45
        self.R2.age = 60
        self.assertFalse(self._executed_1)
        self.assertFalse(self._executed_2)










    

